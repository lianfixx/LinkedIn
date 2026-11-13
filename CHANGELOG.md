# Registro de cambios

Lo más reciente arriba. Formato en `ia/PROTOCOLO.md`, sección 3.

## 2026-11-13 · Claude publica con el sí final de Emi; petición a Vox enviada
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 13/11/2026, en el chat de Claude Code: «que lo publique Claude (con previa confirmación final mía)»; «no muevas nada» del titular, «Acerca de» y experiencia; destacados: «no sé si quitarla»; petición a Vox Studio: «Sí, autorizo ahora mismo».
- Cambios: (1) Modo de entrega: Claude publica o programa a mano desde box solo tras el sí final de Emi al bloque de `entregar` de esa pieza (`entrega.md`, `SKILL.md`, `ia/REGLAS.md`, `AGENTS.md`, `CLAUDE.md`, `cuenta/perfil.json`). (2) El perfil no se toca. (3) `puente/PETICION-vox.md` enviada a la sesión que mantiene Vox Studio.
- Archivos: los citados, `puente/README.md`, `red/estado.json` y este registro.
- Verificación: `python3 ia/verificar.py ci` → aprobado.
- Pendiente: archivo MP4 del video del DOF para publicarlo; que Vox Studio aplique la petición.

## 2026-11-13 · Tarea semanal de revisión de fuentes
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi eligió el 13/11/2026 una revisión semanal de fuentes.
- Cambios: tarea programada en la cuenta de Claude de Emi, «LinkedIn · revisión semanal de fuentes», cada lunes a las 13:19 (centro de México), con aviso al teléfono; abre una sesión nueva que sigue el encargo 6 de `prompts.md`. Primera ejecución: 16/11/2026. Vive en la cuenta de Emi, no en este repositorio. README actualizado.
- Archivos: `README.md` y este registro.
- Verificación: tarea creada → aprobado; su primera ejecución → no probada todavía. Las sesiones que abre no llevan el repositorio conectado: si no pueden subir, dejan un «Registro pendiente».
- Pendiente: ver si la primera ejecución puede subir a `main`; si no, añadir `lianfixx/linkedin` al entorno de la tarea.

## 2026-11-13 · Publicación en GitHub
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 13/11/2026: el repositorio `lianfixx/LinkedIn` ya existe (creado por Emi con Muse, con un README inicial).
- Cambios: se integró la historia completa de linkedin-pro sobre el commit inicial del repositorio (el README inicial queda sustituido por el de la skill) y se subió a `main`.
- Archivos: todos los del repositorio.
- Verificación: `python3 ia/verificar.py ci` → aprobado antes del push; workflow «Control de la skill» en GitHub → aprobado (Python 3.10 y 3.12).
- Pendiente: ver la entrada de arriba.

## 2026-11-13 · Sesión de LinkedIn en box (solo lectura) y línea base del perfil
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 13/11/2026, en el chat de Claude Code: «Intenta sí o sí iniciar con box, hazlo»; abrió él mismo la sesión en box «main» («listo»). Sobre nombres vetados: «de nadie».
- Cambios: (1) La regla de no iniciar sesión cambia: la sesión de box sirve para leer perfil, posts y estadísticas a ritmo de persona; publicar, interactuar o editar requiere orden expresa; nunca se pide ni guarda la contraseña (`ia/REGLAS.md`, `SKILL.md`, `entrega.md`, `medicion.md`, `portabilidad.md`, `AGENTS.md`, `CLAUDE.md`, `ia/INSTRUCCIONES_PROYECTO.md`; en `CLAUDE.md`, leer con `browser_fetch` en box). (2) Perfil y analítica leídos: `cuenta/perfil.json` y `cuenta/diagnosticos/2026-11.md` con cifras agregadas (2,874 impresiones y 47 interacciones en 365 días). Sin nombres de terceros ni del despacho. (3) No hay nombres por vetar.
- Archivos: los citados, `red/estado.json` y este registro.
- Verificación: lectura del perfil, de la experiencia y de «Análisis de contenido» en box → hecha (la pestaña de experiencia se cerró por memoria del navegador; se leyó antes); `python3 ia/verificar.py ci` → aprobado.
- Pendiente: aclarar «Licenciado en Derecho» frente a «Pasante» antes del titular; decisión de Emi sobre sus destacados.

