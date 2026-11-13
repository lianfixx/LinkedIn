@AGENTS.md

# Claude Code en este repositorio

- La skill canónica está en `skills/linkedin-pro/` y se carga desde el puente `.claude/skills/linkedin-pro` (invocable como `/linkedin-pro`).
- Este repositorio no tiene frenos automáticos: las reglas de `ia/REGLAS.md` se cumplen a mano. Registra cada cambio con `Agente: Claude Code`.
- La sesión de LinkedIn está en box «main» (la abrió Emi el 13/11/2026): solo para leer perfil, posts y estadísticas, a ritmo de persona; nada de publicar ni interactuar sin su orden expresa. Las piezas aprobadas se le entregan listas para copiar, según `skills/linkedin-pro/references/entrega.md`. Para leer, usar `browser_fetch` en box (pestaña oculta con la sesión de Emi).
