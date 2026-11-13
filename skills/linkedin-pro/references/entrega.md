# Entregar una pieza para que Emi la publique

## Modo vigente

**Ninguna IA inicia sesión en LinkedIn.** En X, la plataforma bloqueó el inicio de sesión desde las computadoras en la nube que usan las IA de Emi el 10 y el 11/11/2026, y Emi prohibió reintentarlo; la misma regla vale aquí desde el primer día. Además, el Acuerdo de usuario de LinkedIn (§8.2, vigente desde el 3/11/2025) prohíbe usar bots o métodos automatizados no autorizados para crear, comentar, reaccionar o compartir publicaciones, y prohíbe el scraping. Por eso:

1. La IA prepara la pieza, Emi la reescribe y la aprueba, sola o en el paquete semanal (`linkedin.py aprobar … --reescrito`).
2. La IA la entrega lista para copiar con `linkedin.py entregar ARCHIVO ID`: fecha, hora del centro de México, formato, archivo adjunto si lo hay y el texto exacto.
3. **Emi la publica** desde su teléfono o computadora. Si quiere dejarla programada, LinkedIn tiene programación nativa: de 10 minutos a 3 meses antes, con el icono del reloj (en escritorio, abajo a la derecha; en móvil, arriba a la derecha). No sirve para Eventos ni Empleos. La hora se toma de la zona horaria del dispositivo (Centro de ayuda, a1347212).
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

Iniciar sesión, publicar, programar, reaccionar, comentar, enviar invitaciones o mensajes, ni usar extensiones o herramientas que lo hagan por él. Herramientas de programación de socios de LinkedIn (Buffer, Hootsuite y otras) solo si Emi lo decide y las conecta él mismo; esta skill no las configura.
