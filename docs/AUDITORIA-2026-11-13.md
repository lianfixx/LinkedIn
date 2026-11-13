# Auditoría del 13/11/2026

Qué se revisó antes de publicar linkedin-pro 1.0.0, cómo se revisó y qué se corrigió.

## 1. Investigación

Tres agentes trabajaron en paralelo con fuentes primarias, leídas el 13/11/2026:

- **Feed y transparencia.** Centro de ayuda, Políticas de la Comunidad Profesional, Acuerdo de usuario, comunicados de 2026, blog de ingeniería, declaraciones de directivos e informes DSA.
- **Formatos, analítica, perfil, IA y automatización.** Centro de ayuda en inglés, con contraste en español.
- **Estudios de terceros y mitos.** Nueve estudios de proveedores y cuatro académicos, cada uno con su método y su solidez.

Luego, el agente principal descargó desde esta sesión cada página oficial citada y comprobó sus frases marca. Hoy son 54 fuentes en `skills/linkedin-pro/data/fuentes.json`.

## 2. Revisión independiente

Un agente sin contexto previo recibió el repositorio, no las conclusiones, con el encargo de tumbar lo que pudiera. Revisó los commits `6807106` y `7cfedb4`. Hizo tres cosas:

- Cotejó más de 60 afirmaciones contra la página original.
- Corrió el script con entradas límite en copias.
- Revisó enlaces, workflows, privacidad y reglas.

Encontró 37 hallazgos (9 altos, 17 medios y 11 bajos) y confirmó 36 afirmaciones como literales. Todas las correcciones van en la entrada «correcciones de la auditoría» de `CHANGELOG.md` y quedaron cubiertas por pruebas en `test_linkedin.py`, clases `Auditoria` y `Sellar`.