## 2026-11-13 · Decisiones de Emi, nombres vetados por huella y propuesta de titular
- Agente: Claude Code (sesión en la nube)
- Solicitud: Emi, 13/11/2026, en el chat de Claude Code: Muse crea el repositorio; sí a la lectura semanal de páginas públicas, al sello automático en `main` y a que sus métricas vayan en el repositorio público; preguntó si una IA puede entrar a su cuenta (box o API); no entendió lo de los nombres vetados; pidió la mejor propuesta de titular, natural y que no se le pueda criticar.
- Cambios: (1) Las tres autorizaciones quedan en `ia/REGLAS.md`, `SKILL.md`, `medicion.md` y `cuenta/perfil.json`. (2) `linkedin.py vetar "Nombre"` guarda solo la huella del nombre en `cuenta/vetados.json` y el revisor la busca en cada pieza (prueba nueva). (3) Propuesta de titular en `perfil.md` con tres opciones y la condición de tener título para decir «Abogado» (Código Penal Federal, art. 250, verificado en el texto vigente de la Cámara de Diputados). (4) Voz real observada en dos posts públicos suyos (`cuenta/voz.md`) y perfil observado: 212 seguidores y 20 posts.
- Archivos: `skills/linkedin-pro/scripts/{linkedin.py,test_linkedin.py}`, `skills/linkedin-pro/references/{perfil,pilares,redaccion,medicion}.md`, `skills/linkedin-pro/SKILL.md`, `ia/REGLAS.md`, `cuenta/{perfil.json,voz.md}`, `red/estado.json` y este registro.
- Verificación: 71 pruebas → aprobado; `python3 ia/verificar.py ci` → aprobado.
- Pendiente: repositorio (Muse); título y cédula para el titular; copia de datos de LinkedIn (Profile.csv y Shares.csv); nombres por vetar.

## 2026-11-13 · Segunda pasada de la auditoría
- Agente: Claude Code (sesión en la nube)
- Solicitud: encargo del 13/11/2026: corregir todo lo que encuentre la auditoría independiente; el revisor volvió a atacar las correcciones.
- Cambios: siete hallazgos más (E-1 a E-7, en `docs/AUDITORIA-2026-11-13.md`): menos falsos positivos de anzuelo y captación, nuevos anzuelos y fórmulas de captación y de clientes detectados, precio de servicio como error salvo que describa el mercado, `publicado` no acepta fechas anteriores a la aprobación, `sellar --leidas-a-mano` exige `--lector` y guarda quién y cuándo, etiqueta de certeza corregida y apellido Castorena documentado.
- Archivos: `skills/linkedin-pro/scripts/{linkedin.py,test_linkedin.py}`, `skills/linkedin-pro/references/{mitos,pilares,prompts}.md`, `skills/linkedin-pro/SKILL.md`, `docs/AUDITORIA-2026-11-13.md`, `red/estado.json` y este registro.
- Verificación: 70 pruebas → aprobado con Python 3.13 y 3.9; `python3 ia/verificar.py ci` → aprobado.
- Pendiente: los de la entrada «correcciones de la auditoría».

## 2026-11-13 · Regla de Emi sobre la IA y post del video del DOF
- Agente: Claude Code (sesión en la nube)
- Solicitud: respuestas de Emi del 13/11/2026 retransmitidas por la sesión «Matriz de Redes»: regla absoluta «Jamás en nada digas que lo armó una IA»; colores, estilo, nombrar las IA que usa, sin enlace a GitHub, cierre para equipos legales; video del DOF con subtítulos y urgencia de publicarlo hoy.
- Cambios: (1) Regla nueva en `pilares.md`, `redaccion.md`, `SKILL.md` e `ia/REGLAS.md`; `linkedin.py` marca como error decir que una pieza o herramienta la hizo una IA y publicar medios sintéticos de una persona real; se quitó el aviso `nota_ia`, que contradecía la regla. (2) Dos versiones del post para el video del DOF entregadas a la Matriz de Redes para que Emi elija y reescriba (borrador en `cuenta/privado/`, no se sube). (3) `cuenta/perfil.json` con las respuestas de la campaña de lanzamiento.
- Archivos: `skills/linkedin-pro/scripts/{linkedin.py,test_linkedin.py}`, `skills/linkedin-pro/references/{pilares,redaccion}.md`, `skills/linkedin-pro/SKILL.md`, `ia/REGLAS.md`, `cuenta/perfil.json`, `red/estado.json` y este registro.
- Verificación: 67 pruebas → aprobado; `python3 ia/verificar.py ci` → aprobado; los dos borradores del post → `revisar` sin errores.
- Pendiente: que Emi elija el texto, lo publique y mande el enlace; láminas de la campaña.

