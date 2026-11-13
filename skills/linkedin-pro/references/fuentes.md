# Fuentes

Todas las fuentes que sostienen la skill, verificadas el 2026-11-13. La lista que se vigila cada semana está en [data/fuentes.json](../data/fuentes.json); este archivo es su versión legible. Orden de prioridad: Centro de ayuda y políticas, comunicados e ingeniería, directivos y, al final, estudios de terceros.

**Transparencia DSA (Unión Europea).** LinkedIn publica informes de transparencia por los artículos 15, 24 y 42 de la Ley de Servicios Digitales ([a1678508](https://www.linkedin.com/help/linkedin/answer/a1678508)). No se encontró una página propia sobre los parámetros del recomendador (art. 27): lo que hay está en [feed.md](feed.md), sección «Transparencia». Los informes de 2026 se publican en .zip y no se abrieron; tampoco el informe de implementación de la auditoría DSA. Se revisan en la tarea semanal.

## Centro de ayuda de LinkedIn

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [a528176](https://www.linkedin.com/help/linkedin/answer/a528176?lang=en) | Límite de 3,000 caracteres; límite de frecuencia sin cifra | formatos.md, limites.json |
| [a516930](https://www.linkedin.com/help/linkedin/answer/a516930?lang=en) | Distribución inicial a una parte de la red; relevancia profesional; consejos oficiales | feed.md, playbook.md, perfil.md |
| [a1481496](https://www.linkedin.com/help/linkedin/answer/a1481496?lang=en) | IA: voz propia, contenido genérico se distribuye menos, avisar si se usó mucha IA | feed.md, mitos.md, redaccion.md |
| [a1340752](https://www.linkedin.com/help/linkedin/answer/a1340752?lang=en) | Contenido falso o engañoso no se distribuye fuera de la red; medios sintéticos | feed.md |
| [a518909](https://www.linkedin.com/help/linkedin/answer/a518909?lang=en) | Documentos: 100 MB y 300 páginas | formatos.md, limites.json |
| [a548372](https://www.linkedin.com/help/linkedin/answer/a548372?lang=en) | Video: 3 s a 15 min, 5 GB, 1:2.4 a 2.4:1 | formatos.md, limites.json |
| [a554001](https://www.linkedin.com/help/linkedin/answer/a554001?lang=en) | Un video por post; feed vertical no admite publicar directo | formatos.md, conexion-vox.md |
| [a522483](https://www.linkedin.com/help/linkedin/answer/a522483?lang=en) | Artículos: 125,000 caracteres | formatos.md, limites.json |
| [a591266](https://www.linkedin.com/help/linkedin/answer/a591266?lang=en) | Boletín para todos los miembros | formatos.md |
| [a527273](https://www.linkedin.com/help/linkedin/answer/a527273?lang=en) | Encuestas: duraciones; prohibido pedir opiniones políticas | formatos.md, pilares.md, limites.json |
| [a522948](https://www.linkedin.com/help/linkedin/answer/a522948?lang=en) | Encuestas: de 2 a 4 opciones | formatos.md, limites.json |
| [a1347212](https://www.linkedin.com/help/linkedin/answer/a1347212?lang=en) | Programación nativa de 10 minutos a 3 meses | entrega.md, limites.json |
| [a516971](https://www.linkedin.com/help/linkedin/answer/a516971?lang=en) | Métricas de cada post y conservación de datos | medicion.md |
| [a554351](https://www.linkedin.com/help/linkedin/answer/a554351?lang=en) | Perfil completo, foto 2X vistas, Acerca de | perfil.md |
| [a5999182](https://www.linkedin.com/help/linkedin/answer/a5999182?lang=en) | Modo creador eliminado; Seguir o Conectar como acción principal | formatos.md, playbook.md |
| [a523360](https://www.linkedin.com/help/linkedin/answer/a523360?lang=en) | Señales para recomendar: calidad y relevancia profesional; desinterés y reportes | feed.md |
| [a1499047](https://www.linkedin.com/help/linkedin/answer/a1499047?lang=en) | Posts recomendados: interacciones previas, tiempo en la plataforma, perfil y probabilidad de interactuar | feed.md |
| [a1480504](https://www.linkedin.com/help/linkedin/answer/a1480504?lang=en) | Vista «Top» personalizada por defecto; «Recent» sin personalización | feed.md |
| [a1338787](https://www.linkedin.com/help/linkedin/answer/a1338787?lang=en) | Spam: retirar o limitar la distribución de lo que infla la interacción (encuestas de emojis, cadenas) | feed.md, mitos.md |

## Políticas y Acuerdo de usuario

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [politicas](https://www.linkedin.com/legal/professional-community-policies) | Prohíbe inflar la interacción artificialmente y los acuerdos de reacción mutua; medios sintéticos | feed.md, mitos.md |
| [acuerdo](https://www.linkedin.com/legal/user-agreement) | §8.2: prohíbe bots, scraping y automatizar interacciones | entrega.md, REGLAS.md |

## Transparencia DSA

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [a1678508](https://www.linkedin.com/help/linkedin/answer/a1678508?lang=en) | Informes de transparencia DSA (arts. 15, 24 y 42) | feed.md, fuentes.md |

## Comunicados y blog oficial de LinkedIn

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [mejora-feed-2026](https://news.linkedin.com/2026/ImprovingTheFeed) | Menos anzuelos y posts repetitivos; pods ineficaces; ranking con LLM | feed.md, mitos.md |
| [autenticidad-2026](https://news.linkedin.com/2026/authentic-content-and-conversations) | Pods no permitidos; alcance limitado a lo inflado; comentarios automatizados | feed.md, mitos.md |
| [editores-2026](https://news.linkedin.com/2026/HumansHelpingShapeLinkedInsFeed) | Más de 150 editores humanos influyen en qué temas y voces se muestran | feed.md |
| [mythbusting-2022](https://www.linkedin.com/blog/member/product/mythbusting-the-feed-how-the-algorithm-works) | Los algoritmos filtran el contenido de baja calidad | feed.md |

## Blog de ingeniería de LinkedIn

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [dwell-2020](https://engineering.linkedin.com/blog/2020/understanding-feed-dwell-time) | El tiempo de permanencia es señal del ranking | feed.md |
| [danchev-2026](https://www.linkedin.com/blog/engineering/feed/engineering-the-next-generation-of-linkedins-feed) | Recuperación con embeddings de LLM y modelo generativo; predice clic, saltar, lectura larga, reacción, comentario y compartir; sin atributos demográficos | feed.md |
| [jain-2025](https://www.linkedin.com/blog/engineering/feed/putting-members-first-testing-and-measuring-how-content-appears-in-your-feed) | Cientos de señales; no usa datos demográficos para la visibilidad | feed.md |

## Declaraciones de directivos de LinkedIn

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [lorenzetti-2026](https://www.linkedin.com/pulse/keeping-conversations-real-linkedin-laura-lorenzetti-9821e/) | Usar IA está bien si representa tu voz; lo genérico se distribuye menos | feed.md, mitos.md |
| [jurka-2026](https://www.linkedin.com/pulse/technology-behind-linkedins-fight-against-ai-slop-tim-jurka-7ojbc/) | Clasificadores de AI slop: 94 % de precisión, 40 % menos vistas | feed.md, mitos.md |
| [jobanputra-2025](https://www.linkedin.com/posts/rishij_i-shared-last-week-some-thoughts-on-what-activity-7358999334173990912-EI0Q/) | LinkedIn no está diseñado para la viralidad; conversaciones sobre likes | feed.md, mitos.md, playbook.md |
| [jurka-mar-2026](https://www.linkedin.com/pulse/updates-linkedin-feed-focusing-authentic-relevant-tim-jurka-umwnc) | Señales de perfil e interacción; anzuelos y pods | feed.md |
| [jobanputra-2024](https://www.linkedin.com/pulse/understanding-how-linkedin-feed-works-rishi-jobanputra-tshdc) | Pasar de largo u ocultar también enseña al feed; se quieren posts de conocimiento | feed.md |

## Estudios de terceros

| Fuente | Qué sostiene | Dónde se usa |
|---|---|---|
| [buffer-frecuencia-2025](https://buffer.com/resources/how-often-to-post-on-linkedin/) | Frecuencia: más posts no castigan cada post (≈2 millones de posts, efectos fijos por cuenta); solidez alta | mitos.md, playbook.md |
| [socialinsider-2026](https://www.socialinsider.io/blog/linkedin-engagement-report/) | Interacción por formato en páginas de empresa (2.45 millones de posts); solidez media-alta | formatos.md, mitos.md |
| [metricool-2026](https://newsletter.metricool.com/p/5-linkedin-stats-in-2026-you-probably-didn-t-see-coming) | Enlaces −27 % en perfiles y +51 % en páginas; 48 horas; hashtags (≈670,000 posts); solidez media | formatos.md, mitos.md |
| [authoredup-estadisticas](https://authoredup.com/blog/linkedin-post-statistics) | Longitud, formato y tamaño de cuenta en perfiles (≈370,000 posts); solidez media donde declara muestra | formatos.md, mitos.md |
| [buffer-algoritmo-2025](https://buffer.com/resources/linkedin-algorithm/) | Cita a Lorenzetti sobre hashtags y etiquetas (segunda mano de una declaración oficial) | mitos.md |
| [usera-2025](https://consensus.app/papers/details/w:60a05833-ac52-42cb-9bb1-91f2033bd949/) | Usera et al. 2025, revisado por pares: etiquetas y hashtags asociados a más reacciones (991 posts) | mitos.md |
| [vanderblom-2026](https://creatorscience.com/podcast/richard-van-der-blom-2/) | Caída del alcance y frecuencia de 2 a 4 por semana; método no publicado; solidez media-baja | mitos.md |

## Lo que no se pudo verificar

- Límites de caracteres del titular (220), «Acerca de» (2,600) y título de artículo (100): solo en fuentes de terceros; el Centro de ayuda no los publica.
- Conservación de la analítica de video: dos páginas oficiales se contradicen (365 contra 180 días: a516971 y a525196).
- Una frase atribuida a un directivo de LinkedIn según la cual no se limita el alcance de los posts con enlace: no se encontró en ninguna fuente primaria y no se usa.
- Un boletín de terceros (FutureSocial, 13/03/2026) dice que LinkedIn le confirmó que no trata distinto los enlaces ni los hashtags, sin cita con nombre: solidez baja, no se usa como oficial.
- Informes DSA de 2026 (.zip), informe de implementación de la auditoría DSA, el paper 360Brew (arXiv 2501.16450) y el de recuperación con modelos de lenguaje (arXiv 2510.14223): localizados, no leídos.
- Una cita de 2023 de Alice Xiong (LinkedIn) sobre «knowledge and advice»: solo de segunda mano (Entrepreneur); no se usa como oficial.