| # | Hallazgo | Corrección |
|---|---|---|
| H-1 | El 40 % de vistas menos se atribuía a Jurka. | Ahora es de Srinivasan (agosto de 2026, citado por Fortune) y se aclara que solo mide lo ya clasificado. El 94 % queda con Jurka. |
| H-2 | Se citaba mal a Buffer («cada post extra rinde menos»). | Corregido: publicar más sube el alcance por post. |
| H-3 | Cifras de Metricool y Van der Blom que no están en su fuente. | Quitadas o sustituidas por las que sí están (−60 % de Van der Blom; −6.6 % en perfiles según AuthoredUp). |
| H-4 | «El boletín avisa a suscriptores» iba como [oficial] sin fuente. | Bajado a [criterio]. |
| H-5 | Dos citas «de LinkedIn 2023» sin fuente. | Eliminadas. |
| H-6 | La ausencia de ventaja por formato llevaba tres certezas distintas. | Unificada como [criterio]. |
| H-7, H-8 | Métrica principal, cargo de Jobanputra y dwell time de 2020. | Separado lo oficial de lo propio; cargo sin afirmar; dwell time con fecha y matiz. |
| H-9 | La huella no cubría la postura, el pilar, la fecha, las fuentes… | Ahora cubre toda la pieza menos los campos de estado. |
| H-10 | `aprobar` ponía `reescrito` solo. | Exige `--reescrito` explícito. La huella se documenta como compuerta de honor. |
| H-11, H-12 | `publicado` aceptaba piezas no aprobadas, fechas futuras y cualquier URL; se podía volver a aprobar algo publicado. | Ahora corre la revisión completa, exige estado aprobado o entregado, fecha pasada y enlace de post. No reaprueba lo publicado y lo entregado solo con `--de-nuevo`. |
| H-13 | Anzuelos que no detectaba, incluido el ejemplo de LinkedIn. | Patrones nuevos para «comenta X si…», «déjame un comentario y te…», votos con emoji y la versión en inglés. Se quitó el falso positivo «reacciona con calma». |
| H-14 | Castorena se colaba en hashtag o dominio; no se revisaban sus licenciados. | Búsqueda sobre el texto aplanado, sin límite de palabra. Lista privada `cuenta/privado/nombres-vetados.txt`. |
| H-15 | «Mi representado», «un caso que llevé»; cualquier excepción lo salvaba todo. | Patrones nuevos. Los números de expediente y los nombres de clientes siguen siendo error salvo asunto público con fuente oficial. |
| H-16 | Falsos positivos de captación (salario mínimo, honorarios de peritos, clientes de la banca) y falsos negativos (te puedo ayudar, mándame mensaje y lo vemos). | Captación por contexto; los clientes de terceros pasan a aviso; «escríbeme» es aviso. |
| H-17 a H-20 | Insultos en tercera persona, encuestas políticas en cualquier pilar, «entrenar un modelo» confundido con gym, partido en minúsculas, viñetas con selector de emoji. | Corregidos. |
| H-21, H-22 | Crashes con tipos raros; NaN; fechas futuras o inválidas en métricas y aprobación; lista vacía. | Validados; cualquier dato con forma inesperada sale con mensaje y código 2. |
| H-23 | Un salto de línea en una lección fabricaba otra entrada fechada. | Las lecciones y las ideas se guardan en una línea. |
| H-24 | La semana contaba dos veces lo ya publicado. | Corregido. |
| H-25 | El sello semanal rompía el control. | `--comprobar` ignora la fecha del sello y el sello sube también `red/estado.json`. |
| H-26 | `sellar` aceptaba páginas cambiadas o sin leer. | No sella con páginas cambiadas o sin leer salvo `--leidas-a-mano` con ids válidos, y queda registrado. |
| H-27 | 12 páginas citadas no se vigilaban. | Añadidas con frases marca. |
| H-28 | GitHub descargaba linkedin.com cada lunes (tensión con el Acuerdo §8.2). | GitHub ya no descarga nada. La lectura semanal de páginas públicas queda pendiente de que Emi la confirme. |
| H-29 | Dos zonas horarias distintas. | Las dos usan la fecha del centro de México, con un día de margen. |
| H-30, H-31 | Este archivo no existía; el control de enlaces y el de certeza prometían más de lo que hacían. | Creado este archivo; el control revisa los enlaces de todos los `.md`; se precisó qué cubre el control de certeza. |
| H-32 | Documentación contra código. | `formato` obligatorio, `imagenes` validado, fuente del feed vertical corregida. |
| H-33 | Privacidad. | Sin nombres de terceros en diagnósticos; fuera el juicio sobre una persona; menos detalle de infraestructura. Publicar métricas queda pendiente de que Emi lo confirme. |
| H-34 | Python 3.9 sin soporte en GitHub. | GitHub prueba 3.10 y 3.12; 3.9 se probó en local. |
| H-35 | La comparación con X era opcional. | `aprobar` compara con X y avisa si no responde. |
| H-36 | Dos artículos Pulse dan 403 al auditor. | Esta sesión sí los leyó y encontró sus frases marca; queda la nota en `fuentes.json`. |
| H-37 | La conclusión sobre los informes DSA iba como [oficial]. | Ahora va como [oficial] [criterio]. |

## 3. Control final

| Control | Resultado |
|---|---|
| `python3 -m unittest discover -s skills/linkedin-pro/scripts -p 'test_*.py'` | Aprobado: 65 pruebas, con Python 3.13 y 3.9. |
| `python3 ia/verificar.py ci` | Aprobado, con Python 3.13 y 3.9. |
| `linkedin.py fuentes revisar --red` | Sin cambios: las 54 fuentes con sus frases marca. |
| Workflows de GitHub | Ver la entrada de `CHANGELOG.md` del primer push. |

## 4. Lo que no se pudo probar

- **El perfil real.** LinkedIn pide sesión. Solo se vio la ficha pública que muestra Google.
- **Publicaciones y métricas.** Todavía no hay ninguna pieza publicada ni corregida por Emi. La voz es candidata.
- **El efecto de cada regla.** LinkedIn no publica pesos. Las reglas siguen lo que la empresa dice y lo que miden terceros; se ajustan con las métricas de Emi.
- **La tarea semanal.** Se crea cuando exista el repositorio. Su primera ejecución está por verse.
- **Informes DSA de 2026, informe de auditoría DSA y papers de arXiv del feed.** Localizados, no leídos.
- **Si Vox Studio lee el puente.** La petición está preparada, no enviada.
