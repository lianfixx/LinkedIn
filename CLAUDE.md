@AGENTS.md

# Claude Code en este repositorio

- La skill canónica está en `skills/linkedin-pro/` y se carga desde el puente `.claude/skills/linkedin-pro` (invocable como `/linkedin-pro`).
- Este repositorio no tiene frenos automáticos: las reglas de `ia/REGLAS.md` se cumplen a mano. Registra cada cambio con `Agente: Claude Code`.
- No se inicia sesión en LinkedIn desde box ni desde ninguna otra máquina (regla de Emi, 13/11/2026, tras los bloqueos de X). Las piezas aprobadas se le entregan listas para copiar, según `skills/linkedin-pro/references/entrega.md`. Box sí sirve para leer páginas públicas (`browser_fetch`); los perfiles de LinkedIn piden sesión, así que se ven por lo que muestran los buscadores.
