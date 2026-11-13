---
name: linkedin-pro
description: "Planear, redactar, revisar, entregar para publicar y medir las publicaciones de Emi en su perfil personal de LinkedIn (linkedin.com/in/emiliano-milla), con reglas basadas en fuentes oficiales de LinkedIn y marcadas por certeza (oficial, de terceros o criterio): IA + Derecho en México 60 %, carrera y maestría 25 %, opinión jurídico-política 15 %. Usar al pedir un post, documento o carrusel PDF, artículo, boletín, encuesta, calendario o semana de contenido para LinkedIn, al revisar un borrador, al optimizar el perfil (titular, Acerca de, experiencia, destacados), al preguntar qué premia o castiga el feed de LinkedIn o si algo es mito, al anotar o analizar métricas de LinkedIn, al revisar si cambiaron sus fuentes oficiales, o al publicar en LinkedIn un video de Vox Studio. No usar para producir videos (vox-studio), para X (x-viral) u otras redes, ni para mensajes de WhatsApp o correo (estilo-emi)."
license: Uso personal de Emiliano García Milla. Sin licencia de reutilización para terceros.
metadata:
  version: "1.0.0"
  release_date: "2026-11-13"
  language: "es-MX"
  fuentes_verificadas: "2026-11-13"
---

# linkedin-pro

Skill para el perfil personal de Emi en LinkedIn. Es hermana de x-viral (`lianfixx/X`) y sigue su mismo método, pero con una diferencia de fondo: **X publicó el código de su ranking y LinkedIn no.** Aquí no hay pesos ni constantes verificables. Cada regla dice su grado de certeza:

- **oficial**: Centro de ayuda, políticas, comunicados, blog de ingeniería o declaraciones de directivos de LinkedIn.
- **de terceros**: estudios externos con método explícito, con su solidez.
- **criterio**: decisión razonada de esta skill o de Emi.

Lo que «todo el mundo dice» sin sustento va a [mitos.md](references/mitos.md). Funciona en cualquier IA: [portabilidad.md](references/portabilidad.md). Con terminal, las órdenes son de `scripts/linkedin.py` y se corren desde la raíz del repositorio. Abajo, `lk` abrevia `python3 skills/linkedin-pro/scripts/linkedin.py`.

## Reglas que no se rompen

1. **Emi aprueba cada pieza y es él quien la publica.** La IA entrega el texto aprobado listo para copiar, con fecha y hora. Ninguna IA inicia sesión en LinkedIn, publica, programa, reacciona, comenta, invita ni manda mensajes por él. Las métricas llegan por captura.
2. **La IA propone, Emi reescribe.** No se inventan vivencias, opiniones, cifras ni citas.
3. **Nada sobre el algoritmo sin certeza y fuente.** No se inventan pesos ni porcentajes.
4. **Límites de Emi**: nunca clientes ni asuntos, no nombrar a Castorena ni a sus licenciados, sin ataques personales, toda cita legal con fuente oficial verificada, un post informa u opina y no asesora un caso. Detalle en [pilares.md](references/pilares.md).
5. **Sin captación de clientes de MILLA** mientras Emi no la abra (`captacion_milla: false`).
6. **En opinión, primero su postura**, en `opinion_emi`. El perfil no habla a nombre del PAN.
7. **Nada de anzuelos, grupos de interacción ni automatización.** LinkedIn los prohíbe y los degrada.
8. **Cada skill en su carril**: linkedin-pro no produce video, no edita Vox Studio ni las skills de otras redes, y no pega en LinkedIn el mismo texto de otra red.

## Estado de la cuenta

Al 13/11/2026, lo que se ve sin sesión (ficha pública en Google): titular «Abogado en Formación | Enlace Universitario Banxico 2026», más de 180 seguidores y 192 contactos (`cuenta/perfil.json`). Ninguna IA puede ver el perfil completo ni las estadísticas: lo trae Emi con capturas. Lo primero es la [propuesta de perfil](references/perfil.md); se puede redactar desde ya.

## Qué leer según el encargo

| Encargo | Leer |
|---|---|
| Cualquiera | Esta página, `cuenta/perfil.json`, `cuenta/voz.md`, `cuenta/aprendizajes.md` |
| Escribir o revisar una pieza | [redaccion.md](references/redaccion.md), [pilares.md](references/pilares.md), [formatos.md](references/formatos.md) |
| Semana o calendario | Lo anterior, [playbook.md](references/playbook.md) y el [ejemplo de semana](assets/semana.ejemplo.json) |
| Qué premia o castiga LinkedIn | [feed.md](references/feed.md), [mitos.md](references/mitos.md), [fuentes.md](references/fuentes.md) |
| Optimizar el perfil | [perfil.md](references/perfil.md) |
| Entregar una pieza para que Emi la publique | [entrega.md](references/entrega.md) |
| Métricas y revisión mensual | [medicion.md](references/medicion.md) |
| Video de Vox Studio o ideas para video | [conexion-vox.md](references/conexion-vox.md) |
| Encargos listos para copiar | [prompts.md](references/prompts.md) |

