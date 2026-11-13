# Optimización del perfil

Primer entregable que eligió Emi (13/11/2026). Las IA no inician sesión, así que **la propuesta se arma con capturas que pasa Emi** y él hace los cambios desde su cuenta. Certeza de cada punto: **[oficial]**, **[terceros]** o **[criterio]**.

## Lo que se ve hoy (sin sesión)

| Dato | Valor | Certeza |
|---|---|---|
| URL | `linkedin.com/in/emiliano-milla` (ya personalizada) | [oficial] lo que muestra LinkedIn |
| Titular | «Abogado en Formación \| Enlace Universitario Banxico 2026» | [terceros] ficha que muestra Google el 13/11/2026; LinkedIn pide sesión para ver el perfil |
| Red | Más de 180 seguidores y 192 contactos; área metropolitana de Ciudad de México | [terceros] misma ficha de Google |

Para lo demás («Acerca de», experiencia, formación, destacados, aptitudes, foto, portada) hacen falta capturas de Emi.

## Qué dice LinkedIn

| Elemento | Dato | Certeza y fuente |
|---|---|---|
| Perfil completo | «A complete LinkedIn profile will increase your discoverability and profile search appearances». Con foto, «up to 2X more profile views». | [oficial] [a554351](https://www.linkedin.com/help/linkedin/answer/a554351) |
| Verificación | «Complete and verify your profile where available. Verifications are one of many signals» de autenticidad. | [oficial] [a516930](https://www.linkedin.com/help/linkedin/answer/a516930) |
| Titular | Sale en los resultados de búsqueda y puede ser distinto del puesto actual. El Centro de ayuda no publica límite de caracteres; los 220 que circulan son de terceros. | [oficial] [a542926](https://www.linkedin.com/help/linkedin/answer/a542926) · [terceros] |
| Acerca de | Debe expresar «your mission, motivation, and skills»; idealmente uno o dos párrafos. El límite de 2,600 caracteres solo aparece en terceros. | [oficial] [a554351](https://www.linkedin.com/help/linkedin/answer/a554351) · [terceros] |
| Experiencia | Debe reflejar experiencia profesional real con la organización nombrada; las asociaciones informales no van. | [oficial] [a593695](https://www.linkedin.com/help/linkedin/answer/a593695) |
| Destacados | Elementos ilimitados, se muestran 400; solo los ven usuarios con sesión. | [oficial] [a552452](https://www.linkedin.com/help/linkedin/answer/a552452) |
| Foto | De 400×400 a 7680×4320 px, hasta 8 MB, PNG o JPG; debe reflejar su imagen real. | [oficial] [a549049](https://www.linkedin.com/help/linkedin/answer/a549049) |
| Portada | 1584×396 px recomendado, JPG o PNG, menos de 8 MB. | [oficial] [a568217](https://www.linkedin.com/help/linkedin/answer/a568217) |
| URL personalizada | De 3 a 100 caracteres; hasta 5 cambios cada 6 meses. | [oficial] [a542685](https://www.linkedin.com/help/linkedin/answer/a542685) |
| Botón personalizado | Solo para algunos suscriptores de Premium Business, Sales Navigator y Recruiter Lite. No aplica hoy. | [oficial] [a1484520](https://www.linkedin.com/help/linkedin/answer/a1484520) |
| Asistente de IA del perfil | Solo para algunos Premium; si se usa, Emi revisa y reescribe. | [oficial] [a1444194](https://www.linkedin.com/help/linkedin/answer/a1444194) |

## Cómo se arma la propuesta

| Regla | Detalle | Certeza |
|---|---|---|
| Titular | Qué hace y para quién, con las palabras que usaría alguien que lo busca: abogado, IA, derecho, México. Sin adjetivos vacíos («apasionado», «visionario»). Dos o tres opciones para que Emi elija. | [criterio] |
| «Abogado en Formación» | Decidir con Emi cómo se presenta hoy (estudiante, pasante, abogado titulado). La skill no cambia su situación profesional: usa la que él confirme. | [criterio] |
| Acerca de | Primera persona; misión, qué trabaja (IA + Derecho), qué está construyendo y estudiando, y cómo contactarlo para conversar o colaborar. Sin ofrecer servicios de MILLA mientras `captacion_milla` sea `false`. | [oficial] [criterio] |
| Experiencia | Solo experiencia real con la organización nombrada. Castorena Abogados no se menciona en contenido; si Emi la tiene en su experiencia, es su decisión y no se toca desde aquí. MILLA ABOGADOS como experiencia propia, sin oferta. | [oficial] [criterio] |
| Destacados | Dos o tres piezas propias que muestren criterio (un artículo, un documento útil, un reconocimiento verificable). Se llenan conforme existan. | [criterio] |
| Aptitudes | Las que de verdad ejerce y puede sostener; ordenar las de IA + Derecho primero. | [oficial] [criterio] |
| Verificación | Si LinkedIn ofrece verificar identidad o lugar de trabajo, Emi lo hace él mismo desde su teléfono. | [oficial] |

## Pasos

1. Emi manda capturas del perfil completo (o copia el texto de cada sección).
2. La IA arma `cuenta/privado/perfil-propuesta.md` con opciones por sección, cada cambio con su porqué. No se sube a GitHub: es borrador.
3. Emi elige y reescribe. Él aplica los cambios en LinkedIn.
4. Se anota en `cuenta/perfil.json` (`observado`) lo que quedó y en `CHANGELOG.md` el cambio.
