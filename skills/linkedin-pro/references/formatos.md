# Formatos

Qué dice LinkedIn de cada formato y qué dicen los estudios de terceros. Leído el 13/11/2026. Certeza de cada afirmación: **[oficial]** (Centro de ayuda, políticas o declaraciones de LinkedIn), **[terceros]** (estudio externo con método, con su solidez) o **[criterio]** (decisión de esta skill). Los límites que aplica `linkedin.py` están en [data/limites.json](../data/limites.json).

**Lo primero:** LinkedIn **no publica ninguna ventaja de alcance por formato** [oficial: no aparece en el Centro de ayuda ni en sus comunicados]. Las cifras de «el PDF tiene más alcance» son de terceros, casi todas de páginas de empresa o de clientes de herramientas, y muestran correlación, no causa.

## Límites técnicos (perfil personal)

| Formato | Dato | Certeza y fuente |
|---|---|---|
| Texto | Hasta 3,000 caracteres por post. LinkedIn puede limitar cuántos posts se publican en un periodo, sin dar cifra. | [oficial] [a528176](https://www.linkedin.com/help/linkedin/answer/a528176) |
| Imagen | Hasta 20 fotos por post; 5 MB por foto; no se pueden editar una vez publicadas. | [oficial] [a527229](https://www.linkedin.com/help/linkedin/answer/a527229) |
| Documento | PDF, PPT, PPTX, DOC o DOCX; un archivo por post; hasta 100 MB y 300 páginas; no se cambia después de publicar; páginas del mismo tamaño. LinkedIn lo llama «documento», no «carrusel». | [oficial] [a518909](https://www.linkedin.com/help/linkedin/answer/a518909) |
| Video | Un video por post; de 3 s (2 s en móvil) a 15 min; de 75 KB a 5 GB; proporción de 1:2.4 a 2.4:1 (el 9:16 entra); admite subtítulos; dejar libres los bordes. | [oficial] [a548372](https://www.linkedin.com/help/linkedin/answer/a548372), [a554001](https://www.linkedin.com/help/linkedin/answer/a554001) |
| Feed de video vertical | No se puede publicar directamente en él: LinkedIn elige videos ya publicados «based on the quality and relevance». | [oficial] [a554001](https://www.linkedin.com/help/linkedin/answer/a554001) |
| Artículo | Hasta 125,000 caracteres; cualquier miembro puede publicarlos. El título de 100 caracteres solo aparece en fuentes de terceros. | [oficial] [a522483](https://www.linkedin.com/help/linkedin/answer/a522483) |
| Boletín | «All LinkedIn members have access to create a newsletter». El requisito de 150 seguidores es solo para Páginas. | [oficial] [a591266](https://www.linkedin.com/help/linkedin/answer/a591266) |
| Encuesta | De 2 a 4 opciones; 1 día, 3 días, 1 semana (por defecto) o 2 semanas; el autor ve quién votó y qué. **Prohibido pedir opiniones políticas, de salud u otros datos sensibles.** | [oficial] [a522948](https://www.linkedin.com/help/linkedin/answer/a522948), [a527273](https://www.linkedin.com/help/linkedin/answer/a527273) |
| Encuesta (largo de opción) | 30 caracteres por opción: dato que circula en terceros; el Centro de ayuda no lo publica. La skill lo usa como tope prudente. | [terceros] [criterio] |
| Programación | Nativa, de 10 minutos a 3 meses antes; no para Eventos ni Empleos. | [oficial] [a1347212](https://www.linkedin.com/help/linkedin/answer/a1347212) |
| LinkedIn Live | Solo con más de 150 seguidores o contactos, cuenta de 30 días o más y buen historial; requiere herramienta de transmisión externa. Con más de 180 seguidores observados, Emi pasa el umbral, pero no hay solicitud: LinkedIn evalúa y decide. | [oficial] [a568503](https://www.linkedin.com/help/linkedin/answer/a568503) |
| Modo creador | El interruptor se eliminó en marzo de 2024; las herramientas y la analítica siguen para todos. | [oficial] [a5999182](https://www.linkedin.com/help/linkedin/answer/a5999182) |

## Qué se sabe del rendimiento de cada formato

| Formato | Qué dicen los estudios | Certeza |
|---|---|---|
| Documento | Lidera en interacción por impresión en páginas de empresa (Socialinsider 2026: 7.00 % en 2025, n = 2.45 millones de posts de páginas; solidez media-alta). **En perfiles de 0 a 1,000 seguidores rinde 0.86× la mediana** y 1.49× con más de 50,000 (AuthoredUp, ~370,000 posts de perfiles; solidez media). Emi está en la franja chica: no es el formato por defecto. | [terceros] |
| Multi-imagen e imagen | Por encima del texto en interacción (Socialinsider 2026: 6.45 % y 5.30 %). Imagen vertical con más impresiones que horizontal o cuadrada (AuthoredUp; solidez media). | [terceros] |
| Texto | Por debajo de documento e imagen en interacción en páginas (4.50 %). En perfiles, los posts de 2,001 a 2,500 caracteres tienen las impresiones medianas más altas y los de menos de 400 las más bajas (AuthoredUp; solidez media). | [terceros] |
| Video | 6.00 % de interacción en páginas; las vistas por video cayeron 36 % interanual (Socialinsider). AuthoredUp le da 0.86 de alcance. | [terceros] |
| Encuesta | Alcance alto y poca interacción real (AuthoredUp: 1.78 de alcance, 0.37 de interacción). Votar no es conversar. | [terceros] |
| Enlace en el post | El formato con menos interacción en páginas (Socialinsider: 3.25 %). En perfiles, −27 % de impresiones (Metricool 2026). Ver [mitos.md](mitos.md). | [terceros] |
| Artículo y boletín | Sin estudio sólido de alcance en el feed. El boletín avisa a sus suscriptores, que es su ventaja propia. | [oficial] [a1432051](https://www.linkedin.com/help/linkedin/answer/a1432051) |

## Cómo los usa Emi

| Formato | Para qué | Certeza |
|---|---|---|
| Texto | La base: una idea, una experiencia o una opinión fundada. La mayoría de las piezas. | [criterio] |
| Documento | Guías y listas de verificación que se guardan (por ejemplo, verificar citas que propone la IA). Una o dos al mes; probar contra texto con las métricas propias antes de subirle la frecuencia. | [criterio] |
| Imagen | Foto real de Emi en contexto profesional (clase, evento, Banxico) o un esquema propio. Nada de imágenes genéricas de banco o de IA sin decirlo. | [criterio] |
| Video | Solo videos que Emi ya aprobó en Vox Studio y que encajen con el tono de LinkedIn. Ver [conexion-vox.md](conexion-vox.md). | [criterio] |
| Artículo | Análisis largo (una reforma, una sentencia, un tema de la maestría) con fuentes. Uno al mes como máximo. | [criterio] |
| Boletín | Solo cuando haya material para sostener una periodicidad. Propuesta para más adelante, no para el arranque. | [criterio] |
| Encuesta | Preguntas de práctica profesional, nunca políticas. Rara vez. | [oficial] [criterio] |
