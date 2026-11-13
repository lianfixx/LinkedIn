# Qué dice LinkedIn de su feed

LinkedIn **no publica el código ni los pesos de su ranking**. Lo que sigue es lo que la empresa dice en fuentes primarias, leído el 13/11/2026. Cada afirmación lleva su certeza: **[oficial]** (Centro de ayuda, políticas, comunicados, ingeniería o directivos de LinkedIn), **[terceros]** o **[criterio]**. Las citas van en inglés, como las publica LinkedIn. Lista completa de fuentes: [fuentes.md](fuentes.md).

## Cómo se reparte un post

| Afirmación | Fuente | Certeza |
|---|---|---|
| Un post se comparte primero con «a subset of your connections and followers, depending on your connection strength», los ajustes de notificación y el estado de cada quien. | Centro de ayuda, [a516930](https://www.linkedin.com/help/linkedin/answer/a516930) | [oficial] |
| «Content that's professionally relevant will benefit from organic distribution through your network». | [a516930](https://www.linkedin.com/help/linkedin/answer/a516930) | [oficial] |
| Consejos oficiales para la distribución: «Avoid being overly promotional», completar y verificar el perfil, interactuar con lo que publican otros miembros. | [a516930](https://www.linkedin.com/help/linkedin/answer/a516930) | [oficial] |
| «LinkedIn is not designed for virality»; las reacciones indican buena dirección, pero «authentic conversations and connection signify great engagement». Recomienda medir visitas al perfil y seguidores ganados por post. | Rishi Jobanputra, director sénior de producto del feed, [post de 2025](https://www.linkedin.com/posts/rishij_i-shared-last-week-some-thoughts-on-what-activity-7358999334173990912-EI0Q/) | [oficial] |
| El tiempo que alguien se detiene en un post («dwell time») es una señal del ranking. | LinkedIn Engineering, [2020](https://engineering.linkedin.com/blog/2020/understanding-feed-dwell-time) | [oficial] |
| Desde 2026 el ranking usa modelos de lenguaje (LLM) para entender el contenido. | Comunicado del [12/03/2026](https://news.linkedin.com/2026/ImprovingTheFeed) | [oficial] |
| Cuánto pesa cada señal, y en qué orden, no lo publica LinkedIn. Cualquier porcentaje que circule es de terceros o inventado. | Ausencia en todas las fuentes revisadas | [criterio] |

## Qué degrada o castiga

| Afirmación | Fuente | Certeza |
|---|---|---|
| LinkedIn trabaja para reducir «repetitive, low‑substance posts and engagement bait, such as "comment to agree" prompts» y para que los grupos de interacción sean ineficaces. | Comunicado del [12/03/2026](https://news.linkedin.com/2026/ImprovingTheFeed) | [oficial] |
| Los grupos coordinados para dar «me gusta», comentar y compartir no están permitidos; LinkedIn limita el alcance de los posts «artificially boosted». Los comentarios automatizados (extensiones, scripts) pueden ocultarse y la cuenta restringirse. | Comunicado del [13/03/2026](https://news.linkedin.com/2026/authentic-content-and-conversations) | [oficial] |
| «Don't do things to artificially increase engagement with your content… don't agree with others ahead of time to like or re-share each other's content». | [Políticas de la Comunidad Profesional](https://www.linkedin.com/legal/professional-community-policies) | [oficial] |
| «Content that feels generic, repetitive, or lacks a clear point of view is less likely to be widely distributed». Usar IA está permitido, pero el contenido debe reflejar la voz, perspectiva y experiencia del miembro; LinkedIn recomienda avisar si se usó mucha IA y no es obvio. Los miembros pueden marcar un post como «Seems like AI slop». | Centro de ayuda, [a1481496](https://www.linkedin.com/help/linkedin/answer/a1481496) | [oficial] |
| Lo que parece generado por IA y sin perspectiva clara «is less likely to be widely distributed beyond a person's immediate network». | Laura Lorenzetti, editora ejecutiva, [20/05/2026](https://www.linkedin.com/pulse/keeping-conversations-real-linkedin-laura-lorenzetti-9821e/) | [oficial] |
| Los clasificadores de «AI slop» revisan los posts que se distribuyen fuera de la red inmediata, con 94 % de precisión; desde agosto de 2026 ese contenido tiene 40 % menos vistas. | Tim Jurka, LinkedIn, [08/10/2026](https://www.linkedin.com/pulse/technology-behind-linkedins-fight-against-ai-slop-tim-jurka-7ojbc/) | [oficial] |
| El contenido falso o sustancialmente engañoso que no causa daño «is not eligible for distribution beyond the author's network». Los medios sintéticos que muestran a alguien diciendo o haciendo lo que no hizo, sin aclararlo, se retiran (salvo parodia evidente). | Centro de ayuda, [a1340752](https://www.linkedin.com/help/linkedin/answer/a1340752); Políticas | [oficial] |
| Bots, scraping, extensiones y cualquier método automatizado no autorizado para publicar, comentar, reaccionar, compartir, invitar o mandar mensajes están prohibidos; el riesgo es la restricción o el cierre de la cuenta. | [Acuerdo de usuario](https://www.linkedin.com/legal/user-agreement), §8.2 (vigente desde el 3/11/2025) | [oficial] |
| LinkedIn puede limitar cuántos posts publica un miembro en un periodo, sin dar cifra. | [a528176](https://www.linkedin.com/help/linkedin/answer/a528176) | [oficial] |

## Lo que LinkedIn no dice

| Afirmación | Fuente | Certeza |
|---|---|---|
| No hay regla oficial publicada sobre enlaces externos, hashtags, hora de publicación, edición del post, largo de los comentarios ni Premium. Lo que se dice está en [mitos.md](mitos.md), con la evidencia de terceros. | Ausencia en Centro de ayuda, políticas y comunicados revisados | [criterio] |
| No hay ventaja oficial de alcance por formato. Ver [formatos.md](formatos.md). | Ausencia en las mismas fuentes | [criterio] |

## Qué hace la skill con esto

| Regla | Por qué | Certeza |
|---|---|---|
| Cada pieza declara `para_quien` y `aporta`. | LinkedIn distribuye lo profesionalmente relevante y frena lo genérico. | [oficial] [criterio] |
| La IA propone y Emi reescribe con su experiencia. | Lo genérico o sin perspectiva se distribuye menos fuera de la red. | [oficial] |
| `linkedin.py` marca como error los anzuelos de interacción y la captación. | Anzuelos: degradados y contra las políticas. Captación: decisión de Emi. | [oficial] [criterio] |
| Cierre con pregunta genuina de su campo, no «comenta SÍ». | Conversación auténtica, sí; anzuelo, no. | [oficial] |
| Ninguna automatización ni grupos de interacción. | Prohibidos. | [oficial] |
| Métrica principal: comentarios de colegas, guardados, envíos, visitas al perfil y seguidores ganados. | Lo que recomienda medir el director de producto del feed. | [oficial] [criterio] |