## 2026-11-13 · linkedin-pro 1.0.0: correcciones de la auditoría independiente
- Agente: Claude Code (sesión en la nube)
- Solicitud: encargo del 13/11/2026: auditoría adversarial independiente y corregir todo lo que encuentre. Además, datos que Emi dio a la sesión «Matriz de Redes» ese día y que esa sesión retransmitió: se presenta como abogado que estudia la Maestría en Alta Dirección, titular propuesto, aprobación en paquete semanal, tono fuerte permitido, frase «la IA reemplaza tareas, no criterio».
- Cambios: 37 hallazgos corregidos (detalle en `docs/AUDITORIA-2026-11-13.md`). Entre ellos: la huella de aprobación cubre toda la pieza; `aprobar` exige `--reescrito`, admite varias piezas (paquete semanal), compara con X y no reaprueba lo publicado; `publicado` solo acepta piezas aprobadas, fecha pasada y enlace de post; nuevos patrones de anzuelos, captación, clientes, Castorena (hashtag y dominio), lista privada de nombres vetados, encuestas políticas, insultos y partido, con menos falsos positivos; sin crashes con tipos raros; `sellar` ya no sella páginas cambiadas o sin leer; 13 fuentes más (54 en total); citas corregidas (Srinivasan, Buffer, Metricool, Van der Blom, boletín); GitHub ya no descarga páginas de LinkedIn; control de enlaces de todos los Markdown; fecha del centro de México en los dos scripts; privacidad de métricas y de terceros. Fuentes del feed ampliadas con señales oficiales, ingeniería 2025-2026, editores y transparencia DSA. `cuenta/perfil.json` registra la presentación y el modo de aprobación.
- Archivos: `skills/linkedin-pro/scripts/{linkedin.py,test_linkedin.py}`, `skills/linkedin-pro/references/*.md`, `skills/linkedin-pro/data/{fuentes.json,limites.json}`, `skills/linkedin-pro/SKILL.md`, `ia/{verificar.py,test_verificar.py,REGLAS.md}`, `.github/workflows/{control.yml,fuentes.yml}`, `cuenta/{perfil.json,referencias.md}`, `red/estado.json`, `docs/AUDITORIA-2026-11-13.md`, `README.md` y este registro.
- Verificación: 65 pruebas de `linkedin.py` y 5 de `verificar.py` → aprobado con Python 3.13 y 3.9; `python3 ia/verificar.py ci` → aprobado; `fuentes revisar --red` → sin cambios en 54 fuentes; workflows de GitHub → no ejecutados hasta el primer push.
- Pendiente: (a) Emi: crear `lianfixx/LinkedIn` y autorizar a la sesión a conectarlo. (b) Emi: confirmar la lectura semanal de páginas públicas de LinkedIn por la tarea de fuentes, el sello automático en `main` y que sus métricas vayan en el repositorio público. (c) Emi: capturas del perfil completo, nombres vetados en `cuenta/privado/nombres-vetados.txt` (archivo local, no se sube) y respuestas de la campaña de lanzamiento. (d) Crear la tarea semanal de fuentes cuando exista el repositorio. (e) Enviar a Vox Studio `puente/PETICION-vox.md` si Emi lo autoriza.

## 2026-11-13 · linkedin-pro 1.0.0: skill de LinkedIn con fuentes oficiales y certeza por regla
- Agente: Claude Code (sesión en la nube)
- Solicitud: encargo del 13/11/2026 para construir la skill de LinkedIn de Emi con el método de x-viral (`lianfixx/X`). Respuestas de Emi el mismo día en el chat de Claude Code: perfil `linkedin.com/in/emiliano-milla`; solo perfil personal; optimizar el perfil como primer entregable; objetivos de autoridad en IA + Derecho y de red y oportunidades; captar clientes de MILLA «ahora no»; pilares 60/25/15 (IA + Derecho, carrera y maestría, opinión); gym solo con lección profesional; todos los formatos; 2 piezas por semana; tono profesional y cercano con algo de humor; revisión semanal de fuentes; nombre `linkedin-pro`.
- Cambios: (1) Investigación en tres agentes: feed y transparencia, formatos y perfil, y estudios de terceros y mitos, con fuentes primarias de LinkedIn leídas el 13/11/2026. (2) Skill `linkedin-pro` con diez referencias; cada afirmación sobre LinkedIn marcada como [oficial], [terceros] o [criterio], y el control falla si falta. (3) `linkedin.py`: revisión de borradores y semanas (anzuelos, captación, límites de Emi, límites técnicos de cada formato, duplicados también contra X, cadencia y balance), compuerta de aprobación ligada a la huella del contenido, entrega lista para copiar, registro de publicados y métricas por captura, aprendizajes, vigilancia de fuentes por frases marca, `red/estado.json` para la Matriz de Redes (contrato `redes-estado/0.1`, acordado con esa sesión) y puente con Vox Studio. (4) Estado inicial en `cuenta/`, puente y petición para Vox Studio en `puente/`. (5) Puentes `.claude/skills/` y `.agents/skills/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, instrucciones de proyecto, protocolo común, reglas propias, control y dos workflows.
- Archivos: todos los del repositorio (creación).
- Verificación: ver la entrada de arriba («correcciones de la auditoría») y `docs/AUDITORIA-2026-11-13.md`.
- Pendiente: ver la entrada de arriba.
