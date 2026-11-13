# Entregar una pieza para que Emi la publique

## Modo vigente

**Sesión en box, solo para leer.** La sesión de LinkedIn vive en la computadora virtual de Emi (box «main»): Emi la abrió él mismo el 13/11/2026 y pidió que se use. Ahí una IA puede **leer** su perfil, sus posts y sus estadísticas, a ritmo de persona. **No** publica, programa, reacciona, comenta, invita, manda mensajes ni edita el perfil sin una orden expresa de Emi para esa acción concreta. Nunca se escribe ni se pide su contraseña: si la sesión se cae, Emi la vuelve a abrir en box. El Acuerdo de usuario de LinkedIn (§8.2, vigente desde el 3/11/2025) prohíbe usar bots o métodos automatizados no autorizados para crear, comentar, reaccionar o compartir publicaciones, y prohíbe el scraping; por eso la lectura es puntual y nada se automatiza. Por eso:

1. La IA prepara la pieza, Emi la reescribe y la aprueba, sola o en el paquete semanal (`linkedin.py aprobar … --reescrito`).
2. La IA la entrega lista para copiar con `linkedin.py entregar ARCHIVO ID`: fecha, hora del centro de México, formato, archivo adjunto si lo hay y el texto exacto.
3. **Se publica.** Desde el 13/11/2026, Emi pidió que **Claude publique** desde su sesión en box, siempre con su confirmación final: la IA le muestra el bloque de `entregar` (texto exacto, archivo, fecha, hora y huella), Emi responde que sí a **esa** pieza, y solo entonces la IA la publica o la programa en LinkedIn, a mano en el navegador, sin scripts. Después anota el enlace con `publicado`. Sin ese sí explícito, no se publica nada. Si Emi prefiere hacerlo él, la publica desde su teléfono o computadora. Si quiere dejarla programada, LinkedIn tiene programación nativa: de 10 minutos a 3 meses antes, con el icono del reloj (en escritorio, abajo a la derecha; en móvil, arriba a la derecha). No sirve para Eventos ni Empleos. La hora se toma de la zona horaria del dispositivo (Centro de ayuda, a1347212).
4. Emi manda el enlace del post. La IA lo anota con `linkedin.py publicado ARCHIVO ID --url URL` (y `--fecha`, `--hora` si salió en otro momento). Solo acepta piezas aprobadas, enlaces de un post y fechas que ya pasaron.
5. **A los 7 días**, Emi manda captura de las estadísticas del post y la IA las anota con `linkedin.py metricas`. Ver [medicion.md](medicion.md).

## Formato del bloque de entrega

Lo genera `entregar`; no se escribe a mano:

```
PUBLICAR EN LINKEDIN · 2026-11-18 a las 08:30 (hora del centro de México)
Pieza: 2026-W47-a · pilar ia-derecho · formato documento · huella 3f2a…
TÍTULO DEL DOCUMENTO: …
ARCHIVO: …
TEXTO:
----------------------------------------
(texto exacto)
----------------------------------------
```

`entregar` se niega si la pieza tiene errores, si la aprobación no corresponde al texto vigente (huella) o si la fecha y hora ya pasaron.

## Si algo cambia

- **Antes de publicar**: si cambia una sola palabra, la fecha, la hora, el pilar, la postura o las fuentes, se vuelve a correr `revisar` y `aprobar` (con `--de-nuevo` si ya se había entregado). La aprobación vale para una pieza exacta.
- **Ya programada en LinkedIn**: la edita o borra Emi desde su cuenta. La IA actualiza el archivo y la vuelve a entregar.
- **Ya publicada**: LinkedIn permite editar el texto de un post publicado, pero no cambiar un documento ni las fotos ya subidas (Centro de ayuda, a518909 y a527229). Si Emi edita, se anota en `cuenta/aprendizajes.md` qué cambió y por qué.

## Lo que la IA nunca hace

Publicar, programar, reaccionar, comentar, enviar invitaciones o mensajes, ni usar extensiones o herramientas que lo hagan por él. Herramientas de programación de socios de LinkedIn (Buffer, Hootsuite y otras) solo si Emi lo decide y las conecta él mismo; esta skill no las configura.
