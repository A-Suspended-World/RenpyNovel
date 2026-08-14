# Efectos de texto

El proyecto utiliza text shaders incluidos en Ren'Py. No se ha incorporado una
librería externa de efectos tipográficos.

## Efecto predeterminado

`menu_ui_dialogue_text_shader = "dissolve"` hace que cada carácter aparezca
suavemente mientras avanza la velocidad de texto.

## Efectos narrativos puntuales

Ren'Py permite aplicar un shader a una parte de una línea:

```renpy
k "¡No vuelvas a hacer eso! {shader=jitter:1.0,3.0}¿Entendido?{/shader}"
```

Ejemplos útiles:

```renpy
"Una voz {shader=wave}distante{/shader} recorrió la sala."
"La señal comenzó a {shader=jitter:0.7,2.0}fallar{/shader}."
"La palabra apareció de {shader=zoom}repente{/shader}."
```

## Criterios de uso

- `jitter`: miedo, impacto, interferencia o grito.
- `wave`: voz sobrenatural, canto o recuerdo.
- `zoom`: énfasis breve.
- `dissolve`: lectura normal.

No se recomienda aplicar efectos intensos a párrafos completos. Deben conservar
la legibilidad y utilizarse como información narrativa, no como decoración
constante.
