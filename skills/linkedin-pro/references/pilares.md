# Pilares, objetivos y límites

Decididos por Emi el 13/11/2026. Cambiar cualquiera de estos puntos requiere su confirmación expresa. Las proporciones viven en `cuenta/perfil.json` y las aplica `linkedin.py`.

## Objetivos

1. **Autoridad profesional en IA + Derecho en México**: que quien busque a alguien que entiende cómo se usa la IA en el trabajo jurídico, con rigor, lo encuentre a él.
2. **Red y oportunidades**: empleo, alianzas y academia (incluida la Maestría en Alta Dirección).

**Captación de clientes de MILLA ABOGADOS: no, por ahora** (respuesta de Emi: «Ahora no»). MILLA puede aparecer como parte de su trayectoria, pero ninguna pieza ofrece servicios, precios ni consultas. `linkedin.py` marca como error las fórmulas de captación mientras `captacion_milla` sea `false`. Si Emi decide abrirla, antes hay que fijar con él los límites éticos (sin promesas de resultado, sin precios públicos, cómo se atiende un mensaje privado) y escribirlos aquí.

## Pilares

| Pilar | id | Meta | Qué entra |
|---|---|---|---|
| IA + Derecho | `ia-derecho` | 60 % | Cómo se usa la IA en el trabajo jurídico en México: herramientas, verificación, riesgos, regulación, casos públicos, lo que Emi construye y aprende. |
| Carrera, maestría y liderazgo | `carrera` | 25 % | Formación, Maestría en Alta Dirección, Banxico, decisiones de carrera, disciplina y hábitos. El gym y el estilo de vida solo entran aquí, y solo cuando dejan una lección profesional (`leccion_profesional`). |
| Opinión jurídico-política | `opinion` | 15 % | Análisis de reformas, sentencias y decisiones públicas como abogado con postura, crítico independiente. |

`linkedin.py balance` dice qué pilar toca. `semana` avisa si un pilar se aleja más de 15 puntos de su meta (a partir de 4 piezas).

## Opinión política en LinkedIn

- Emi opina como analista jurídico con postura: fundamenta, cita la fuente oficial y critica decisiones e ideas, no personas.
- La postura la da él con sus palabras, antes de redactar (`opinion_emi`).
- Participa en Acción Política Juvenil Tlalnepantla (PAN), pero su perfil personal **no habla a nombre del partido ni usa sus logotipos**. Si una pieza menciona al partido, `linkedin.py` avisa para confirmarlo.
- Las encuestas de LinkedIn no pueden pedir opiniones políticas ni datos sensibles (Centro de ayuda, a527273); en el pilar de opinión no se usan encuestas.
- En periodo electoral, nada sobre candidatos o partidos sin su confirmación expresa.

## Límites permanentes (valen para todo lo que salga en su perfil)

1. **Nunca clientes ni asuntos** de ningún despacho, ni anonimizados. Un ejemplo hipotético o un asunto público con fuente se declara en `excepcion_limite`.
2. **No nombrar a Castorena Abogados ni a sus licenciados.**
3. **Sin ataques personales.**
4. **Toda cita legal con fuente oficial verificada** (DOF, SCJN, Cámara de Diputados, órganos oficiales). Se marca `cita_legal: true` y se ponen los enlaces en `fuentes`.
5. **Un post informa u opina, no asesora un caso concreto.** Nada de «en tu caso debes…».
6. **La IA propone, Emi reescribe.** No se inventan vivencias, opiniones, cifras ni citas.
7. **Jamás decir que algo lo hizo una IA** (Emi, 13/11/2026, a la Matriz de Redes: «Jamás en nada digas que lo armó una IA»). Ninguna pieza dice que la hizo, la armó o la editó una IA; las herramientas las construyó él. Sí se nombran las IA que usa. LinkedIn recomienda avisar cuando se usó mucha IA y no es obvio (a1481496), pero es recomendación; lo obligatorio es no publicar medios sintéticos que muestren a una persona real diciendo o haciendo lo que no hizo, y eso aquí no se publica.

## Cada red es independiente

La misma idea puede salir en X, LinkedIn y otras redes, pero **adaptada**: nunca el mismo texto pegado. `linkedin.py revisar --contra-x` compara con lo publicado en X (`lianfixx/X`) y marca como error un texto casi idéntico. Las reglas de cada red viven en su propia skill; aquí no se copian.
