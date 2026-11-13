# Registro de cambios

Lo más reciente arriba. Formato en `ia/PROTOCOLO.md`, sección 3.

## 2026-11-13 · linkedin-pro 1.0.0: skill de LinkedIn con fuentes oficiales y certeza por regla
- Agente: Claude Code (sesión en la nube)
- Solicitud: encargo del 13/11/2026 para construir la skill de LinkedIn de Emi con el método de x-viral (`lianfixx/X`). Respuestas de Emi el mismo día en el chat de Claude Code: perfil `linkedin.com/in/emiliano-milla`; solo perfil personal; optimizar el perfil como primer entregable; objetivos de autoridad en IA + Derecho y de red y oportunidades; captar clientes de MILLA «ahora no»; pilares 60/25/15 (IA + Derecho, carrera y maestría, opinión); gym solo con lección profesional; todos los formatos; 2 piezas por semana; tono profesional y cercano con algo de humor; revisión semanal de fuentes; nombre `linkedin-pro`.
- Cambios: (1) Investigación en tres agentes: feed y transparencia, formatos y perfil, y estudios de terceros y mitos, con fuentes primarias de LinkedIn leídas el 13/11/2026. (2) Skill `linkedin-pro` con diez referencias; cada afirmación sobre LinkedIn marcada como [oficial], [terceros] o [criterio], y el control falla si falta. (3) `linkedin.py`: revisión de borradores y semanas (anzuelos, captación, límites de Emi, límites técnicos de cada formato, duplicados también contra X, cadencia y balance), compuerta de aprobación ligada a la huella del contenido, entrega lista para copiar, registro de publicados y métricas por captura, aprendizajes, vigilancia de fuentes por frases marca, `red/estado.json` para la Matriz de Redes (contrato `redes-estado/0.1`, acordado con esa sesión) y puente con Vox Studio. (4) Estado inicial en `cuenta/`, puente y petición para Vox Studio en `puente/`. (5) Puentes `.claude/skills/` y `.agents/skills/`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, instrucciones de proyecto, protocolo común, reglas propias, control y dos workflows.
- Archivos: todos los del repositorio (creación).
- Verificación: ver la entrada siguiente y `docs/AUDITORIA-2026-11-13.md`.
- Pendiente: ver la auditoría.
