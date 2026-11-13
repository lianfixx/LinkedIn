# linkedin-pro · la skill de LinkedIn de Emi

Skill para planear, redactar, revisar, entregar para publicar y medir lo que Emi publica en su perfil personal de LinkedIn ([linkedin.com/in/emiliano-milla](https://www.linkedin.com/in/emiliano-milla)). Sirve en cualquier IA.

Objetivos: **autoridad en IA + Derecho en México** y **red y oportunidades**. Pilares: IA + Derecho 60 %, carrera y maestría 25 %, opinión jurídico-política 15 %. Dos piezas por semana. Sin captar clientes por ahora.

## De dónde sale

Del método de la skill hermana x-viral (`lianfixx/X`), que partió del código público del algoritmo de X. **LinkedIn no publica el suyo**, así que aquí las fuentes son, en este orden: Centro de ayuda y políticas de LinkedIn, sus comunicados y su blog de ingeniería, declaraciones de sus directivos y, después, estudios de terceros con método explícito. Cada regla dice si es **oficial**, **de terceros** o **criterio**; el control de GitHub falla si una viñeta o fila de `feed.md`, `formatos.md`, `mitos.md` o `perfil.md` no lo dice. Lo que no tiene sustento está en [mitos.md](skills/linkedin-pro/references/mitos.md). Detalle de la revisión en la [auditoría](docs/AUDITORIA-2026-11-13.md).

## Mapa

| Ruta | Qué es |
|---|---|
| [`skills/linkedin-pro/SKILL.md`](skills/linkedin-pro/SKILL.md) | La skill: reglas, flujo y a dónde ir según el encargo. |
| [`references/feed.md`](skills/linkedin-pro/references/feed.md) | Lo que LinkedIn dice de su feed, con fuente y certeza. |
| [`references/mitos.md`](skills/linkedin-pro/references/mitos.md) | Lo que se dice sin sustento, y qué hay de verdad. |
| [`references/formatos.md`](skills/linkedin-pro/references/formatos.md) | Límites oficiales y rendimiento de cada formato. |
| [`references/perfil.md`](skills/linkedin-pro/references/perfil.md) | Optimización del perfil. |
| [`references/pilares.md`](skills/linkedin-pro/references/pilares.md) | Objetivos, pilares, opinión política y límites. |
| [`references/redaccion.md`](skills/linkedin-pro/references/redaccion.md) | Cómo se escribe y se revisa una pieza. |
| [`references/playbook.md`](skills/linkedin-pro/references/playbook.md) | El plan para el perfil, paso a paso. |
| [`references/entrega.md`](skills/linkedin-pro/references/entrega.md) | Cómo se le entrega una pieza a Emi para que la publique. |
| [`references/medicion.md`](skills/linkedin-pro/references/medicion.md) | Métricas por captura y revisión mensual. |
| [`references/fuentes.md`](skills/linkedin-pro/references/fuentes.md) | Todas las fuentes, por tipo, con fecha. |
| [`references/conexion-vox.md`](skills/linkedin-pro/references/conexion-vox.md) | Puente con Vox Studio (videos). |
| [`references/prompts.md`](skills/linkedin-pro/references/prompts.md) | Encargos listos para copiar. |
| [`references/portabilidad.md`](skills/linkedin-pro/references/portabilidad.md) | Cómo cargarla en cada IA. |
| [`scripts/linkedin.py`](skills/linkedin-pro/scripts/linkedin.py) | Revisión de borradores y semanas, aprobación, entrega, registro, métricas, fuentes, estado. |
| [`data/`](skills/linkedin-pro/data/limites.json) | Límites técnicos oficiales y fuentes vigiladas. |
| [`cuenta/`](cuenta/README.md) | Estado del perfil: configuración, voz, aprendizajes, publicados. |
| [`red/estado.json`](red/estado.json) | Resumen para la Matriz de Redes (contrato `redes-estado/0.1`). |
| [`puente/`](puente/README.md) | Lo que linkedin-pro deja para Vox Studio. |
| [`ia/`](ia/REGLAS.md) | Reglas, protocolo entre IA y control. |
| [`docs/`](docs/AUDITORIA-2026-11-13.md) | Auditoría. |
| [`CHANGELOG.md`](CHANGELOG.md) | Registro de cada cambio. |

## Uso rápido

```bash
python3 skills/linkedin-pro/scripts/linkedin.py balance                                   # qué pilar toca
python3 skills/linkedin-pro/scripts/linkedin.py revisar cuenta/privado/b.json --contra-x  # revisar una pieza
python3 skills/linkedin-pro/scripts/linkedin.py semana cuenta/privado/2026-W47.json       # revisar una semana
python3 skills/linkedin-pro/scripts/linkedin.py aprobar cuenta/privado/2026-W47.json ID [ID…] --medio "chat" --reescrito
python3 skills/linkedin-pro/scripts/linkedin.py entregar cuenta/privado/2026-W47.json ID  # bloque listo para copiar
python3 skills/linkedin-pro/scripts/linkedin.py fuentes ver                               # vigencia de las fuentes
python3 skills/linkedin-pro/scripts/linkedin.py estado                                    # regenera red/estado.json
python3 ia/verificar.py ci                                                                # control completo antes de un commit
```

Python 3.9 o posterior, sin dependencias (probado con 3.9 y 3.13 en local, 3.10 y 3.12 en GitHub). Sin terminal: [portabilidad.md](skills/linkedin-pro/references/portabilidad.md).

## Cómo se mantiene al día

- Cada push pasa el control de [`control.yml`](.github/workflows/control.yml) con Python 3.10 y 3.12.
- Cada lunes, [`fuentes.yml`](.github/workflows/fuentes.yml) marca en rojo si la verificación de fuentes tiene más de 10 días. GitHub no descarga páginas de LinkedIn. GitHub pausa los workflows programados tras 60 días sin actividad en el repositorio.
- Revisión semanal: la tarea «LinkedIn · revisión semanal de fuentes» (cuenta de Claude de Emi, lunes 13:19 del centro de México, desde el 16/11/2026) lee las fuentes y busca comunicados nuevos; si nada cambió, sella la fecha; si algo cambió, abre un pull request.

## Estado

Versión 1.0.0 (13/11/2026). Ver la sección «Lo que no se pudo probar» de la [auditoría](docs/AUDITORIA-2026-11-13.md): no hay piezas publicadas, métricas ni correcciones de voz de Emi; el perfil completo no se ha visto (LinkedIn pide sesión).

El repositorio es público. Contiene las reglas de trabajo de Emi, no borradores ni datos de terceros.

Uso personal de Emiliano García Milla. Las páginas de LinkedIn y los estudios citados son de sus autores; aquí se citan y se enlazan.
