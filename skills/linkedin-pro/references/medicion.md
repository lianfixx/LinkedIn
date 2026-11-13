# Medir

Las estadísticas de un post son privadas: solo las ve Emi (Centro de ayuda, a516971) [oficial]. Esta skill guarda sus cifras en el repositorio público porque son de Emi y sirven a la Matriz de Redes; **pendiente de que Emi confirme** que acepta publicarlas (si no, `cuenta/publicados.jsonl` pasa a `privado/`). Ninguna IA entra a su cuenta, así que **las métricas llegan por captura** que Emi manda.

## Cuándo pedirlas

- **A los 7 días de publicar**, captura de «Ver estadísticas» del post. Es criterio de la skill: da tiempo a que el post termine de circular y es fácil de recordar.
- **Cada mes**, captura de «Analytics & tools» del perfil (desde el perfil: Analytics → Show all): impresiones de todos los posts, seguidores nuevos y visitas al perfil. El resumen va en `cuenta/diagnosticos/AAAA-MM.md` **solo con cifras agregadas**: nunca nombres de quienes vieron el perfil o el post (son datos de terceros y el repositorio es público). Las capturas no se suben.

## Qué se anota

Nombres tal como los muestra LinkedIn en español (a516971?lang=es) y su clave en `linkedin.py metricas`:

| LinkedIn | Clave |
|---|---|
| Impresiones | `--impresiones` |
| Miembros alcanzados | `--miembros-alcanzados` |
| Reacciones | `--reacciones` |
| Comentarios | `--comentarios` |
| Compartir (reposts) | `--republicaciones` |
| Veces guardado | `--guardados` |
| Envíos en LinkedIn | `--envios` |
| Visualizaciones del perfil desde esta publicación | `--visitas-al-perfil` |
| Seguidores obtenidos a través de esta publicación | `--seguidores-ganados` |
| Visitas a los enlaces | `--clics` |
| Visualizaciones de video | `--visualizaciones-video` |
| Votos de encuesta | `--votos-encuesta` |
| Suscriptores del boletín | `--suscriptores-ganados` |

```bash
python3 skills/linkedin-pro/scripts/linkedin.py metricas 2026-W47-a --impresiones 812 --reacciones 23 \
  --comentarios 6 --guardados 9 --fuente "captura de Emi del 25/11/2026"
```

## Cuidado al leerlas

- Las cifras de LinkedIn son estimaciones, y **las vistas propias de Emi también cuentan** (a516971).
- LinkedIn guarda los datos por tiempo limitado: interacciones 1,000 días, miembros alcanzados 400 días, datos demográficos 180 días; artículos y boletines, dos años. Para video hay dos páginas oficiales que se contradicen (365 contra 180 días). Por eso se anotan a los 7 días y no se deja para después.
- Con 2 piezas por semana, **una sola pieza no prueba nada**. Las lecciones salen de comparar varias del mismo pilar o formato, y se escriben como hipótesis hasta que se repitan.

## Qué mirar

Para los objetivos de Emi (autoridad y red), en este orden [criterio]:

1. **Comentarios de colegas** y conversaciones que siguieron en privado (Emi lo cuenta).
2. **Guardados y envíos**: alguien quiso conservarlo o pasarlo.
3. **Visitas al perfil y seguidores ganados** desde el post.
4. Impresiones y miembros alcanzados: contexto, no meta.

Cada mes: `linkedin.py balance`, revisión de lo anterior y una o dos lecciones con `linkedin.py aprender`. Lo que funcione y sirva para video va a Vox Studio con `linkedin.py vox idea`.
