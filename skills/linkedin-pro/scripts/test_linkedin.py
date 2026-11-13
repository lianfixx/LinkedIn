#!/usr/bin/env python3
"""Pruebas de linkedin.py. Correr: python3 -m unittest discover -s skills/linkedin-pro/scripts -p 'test_*.py'"""
from __future__ import annotations

import contextlib
import copy
import datetime as dt
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path

import linkedin as L

REAL_SKILL = L.SKILL
REAL_RAIZ = L.RAIZ


def futuro(dias: int = 3) -> str:
    return (L.ahora().date() + dt.timedelta(days=dias)).isoformat()


BASE = {
    "id": "t-1",
    "pilar": "ia-derecho",
    "formato": "texto",
    "texto": "La IA no firma demandas.\n\nRevisé tres herramientas para redactar escritos y las tres inventaron una "
             "tesis. Mi regla: la IA propone, el abogado verifica en el Semanario.",
    "para_quien": "abogados jóvenes que empiezan a usar IA en el despacho",
    "aporta": "un método de verificación aplicable el lunes",
}


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "cuenta").mkdir()
        (self.tmp / "puente").mkdir()
        (self.tmp / "red").mkdir()
        shutil.copy(REAL_RAIZ / "cuenta" / "perfil.json", self.tmp / "cuenta" / "perfil.json")
        self.viejo = (L.CUENTA, L.PUENTE, L.ESTADO_RED)
        L.CUENTA, L.PUENTE, L.ESTADO_RED = self.tmp / "cuenta", self.tmp / "puente", self.tmp / "red" / "estado.json"
        self.cfg = L.perfil()

    def tearDown(self):
        L.CUENTA, L.PUENTE, L.ESTADO_RED = self.viejo
        shutil.rmtree(self.tmp)

    def rev(self, **cambios):
        b = copy.deepcopy(BASE)
        b.update(cambios)
        return L.revisar(b, [], self.cfg)

    def errores(self, **cambios):
        return self.rev(**cambios)[0]

    def avisos(self, **cambios):
        return self.rev(**cambios)[1]

    def correr(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = L.main(list(argv))
        return code, out.getvalue() + err.getvalue()

    def archivo(self, posts) -> Path:
        ruta = self.tmp / "cuenta" / "privado.json"
        ruta.write_text(json.dumps(posts, ensure_ascii=False), encoding="utf-8")
        return ruta


class Basico(Base):
    def test_borrador_limpio(self):
        self.assertEqual(self.errores(), [])

    def test_faltan_campos(self):
        e = self.errores(para_quien="", aporta=" ")
        self.assertTrue(any("para_quien" in x for x in e))
        self.assertTrue(any("aporta" in x for x in e))

    def test_pilar_y_formato(self):
        self.assertTrue(any("pilar" in x for x in self.errores(pilar="lifestyle")))
        self.assertTrue(any("formato" in x for x in self.errores(formato="hilo")))

    def test_no_objeto(self):
        self.assertEqual(L.revisar("hola", [], self.cfg)[0], ["el borrador debe ser un objeto JSON"])
        self.assertTrue(L.revisar({"texto": " "}, [], self.cfg)[0])

    def test_largo_maximo(self):
        lim = L.limites_formato()["texto"]["max_texto"]
        e = self.errores(texto="a" * (lim + 1))
        self.assertTrue(any("caracteres" in x for x in e))
        self.assertFalse(any("caracteres; el máximo" in x for x in self.errores(texto="a " * (lim // 2 - 5))))

    def test_gancho_largo_avisa(self):
        self.assertTrue(any("primera línea" in x for x in self.avisos(texto="palabra " * 40)))


class Anzuelos(Base):
    def test_detecta(self):
        for t in ("Comenta GUÍA y te la mando por mensaje.", "Dale like si estás de acuerdo.",
                  "Reacciona con ❤️ si te pasó.", "Si estás de acuerdo, comparte.", "Etiqueta a un colega que lo necesite.",
                  "Comenta 'PDF' para recibir la plantilla.", "Escribe «sí» en los comentarios.",
                  "Conéctate conmigo y te mando el formato."):
            self.assertTrue(any("anzuelo" in x for x in self.errores(texto=t)), t)

    def test_no_marca_conversacion(self):
        for t in ("¿Ustedes cómo verifican las citas que propone la IA? Me interesa leerlos.",
                  "Comenté el criterio con un colega y coincidimos.", "El artículo comenta la reforma.",
                  "Compartí esto en clase de la maestría."):
            self.assertFalse(any("anzuelo" in x for x in self.errores(texto=t)), t)

    def test_sigueme_avisa(self):
        self.assertTrue(any("plantilla" in x for x in self.avisos(texto="Sígueme para más contenido así.")))


class Limites(Base):
    def test_castorena(self):
        self.assertTrue(any("despacho" in x for x in self.errores(texto="Aprendí mucho en Castorena Abogados.")))

    def test_clientes(self):
        for t in ("Un cliente me preguntó ayer por su despido.", "Mis clientes siempre preguntan lo mismo.",
                  "En el expediente 1234/2025 pasó algo curioso.", "En el despacho atendimos un caso así."):
            self.assertTrue(any("límite" in x for x in self.errores(texto=t)), t)

    def test_excepcion(self):
        e, w = self.rev(texto="Un cliente hipotético llega con un contrato.", excepcion_limite="ejemplo hipotético")
        self.assertFalse(any("límite" in x for x in e))
        self.assertTrue(any("excepción" in x for x in w))

    def test_insultos(self):
        self.assertTrue(any("ataque" in x for x in self.errores(texto="El diputado es un idiota.")))
        self.assertFalse(any("ataque" in x for x in self.errores(texto="Ese día fui un idiota con el tiempo.")))
        self.assertTrue(any("persona" in x for x in self.avisos(texto="Es una propuesta de payasos.")))

    def test_captacion(self):
        for t in ("Agenda tu consulta conmigo.", "Primera consulta gratis este mes.", "Contrátame para tu divorcio.",
                  "Escríbeme por DM y vemos tu caso.", "Te ayudo con tu despido.", "Honorarios accesibles.",
                  "Desde $1,500 + IVA."):
            self.assertTrue(any("captación" in x for x in self.errores(texto=t)), t)

    def test_captacion_permitida(self):
        self.cfg["captacion_milla"] = True
        self.assertFalse(any("captación" in x for x in self.errores(texto="Agenda tu consulta conmigo.")))

    def test_milla_y_partido(self):
        self.assertTrue(any("MILLA" in x for x in self.avisos(texto="Fundé MILLA ABOGADOS en 2025.")))
        self.assertTrue(any("partido" in x for x in self.avisos(texto="Hoy en el PAN discutimos la reforma.")))
        self.assertFalse(any("partido" in x for x in self.avisos(texto="El pan de muerto es lo mejor.")))

    def test_asesoria(self):
        self.assertTrue(any("asesora" in x for x in self.avisos(texto="En tu caso debes demandar ya.")))


class Sustancia(Base):
    def test_opinion_requiere_postura(self):
        self.assertTrue(any("opinion_emi" in x for x in self.errores(pilar="opinion")))
        self.assertFalse(any("opinion_emi" in x for x in self.errores(pilar="opinion", opinion_emi="Es inconstitucional.")))

    def test_gym_requiere_leccion(self):
        t = "Hoy en el gym entendí algo sobre la constancia."
        self.assertTrue(any("leccion" in x for x in self.errores(pilar="carrera", texto=t)))
        self.assertFalse(any("leccion" in x for x in self.errores(pilar="carrera", texto=t, leccion_profesional="La constancia gana.")))
        self.assertTrue(any("leccion" in x for x in self.avisos(pilar="ia-derecho", texto=t)))

    def test_cita_legal(self):
        self.assertTrue(any("fuentes" in x for x in self.errores(cita_legal=True)))
        self.assertTrue(any("fuentes" in x for x in self.errores(cita_legal=True, fuentes=["https://bit.ly/x"])))
        self.assertFalse(any("fuentes" in x for x in self.errores(cita_legal=True, fuentes=["https://www.dof.gob.mx/x"])))
        self.assertTrue(any("oficial" in x for x in self.avisos(cita_legal=True, fuentes=["https://blog.example.com/x"])))
        self.assertTrue(any("cita_legal" in x for x in self.avisos(texto="El artículo 123 constitucional dice algo.")))

    def test_estilo(self):
        w = self.avisos(texto="Me complace anunciar algo — en resumen, sinergia. #a #b #c #d")
        self.assertTrue(any("plantilla" in x for x in w))
        self.assertTrue(any("raya" in x for x in w))
        self.assertTrue(any("hashtags" in x for x in w))

    def test_duplicado(self):
        hist = [{"id": "viejo", "fecha": "2026-11-01", "texto": BASE["texto"]}]
        e, _ = L.revisar(copy.deepcopy(BASE) | {"id": "nuevo"}, hist, self.cfg)
        self.assertTrue(any("casi idéntico" in x for x in e))
        hist_x = [{"id": "X:1", "fecha": "2026-11-01", "texto": BASE["texto"]}]
        e, _ = L.revisar(copy.deepcopy(BASE) | {"id": "nuevo"}, hist_x, self.cfg)
        self.assertTrue(any("en X" in x for x in e))
        otro = [{"id": "o", "fecha": "2026-11-01", "texto": "Hoy hablé de otro tema completamente distinto en clase."}]
        self.assertFalse(L.revisar(copy.deepcopy(BASE), otro, self.cfg)[0])


class Formatos(Base):
    def test_articulo(self):
        e = self.errores(formato="articulo")
        self.assertTrue(any("titulo" in x for x in e) and any("cuerpo" in x for x in e))
        self.assertFalse(self.errores(formato="articulo", titulo="IA y amparo", cuerpo="Texto largo del artículo."))

    def test_documento(self):
        e = self.errores(formato="documento", titulo="Guía")
        self.assertTrue(any("paginas" in x for x in e) and any("media" in x for x in e))
        self.assertFalse(self.errores(formato="documento", titulo="Guía", paginas=8, media="guia.pdf"))
        mx = L.limites_formato()["documento"].get("max_paginas")
        if mx:
            self.assertTrue(any("paginas" in x for x in self.errores(formato="documento", titulo="G", paginas=mx + 1, media="g.pdf")))

    def test_encuesta(self):
        lim = L.limites_formato()["encuesta"]
        ok = {"pregunta": "¿Usas IA para revisar contratos?", "opciones": ["Sí, siempre", "A veces", "Nunca"],
              "duracion": lim["duraciones"][0]}
        self.assertFalse(self.errores(formato="encuesta", encuesta=ok))
        mal = dict(ok, opciones=["Solo una"])
        self.assertTrue(any("opciones" in x for x in self.errores(formato="encuesta", encuesta=mal)))
        mal = dict(ok, opciones=["a", "A"])
        self.assertTrue(any("repetidas" in x for x in self.errores(formato="encuesta", encuesta=mal)))
        mal = dict(ok, duracion="5 años")
        self.assertTrue(any("duracion" in x for x in self.errores(formato="encuesta", encuesta=mal)))
        mal = dict(ok, opciones=["x" * (lim["max_opcion"] + 1), "b"])
        self.assertTrue(any("pasa de" in x for x in self.errores(formato="encuesta", encuesta=mal)))
        mal = dict(ok, pregunta="Comenta SI y te mando el resultado")
        self.assertTrue(any("anzuelo" in x for x in self.errores(formato="encuesta", encuesta=mal)))

    def test_video(self):
        self.assertTrue(any("duracion_s" in x for x in self.errores(formato="video", media="v.mp4")))
        self.assertFalse(self.errores(formato="video", media="v.mp4", duracion_s=45, subtitulos=True))
        mx = L.limites_formato()["video"].get("max_s")
        if mx:
            self.assertTrue(any("máximo" in x for x in self.errores(formato="video", media="v.mp4", duracion_s=mx + 1)))
        self.assertTrue(any("subtitulos" in x for x in self.avisos(formato="video", media="v.mp4", duracion_s=45)))


class Aprobacion(Base):
    def test_compuerta(self):
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00"}
        e, _ = L.revisar(b, [], self.cfg, "aprobado")
        self.assertTrue(any("aprobado_por_emi" in x for x in e) and any("huella" in x for x in e))
        b.update(aprobado_por_emi="sí", aprobado_huella=L.huella(b), reescrito="true")
        e, _ = L.revisar(b, [], self.cfg, "aprobado")
        self.assertTrue(any("aprobado_por_emi" in x for x in e) and any("reescrito" in x for x in e))

    def test_flujo_completo(self):
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00"}
        ruta = self.archivo([b])
        code, out = self.correr("entregar", str(ruta), "t-1")
        self.assertEqual(code, 2, out)  # sin aprobar no se entrega
        code, out = self.correr("aprobar", str(ruta), "t-1", "--medio", "chat de prueba", "--reescrito", "--sin-x")
        self.assertEqual(code, 0, out)
        code, out = self.correr("entregar", str(ruta), "t-1")
        self.assertEqual(code, 0, out)
        self.assertIn("PUBLICAR EN LINKEDIN", out)
        self.assertIn(BASE["texto"].split("\n")[0], out)
        url = "https://www.linkedin.com/posts/emiliano-milla_ia-activity-123"
        code, out = self.correr("publicado", str(ruta), "t-1", "--url", url)
        self.assertEqual(code, 2, out)  # la fecha planeada es futura: aún no sale
        code, out = self.correr("publicado", str(ruta), "t-1", "--url", "https://www.linkedin.com/x",
                                "--fecha", L.hoy(), "--hora", "00:01")
        self.assertEqual(code, 2, out)  # no es enlace de un post
        code, out = self.correr("publicado", str(ruta), "t-1", "--url", url, "--fecha", L.hoy(), "--hora", "00:01")
        self.assertEqual(code, 0, out)
        code, out = self.correr("publicado", str(ruta), "t-1", "--url", url, "--fecha", L.hoy(), "--hora", "00:01")
        self.assertEqual(code, 2, out)  # no se anota dos veces
        code, out = self.correr("metricas", "t-1", "--impresiones", "350", "--reacciones", "12", "--fuente", "captura")
        self.assertEqual(code, 0, out)
        code, out = self.correr("metricas", "t-1", "--impresiones", "-1", "--fuente", "captura")
        self.assertEqual(code, 2, out)
        fila = L.publicados()[0]
        self.assertEqual(fila["metricas"][0]["valores"], {"impresiones": 350, "reacciones": 12})
        self.assertEqual(len(fila["huella_texto"]), 64)

    def test_cambio_invalida(self):
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00"}
        ruta = self.archivo([b])
        self.assertEqual(self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")[0], 0)
        dato = json.loads(ruta.read_text(encoding="utf-8"))
        dato[0]["texto"] += " Una palabra más."
        ruta.write_text(json.dumps(dato, ensure_ascii=False), encoding="utf-8")
        code, out = self.correr("entregar", str(ruta), "t-1")
        self.assertEqual(code, 2)
        self.assertIn("huella", out)

    def test_cambio_de_encuesta_invalida(self):
        lim = L.limites_formato()["encuesta"]
        b = copy.deepcopy(BASE) | {"formato": "encuesta", "fecha": futuro(), "hora": "09:00",
                                   "encuesta": {"pregunta": "¿Sí?", "opciones": ["Sí", "No"], "duracion": lim["duraciones"][0]}}
        h1 = L.huella(b)
        b["encuesta"]["opciones"][1] = "Tal vez"
        self.assertNotEqual(h1, L.huella(b))

    def test_fecha_pasada(self):
        b = copy.deepcopy(BASE) | {"fecha": "2020-01-01", "hora": "09:00"}
        ruta = self.archivo([b])
        self.assertEqual(self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")[0], 0)
        code, out = self.correr("entregar", str(ruta), "t-1")
        self.assertEqual(code, 2)
        self.assertIn("ya pasaron", out)

    def test_fechas_invalidas(self):
        self.assertTrue(any("fecha" in x for x in self.errores(fecha="2026-02-30", hora="09:00")))
        self.assertTrue(any("hora" in x for x in self.errores(fecha=futuro(), hora="24:00")))


class Semana(Base):
    def pieza(self, i, dia, hora="09:00", pilar="ia-derecho"):
        return copy.deepcopy(BASE) | {"id": f"s-{i}", "fecha": dia, "hora": hora, "pilar": pilar,
                                      "texto": f"Pieza {i} sobre un tema distinto número {i * 7919} con su propio ángulo."}

    def test_cadencia(self):
        lunes = L.ahora().date() + dt.timedelta(days=7 - L.ahora().weekday())
        d = [(lunes + dt.timedelta(days=k)).isoformat() for k in range(5)]
        e, _ = L.revisar_semana([self.pieza(1, d[0]), self.pieza(2, d[2])], self.cfg, [])
        self.assertEqual(e, [])
        e, _ = L.revisar_semana([self.pieza(1, d[0]), self.pieza(2, d[2]), self.pieza(3, d[4])], self.cfg, [])
        self.assertTrue(any("por semana" in x for x in e))
        e, _ = L.revisar_semana([self.pieza(1, d[0], "08:00"), self.pieza(2, d[0], "18:00")], self.cfg, [])
        self.assertTrue(any("al día" in x for x in e) and any("separados" in x for x in e))
        e, _ = L.revisar_semana([self.pieza(1, d[0], "20:00"), self.pieza(2, d[1], "08:00")], self.cfg, [])
        self.assertTrue(any("separados" in x for x in e))

    def test_cuenta_publicados(self):
        lunes = L.ahora().date() + dt.timedelta(days=7 - L.ahora().weekday())
        ya = [self.pieza(9, lunes.isoformat())]
        e, _ = L.revisar_semana([self.pieza(1, (lunes + dt.timedelta(days=2)).isoformat()),
                                 self.pieza(2, (lunes + dt.timedelta(days=4)).isoformat())], self.cfg, ya)
        self.assertTrue(any("por semana" in x for x in e))

    def test_balance(self):
        lunes = L.ahora().date() + dt.timedelta(days=7 - L.ahora().weekday())
        piezas = [self.pieza(i, (lunes + dt.timedelta(days=7 * i)).isoformat(), pilar="opinion") for i in range(4)]
        _, w = L.revisar_semana(piezas, self.cfg, [])
        self.assertTrue(any("balance" in x for x in w))

    def test_ejemplo_documentado_pasa(self):
        ruta = REAL_SKILL / "assets" / "semana.ejemplo.json"
        posts = L.lista_de(L.leer_json(ruta))
        for p in posts:
            e, _ = L.revisar(p, [], self.cfg)
            self.assertEqual(e, [], p.get("id"))
        e, _ = L.revisar_semana(posts, self.cfg, [])
        self.assertEqual(e, [])


class Archivos(Base):
    def test_json_malo(self):
        ruta = self.tmp / "malo.json"
        ruta.write_text("{no", encoding="utf-8")
        code, out = self.correr("revisar", str(ruta))
        self.assertEqual(code, 2)
        self.assertIn("JSON inválido", out)
        code, out = self.correr("revisar", str(self.tmp / "noexiste.json"))
        self.assertEqual(code, 2)

    def test_perfil_malo(self):
        p = json.loads((self.tmp / "cuenta" / "perfil.json").read_text(encoding="utf-8"))
        p["captacion_milla"] = "false"
        (self.tmp / "cuenta" / "perfil.json").write_text(json.dumps(p), encoding="utf-8")
        with self.assertRaises(L.Falla):
            L.perfil()
        p["captacion_milla"] = False
        p["balance"] = {"ia-derecho": 0.5, "carrera": 0.5, "opinion": 0.5}
        (self.tmp / "cuenta" / "perfil.json").write_text(json.dumps(p), encoding="utf-8")
        with self.assertRaises(L.Falla):
            L.perfil()

    def test_ids_repetidos(self):
        ruta = self.archivo([copy.deepcopy(BASE), copy.deepcopy(BASE) | {"texto": "Otro texto distinto del todo, sin parecido."}])
        code, out = self.correr("revisar", str(ruta))
        self.assertEqual(code, 1)
        self.assertIn("repetido", out)

    def test_aprender_y_balance(self):
        self.assertEqual(self.correr("aprender", "Los documentos se guardan más que el texto")[0], 0)
        self.assertIn("Los documentos", (self.tmp / "cuenta" / "aprendizajes.md").read_text(encoding="utf-8"))
        code, out = self.correr("balance")
        self.assertEqual(code, 0)
        self.assertIn("Toca: ia-derecho", out)

    def test_vox_idea(self):
        self.assertEqual(self.correr("vox", "idea", "Video sobre IA en juzgados")[0], 0)
        self.assertIn("IA en juzgados", (self.tmp / "puente" / "para-vox.md").read_text(encoding="utf-8"))
        self.assertEqual(self.correr("vox", "idea", " ")[0], 2)

    def test_estado_red(self):
        self.correr("aprender", "Lección uno")
        code, out = self.correr("estado")
        self.assertEqual(code, 0, out)
        d = json.loads((self.tmp / "red" / "estado.json").read_text(encoding="utf-8"))
        self.assertEqual(d["contrato"], "redes-estado/0.1")
        self.assertEqual(d["red"], "linkedin")
        self.assertEqual(d["lecciones"][0]["texto"], "Lección uno")
        self.assertIn(d["cadencia"]["certeza"], ("oficial", "terceros", "criterio"))
        for f in d["formatos"]:
            self.assertIn(f["certeza"], ("oficial", "terceros", "criterio"))
        self.assertEqual(self.correr("estado", "--comprobar")[0], 0)
        self.correr("aprender", "Lección dos")
        self.assertEqual(self.correr("estado", "--comprobar")[0], 1)


class Fuentes(unittest.TestCase):
    def test_archivo_valido(self):
        d = L.cargar_fuentes()
        self.assertTrue(d["fuentes"])
        for f in d["fuentes"]:
            self.assertTrue(f["url"].startswith("https://"), f)
            self.assertIn(f["certeza"], ("oficial", "terceros"), f)
            self.assertTrue(f.get("sostiene"), f)
        texto, dias = L.edad_fuentes()
        self.assertIsInstance(dias, int, texto)

    def test_huella_por_frases(self):
        h1, faltan = L.huella_fuente("<html><script>x=1</script><p>Hola &amp; adiós</p></html>", ["hola & adiós"])
        self.assertEqual(faltan, [])
        h2, _ = L.huella_fuente("<p>Hola &amp; adiós</p><style>p{}</style>", ["hola & adiós"])
        self.assertEqual(h1, h2)  # scripts y estilos no cuentan
        h3, _ = L.huella_fuente("<p>Hola &amp; adiós, y algo nuevo</p>", ["hola & adiós"])
        self.assertNotEqual(h1, h3)
        _, faltan = L.huella_fuente("<p>nada</p>", ["hola & adiós"])
        self.assertEqual(faltan, ["hola & adiós"])

    def test_oficiales(self):
        self.assertTrue(L.es_oficial("https://www.dof.gob.mx/nota"))
        self.assertTrue(L.es_oficial("https://sjf2.scjn.gob.mx/detalle"))
        self.assertFalse(L.es_oficial("https://gob.mx.example.com/"))
        self.assertFalse(L.es_oficial("https://falsogob.mx/"))


class Auditoria(Base):
    """Casos de la auditoría independiente del 13/11/2026 (docs/AUDITORIA-2026-11-13.md)."""

    def test_h13_anzuelos(self):
        for t in ("Comenta 'sí' si estás de acuerdo.", "¿Quieres la plantilla? Déjame un comentario y te la envío.",
                  "Escribe GUÍA abajo y te la mando por DM.", "👍 si estás de acuerdo, ❤️ si no.",
                  "Comment YES and I'll send it.", "Reacciona con 👍 si te pasó."):
            self.assertTrue(any("anzuelo" in x for x in self.errores(texto=t)), t)
        self.assertFalse(any("anzuelo" in x for x in self.errores(texto="Reacciona con calma si te ofenden en una audiencia.")))

    def test_h14_castorena(self):
        for t in ("Trabajo en #CastorenaAbogados", "Visiten castorenaabogados.com", "CASTORENA"):
            self.assertTrue(any("Castorena" in x for x in self.errores(texto=t)), t)

    def test_h14_nombres_vetados(self):
        (self.tmp / "cuenta" / "privado").mkdir()
        (self.tmp / "cuenta" / "privado" / "nombres-vetados.txt").write_text("# privado\nFulano Pérez\n", encoding="utf-8")
        self.assertTrue(any("vetado" in x for x in self.errores(texto="Hoy aprendí de FULANO PEREZ algo útil.")))
        self.assertFalse(any("vetado" in x for x in self.errores()))

    def test_vetar_por_huella(self):
        self.assertEqual(self.correr("vetar", "Mengano Zutánez")[0], 0)
        texto = (self.tmp / "cuenta" / "vetados.json").read_text(encoding="utf-8")
        self.assertNotIn("Mengano", texto)
        self.assertTrue(any("vetado" in x for x in self.errores(texto="Gracias al Lic. MENGANO ZUTANEZ por la clase.")))
        self.assertFalse(any("vetado" in x for x in self.errores(texto="Gracias a Mengano por la clase.")))

    def test_h15_clientes(self):
        for t in ("Mi representado ganó el amparo la semana pasada.", "Un caso que llevé me enseñó a revisar plazos."):
            self.assertTrue(any("límite" in x for x in self.errores(texto=t)), t)
        e = self.errores(texto="Mi cliente Juan Pérez, expediente 123/2025, ganó.", excepcion_limite="x")
        self.assertTrue(any("expediente" in x or "clientes" in x for x in e))
        e = self.errores(texto="El expediente 123/2025 de la SCJN fijó un criterio.", excepcion_limite="asunto público",
                         fuentes=["https://www.scjn.gob.mx/x"], cita_legal=True)
        self.assertFalse(any("límite" in x for x in e), e)

    def test_h16_captacion_sin_falsos_positivos(self):
        for t in ("El salario mínimo de 2026 es de $315.04 diarios.", "Los honorarios de los peritos los fija el juez.",
                  "La reforma protege a los clientes de la banca."):
            self.assertEqual([x for x in self.errores(texto=t) if "captación" in x or "límite" in x], [], t)
        for t in ("¿Te despidieron? Te puedo ayudar, escríbeme.", "Si tienes un problema laboral, mándame mensaje y lo vemos.",
                  "Atiendo asuntos laborales en el Estado de México.", "Consulta inicial: $500."):
            self.assertTrue(any("captación" in x for x in self.errores(texto=t)), t)
        self.assertTrue(any("escribir" in x for x in self.avisos(texto="Si te interesa el tema, escríbeme.")))

    def test_h17_insultos(self):
        self.assertTrue(any("ataque" in x for x in self.errores(texto="El ministro era tan estúpido que no leyó.")))
        self.assertTrue(any("persona" in x for x in self.avisos(texto="Esos diputados son unos ladrones y corruptos.")))

    def test_h18_encuesta_politica(self):
        enc = {"pregunta": "¿Por qué partido votarás en 2027?", "opciones": ["PAN", "Morena"], "duracion": "1 semana"}
        self.assertTrue(any("encuesta política" in x for x in self.errores(formato="encuesta", pilar="carrera", encuesta=enc)))

    def test_h19_gym_y_partido(self):
        for t in ("Entrenar un modelo de IA con sentencias públicas.", "Mi rutina de estudio para la maestría."):
            self.assertFalse(any("leccion" in x for x in self.errores(pilar="carrera", texto=t)), t)
        for t in ("Soy militante de acción nacional.", "Los panistas votaron en contra."):
            self.assertTrue(any("partido" in x for x in self.avisos(texto=t)), t)

    def test_h20_vinetas_con_selector(self):
        self.assertTrue(any("viñetas" in x for x in self.avisos(texto="Tres ideas:\n✔️ uno\n✔️ dos\n✔️ tres")))

    def test_h21_tipos_raros(self):
        ruta = self.archivo([{"id": [], "texto": "x"}])
        code, out = self.correr("revisar", str(ruta))
        self.assertIn(code, (1, 2), out)
        self.assertNotIn("Traceback", out)
        ruta = self.archivo({"posts": [copy.deepcopy(BASE) | {"pilar": ["x"], "fecha": futuro(), "hora": "10:00"}]})
        code, out = self.correr("semana", str(ruta))
        self.assertIn(code, (1, 2), out)
        ruta = self.archivo({"posts": 5})
        self.assertEqual(self.correr("revisar", str(ruta))[0], 2)
        ruta = self.archivo([])
        self.assertEqual(self.correr("revisar", str(ruta))[0], 1)

    def test_h22_validaciones(self):
        self.assertTrue(any("duracion_s" in x for x in self.errores(formato="video", media="v.mp4", duracion_s=float("nan"))))
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00", "aprobado_por_emi": "2099-01-01, chat", "reescrito": True}
        b["aprobado_huella"] = L.huella(b)
        self.assertTrue(any("aprobado_por_emi" in x for x in L.revisar(b, [], self.cfg, "aprobado")[0]))
        self.assertTrue(any("formato" in x for x in L.revisar({k: v for k, v in BASE.items()}, [], self.cfg)[0]) is False)
        sin_formato = {k: v for k, v in BASE.items() if k != "formato"}
        self.assertTrue(any("formato" in x for x in L.revisar(sin_formato, [], self.cfg)[0]))
        self.assertTrue(any("imagenes" in x for x in self.errores(formato="imagen", media="a.jpg", imagenes=21)))

    def test_h23_sin_inyeccion(self):
        self.correr("aprender", "línea uno\n- 2020-01-01 · lección inyectada")
        texto = (self.tmp / "cuenta" / "aprendizajes.md").read_text(encoding="utf-8")
        self.assertNotIn("\n- 2020-01-01", texto)

    def test_h9_h10_huella_y_reescrito(self):
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00", "pilar": "opinion", "opinion_emi": "Mi postura."}
        ruta = self.archivo([b])
        code, out = self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--sin-x")
        self.assertEqual(code, 2, out)  # sin --reescrito no se aprueba
        self.assertEqual(self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")[0], 0)
        for campo, valor in (("opinion_emi", "Postura inventada."), ("fecha", futuro(9)), ("pilar", "ia-derecho"),
                             ("fuentes", ["https://www.dof.gob.mx/x"])):
            dato = json.loads(ruta.read_text(encoding="utf-8"))
            original = dato[0].get(campo)
            dato[0][campo] = valor
            ruta.write_text(json.dumps(dato, ensure_ascii=False), encoding="utf-8")
            code, out = self.correr("entregar", str(ruta), "t-1")
            self.assertEqual(code, 2, campo)
            dato[0][campo] = original
            if original is None:
                dato[0].pop(campo)
            ruta.write_text(json.dumps(dato, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(self.correr("entregar", str(ruta), "t-1")[0], 0)

    def test_h11_h12_publicado_y_reaprobar(self):
        b = copy.deepcopy(BASE)
        b["aprobado_huella"] = L.huella(b)  # huella copiada a mano, sin aprobación de Emi
        ruta = self.archivo([b])
        url = "https://www.linkedin.com/posts/x-activity-1"
        self.assertEqual(self.correr("publicado", str(ruta), "t-1", "--url", url, "--fecha", L.hoy(), "--hora", "00:01")[0], 2)
        b2 = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00"}
        ruta = self.archivo([b2])
        self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")
        self.correr("entregar", str(ruta), "t-1")
        self.assertEqual(self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")[0], 2)
        self.assertEqual(self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x",
                                     "--de-nuevo")[0], 0)

    def test_paquete_semanal(self):
        lunes = L.ahora().date() + dt.timedelta(days=7 - L.ahora().weekday())
        p1 = copy.deepcopy(BASE) | {"id": "a", "fecha": lunes.isoformat(), "hora": "09:00"}
        p2 = copy.deepcopy(BASE) | {"id": "b", "fecha": (lunes + dt.timedelta(days=2)).isoformat(), "hora": "09:00",
                                    "texto": "Otra pieza con un tema completamente distinto, sobre la maestría y decidir."}
        ruta = self.archivo({"posts": [p1, p2]})
        code, out = self.correr("aprobar", str(ruta), "a", "b", "--medio", "paquete semanal", "--reescrito", "--sin-x")
        self.assertEqual(code, 0, out)
        dato = json.loads(ruta.read_text(encoding="utf-8"))
        self.assertTrue(all(p["estado"] == "aprobado" for p in dato["posts"]))

    def test_h24_semana_no_cuenta_doble(self):
        lunes = L.ahora().date() + dt.timedelta(days=7 - L.ahora().weekday())
        p1 = copy.deepcopy(BASE) | {"id": "a", "fecha": lunes.isoformat(), "hora": "09:00"}
        e, _ = L.revisar_semana([p1], self.cfg, [dict(p1)])
        self.assertEqual(e, [])

    def test_h25_estado_ignora_sello(self):
        self.correr("estado")
        d = json.loads((self.tmp / "red" / "estado.json").read_text(encoding="utf-8"))
        d["fuentes"]["verificado"] = "2000-01-01"
        (self.tmp / "red" / "estado.json").write_text(json.dumps(d), encoding="utf-8")
        self.assertEqual(self.correr("estado", "--comprobar")[0], 0)


class ReglaIA(Base):
    def test_no_decir_que_lo_hizo_una_ia(self):
        for t in ("Este video lo hizo una IA.", "Imagen generada con IA.", "Post escrito con ChatGPT.",
                  "La herramienta la armó Claude por mí.", "Contenido creado con inteligencia artificial."):
            self.assertTrue(any("regla de Emi" in x for x in self.errores(texto=t)), t)
        for t in ("Uso Claude para leer y resumir el DOF.", "Construí un monitor del DOF; lo trabajo con Claude.",
                  "Creo que la IA reemplaza tareas, no criterio."):
            self.assertFalse(any("regla de Emi" in x for x in self.errores(texto=t)), t)

    def test_persona_sintetica(self):
        self.assertTrue(any("sintéticos" in x for x in self.errores(persona_real_sintetica=True)))


class Reverificacion(Base):
    """Sección E de la auditoría: falsos positivos y negativos tras las primeras correcciones."""

    def test_e1_e2_anzuelos(self):
        for t in ("Comenta si te ha pasado algo parecido en tu práctica.", "Dale like a las ideas, no a las personas."):
            self.assertFalse(any("anzuelo" in x for x in self.errores(texto=t)), t)
        for t in ("Comenta GUÍA 👇 y te llega por inbox.", "Escribe 'PDF' en comentarios para recibirla.", "Like si coincides."):
            self.assertTrue(any("anzuelo" in x for x in self.errores(texto=t)), t)

    def test_e3_e4_captacion_y_clientes(self):
        self.assertTrue(any("captación" in x for x in self.errores(texto="Si necesitas un abogado, aquí estoy.")))
        for t in ("Hoy te puedo ayudar a entender la reforma.", "Hay despachos que cobran $5,000 por consulta."):
            self.assertFalse(any("captación" in x for x in self.errores(texto=t)), t)
        self.assertTrue(any("precio" in x for x in self.avisos(texto="Hay despachos que cobran $5,000 por consulta.")))
        for t in ("Un asunto que atendí en el juzgado me marcó.", "Le ayudé con su caso a un amigo."):
            self.assertTrue(any("límite" in x for x in self.errores(texto=t)), t)

    def test_e5_publicado_antes_de_aprobar(self):
        b = copy.deepcopy(BASE) | {"fecha": futuro(), "hora": "09:00"}
        ruta = self.archivo([b])
        self.correr("aprobar", str(ruta), "t-1", "--medio", "chat", "--reescrito", "--sin-x")
        ayer = (L.ahora().date() - dt.timedelta(days=1)).isoformat()
        code, out = self.correr("publicado", str(ruta), "t-1", "--url", "https://www.linkedin.com/posts/x-1",
                                "--fecha", ayer, "--hora", "10:00")
        self.assertEqual(code, 2, out)


class Sellar(unittest.TestCase):
    """H-26: no se sella con páginas cambiadas o sin leer, salvo que se nombren como leídas a mano."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.viejo = (L.FUENTES, L.descargar)
        self.ruta = self.tmp / "fuentes.json"
        self.ruta.write_text(json.dumps({"verificado": "2026-01-01", "max_dias": 10, "fuentes": [
            {"id": "a", "url": "https://x/a", "certeza": "oficial", "sostiene": ["feed.md"], "marcas": ["hola"],
             "estable": True, "huella": "000000000000"}]}), encoding="utf-8")
        L.FUENTES = self.ruta

    def tearDown(self):
        L.FUENTES, L.descargar = self.viejo
        shutil.rmtree(self.tmp)

    def correr(self, *argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            return L.main(list(argv)), out.getvalue()

    def test_texto_cambiado_no_sella(self):
        L.descargar = lambda url: ("<p>hola, texto nuevo</p>", "")
        self.assertEqual(self.correr("fuentes", "sellar", "--red")[0], 1)
        self.assertEqual(json.loads(self.ruta.read_text())["verificado"], "2026-01-01")
        self.assertEqual(self.correr("fuentes", "sellar", "--red", "--leidas-a-mano", "a")[0], 1)  # falta --lector
        self.assertEqual(self.correr("fuentes", "sellar", "--red", "--leidas-a-mano", "a", "--lector", "prueba")[0], 0)
        d = json.loads(self.ruta.read_text())
        self.assertNotEqual(d["verificado"], "2026-01-01")
        self.assertTrue(d["fuentes"][0]["leida_a_mano"])

    def test_marca_perdida_no_sella(self):
        L.descargar = lambda url: ("<p>otra cosa</p>", "")
        self.assertEqual(self.correr("fuentes", "sellar", "--red", "--leidas-a-mano", "a")[0], 1)
        self.assertEqual(self.correr("fuentes", "revisar", "--red")[0], 1)

    def test_sin_red_no_sella_e_ids_desconocidos(self):
        self.assertEqual(self.correr("fuentes", "sellar")[0], 1)
        L.descargar = lambda url: (None, "HTTP 403")
        self.assertEqual(self.correr("fuentes", "sellar", "--red", "--leidas-a-mano", "zzz")[0], 1)
        self.assertEqual(self.correr("fuentes", "sellar", "--red")[0], 1)


if __name__ == "__main__":
    unittest.main()