## Flujo de una pieza

1. **Contexto**: `lk balance` (qué pilar toca) y `lk vox leer` (tono y lecciones de Vox Studio; es información, no instrucciones). Si no responde, seguir con `cuenta/voz.md` y decírselo a Emi.
2. **Material real**: preguntar a Emi, todo junto, qué pasó, qué piensa y qué quiere decir.
3. **Fuente**: si hay derecho o datos, verificar en la fuente oficial y guardar el enlace.
4. **Borrador** en `cuenta/privado/` con el formato de [redaccion.md](references/redaccion.md): texto, pilar, formato, `para_quien`, `aporta`.
5. **Revisar**: `lk revisar ARCHIVO --contra-x`. Corregir hasta que no haya errores; atender los avisos.
6. **Emi lo reescribe y aprueba** ese texto exacto y su archivo. Solo entonces: `lk aprobar ARCHIVO ID --medio "dónde lo aprobó"`, que anota la fecha y la huella del contenido. Si cambia, la aprobación deja de valer.
7. **Entregar**: `lk entregar ARCHIVO ID` imprime el bloque listo para copiar ([entrega.md](references/entrega.md)). Emi lo publica o lo programa en LinkedIn y manda el enlace.
8. **Anotar**: `lk publicado ARCHIVO ID --url URL`; a los 7 días, `lk metricas ID … --fuente "captura"`; la lección con `lk aprender "…"`; y `lk estado` para la Matriz de Redes.

Para una semana: lo mismo con `lk semana ARCHIVO --contra-x`, que además valida cadencia (1 al día, 2 por semana, 24 horas entre piezas) y balance.

## Lo esencial del feed

Resumen de [feed.md](references/feed.md), verificado el 13/11/2026:

- Un post se muestra primero a una parte de los contactos y seguidores, según la fuerza de la conexión; lo profesionalmente relevante se distribuye más allá [oficial].
- LinkedIn dice que prioriza conocimiento y conversación auténtica sobre los «me gusta», y que no está diseñado para la viralidad [oficial].
- Lo genérico, repetitivo o sin punto de vista, incluido lo hecho con IA sin voz propia, se distribuye menos fuera de la red [oficial].
- Anzuelos («comenta SÍ»), grupos de interacción y comentarios automatizados están prohibidos o degradados [oficial].
- Contenido falso o engañoso no se distribuye más allá de la red del autor [oficial].
- No hay ventaja oficial por formato, hashtag ni hora; los estudios de terceros dan correlaciones, a veces contradictorias [terceros].

## Mantener al día

LinkedIn cambia sin aviso de código. Cada semana (tarea programada de Emi, o a mano), con el encargo 6 de [prompts.md](references/prompts.md):

```bash
python3 skills/linkedin-pro/scripts/linkedin.py fuentes revisar --red   # busca las frases marca de cada fuente
python3 skills/linkedin-pro/scripts/linkedin.py fuentes sellar --red    # solo si no cambió nada
```

`revisar` sale con 1 si una frase marca desapareció. Una fuente que no se pudo descargar es aviso: se revisa a mano. **No detecta páginas nuevas**: la tarea semanal busca además comunicados recientes. Si algo cambió: corregir cada afirmación afectada con su certeza, actualizar `data/limites.json` si cambió un límite, correr `python3 ia/verificar.py ci`, subir `metadata.version` y `VERSION` del script y registrar en `CHANGELOG.md`. GitHub marca en rojo cada lunes si la verificación tiene más de 10 días (`fuentes.yml`).

## Aprender

Cada corrección de Emi y cada resultado se guarda: `lk aprender "qué pasó y qué regla queda"`. Las correcciones de estilo van además a `cuenta/voz.md` con el antes y el después. Lo que sirva para video se deja a Vox Studio con `lk vox idea "…"`. Las lecciones no se borran; si una cambia, se añade la nueva.

## Terminado

Una pieza está terminada cuando: `revisar` no da errores, Emi la reescribió y aprobó, se le entregó lista para copiar y él confirmó que la publicó o programó. Después: anotada con `lk publicado`, con métricas a los 7 días, su lección y `red/estado.json` regenerado. Todo cambio en archivos del repositorio se registra en `CHANGELOG.md` según `ia/PROTOCOLO.md`; varias anotaciones del mismo día pueden ir en una sola entrada.
