# Cómo se escribe y se revisa una pieza

## Voz

Tono elegido por Emi para LinkedIn (13/11/2026): **profesional y cercano, con algo de humor**. Las correcciones de Emi mandan sobre todo lo demás y se guardan en `cuenta/voz.md` con el antes y el después.

- Primera persona, español de México, frases cortas. Habla de tú a su lector, con respeto de colega.
- Una idea por pieza. La primera línea ya dice algo concreto: una tesis, un dato con fuente o una escena real. Nada de «hoy quiero compartirles».
- El humor es un guiño, no el gancho: una línea, sin burlarse de personas, nunca a costa del dato. En opinión, con medida; en temas jurídicos delicados, ninguno.
- Postura clara. Si hay duda honesta, se dice como duda.
- Experiencia propia por encima de consejos genéricos. LinkedIn dice que lo genérico, repetitivo o sin punto de vista se distribuye menos (Centro de ayuda, a1481496).
- **Nunca decir que una pieza o una herramienta la hizo, armó o editó una IA** (regla absoluta de Emi, 13/11/2026). Las herramientas las construyó él; sí se nombra la IA que usa («uso Claude para…»). `linkedin.py` lo marca como error.
- Sin «me complace anunciar», «apasionado por», «sinergia», rayas largas, listas de emojis ni hashtags de relleno.

## Estructura de un post de texto (punto de partida, no fórmula)

1. **Primera línea** (menos de 140 caracteres, porque LinkedIn corta el post con «…más»): la idea.
2. **Desarrollo**: el porqué, con un ejemplo real o un dato con fuente. Párrafos de una a tres líneas.
3. **Cierre**: lo que el lector se lleva, o una pregunta genuina de su campo. Nunca «comenta SÍ».

## Formato del borrador

Un JSON por pieza (o una semana con `"posts": [...]`) en `cuenta/privado/`, que no se sube a GitHub. Ejemplo completo y válido: [assets/semana.ejemplo.json](../assets/semana.ejemplo.json).

| Campo | Obligatorio | Qué es |
|---|---|---|
| `id` | sí | Por ejemplo `2026-W47-a`. |
| `pilar` | sí | `ia-derecho`, `carrera` u `opinion`. |
| `formato` | sí | `texto`, `imagen`, `documento`, `video`, `articulo`, `boletin` o `encuesta`. |
| `texto` | sí | El texto exacto del post (en artículo o boletín, el que acompaña al compartir). |
| `para_quien` | sí | Qué lector profesional lo necesita. |
| `aporta` | sí | Qué se lleva ese lector: conocimiento, experiencia u opinión fundada. |
| `fecha`, `hora` | para aprobar | AAAA-MM-DD y HH:MM, hora del centro de México. |
| `titulo` | documento, artículo, boletín | Título. |
| `cuerpo` | artículo, boletín | Texto completo. |
| `paginas`, `media` | documento | Páginas del PDF y archivo propio. |
| `duracion_s`, `media`, `subtitulos` | video | Segundos, archivo y si lleva subtítulos (`true`). |
| `encuesta` | encuesta | `{pregunta, opciones (2 a 4), duracion}`. |
| `opinion_emi` | pilar opinión | La postura de Emi con sus palabras. |
| `leccion_profesional` | si habla de gym o estilo de vida | La lección profesional que justifica el tema. |
| `cita_legal`, `fuentes` | si afirma derecho | `true` y enlaces directos a la fuente oficial. |
| `excepcion_limite` | solo si aplica | Por qué un ejemplo hipotético o un asunto público no rompe el límite de clientes. |
| `persona_real_sintetica` | si aplica | `true` si una imagen, voz o video muestra a una persona real diciendo o haciendo algo que no hizo. Es error: no se publica (Políticas de la Comunidad Profesional). |
| `idea_matriz` | opcional | Id de la idea en la Matriz de Redes, si viene de ahí. |
| `imagenes` | imagen | Cuántas imágenes lleva el post (máximo 20). |
| `estado`, `aprobado_por_emi`, `aprobado_huella`, `reescrito`, `entregado`, `publicado_url` | los ponen `aprobar`, `entregar` y `publicado` | No se escriben a mano. Todos los demás campos entran en la huella de aprobación. |

## Revisión

```bash
python3 skills/linkedin-pro/scripts/linkedin.py revisar cuenta/privado/2026-W47.json --contra-x
python3 skills/linkedin-pro/scripts/linkedin.py semana  cuenta/privado/2026-W47.json --contra-x
```

**Errores** (no pasa): anzuelos de interacción, captación de clientes, Castorena (también en hashtag o dominio) y los nombres vetados (`linkedin.py vetar "Nombre"` guarda solo su huella en `cuenta/vetados.json`; también vale la lista local `cuenta/privado/nombres-vetados.txt`), clientes o asuntos (los números de expediente y nombres de clientes no se salvan ni con excepción, salvo asunto público con fuente oficial), encuestas que pregunten por partidos o votos, insultos, cita legal sin fuente, falta de `para_quien` o `aporta`, opinión sin postura de Emi, gym sin lección en el pilar carrera, encuesta en el pilar opinión, límites técnicos del formato, texto casi idéntico a uno ya publicado (también en X), cadencia (más de 1 al día, de 2 por semana o menos de 24 horas entre piezas), aprobación que no corresponde al texto.

**Avisos** (se atienden o se explican): «escríbeme» (confirmar que es para conversar, no para atender casos), «los clientes» de terceros, insultos leves (ladrones, corruptos…), primera línea larga, frases de plantilla, raya larga, más de 3 hashtags, más de 5 menciones, mención de MILLA o del partido, «en tu caso debes…», texto que parece citar derecho sin `cita_legal`, fuente que no es de un dominio oficial conocido, video sin subtítulos, desbalance de pilares.

`linkedin.py` no juzga la calidad de la idea ni la verdad de lo que se afirma: eso lo hacen la IA que redacta, verificando, y Emi.

## Sin terminal

En ChatGPT, Gemini o claude.ai sin terminal se aplica a mano la lista de errores y avisos de arriba, se le muestra a Emi y se le dice que la revisión fue manual.
