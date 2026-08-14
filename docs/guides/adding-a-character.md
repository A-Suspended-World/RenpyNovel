# Agregar un personaje

## 1. Crear una paleta

En `game/systems/dialogue/00_character_themes.rpy`, agrega una entrada única:

```python
"nova": {
    "name_color": "#9ee7ff",
    "accent_color": "#3ebfe8",
    "dialogue_color": DIALOGUE_BODY_COLOR,
},
```

Si quieres que todo el diálogo del personaje tenga otro color, cambia solamente
`dialogue_color`. Verifica que conserve contraste con el cuadro oscuro.

## 2. Declarar el personaje

En `game/data/characters.rpy`:

```renpy
define nova = make_dialogue_character("Nova", "nova")
```

## 3. Usarlo en la historia

```renpy
nova "Este diálogo utilizará automáticamente su tema."
```

## 4. Traducir el nombre cuando corresponda

Los nombres propios normalmente no cambian. Los títulos, roles o nombres
descriptivos se agregan a un bloque `translate <idioma> strings`.

## Identificadores

Cada variable debe ser única. Antes existían dos declaraciones llamadas `e`
para Elen y Estudiante; la segunda reemplazaba silenciosamente a la primera.
Ahora `e` identifica a Elen y `student` identifica a Estudiante.
