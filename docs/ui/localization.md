# Idiomas de la interfaz

El idioma base del proyecto es español. La traducción inglesa de la interfaz
personalizada vive en `game/tl/english/dialogue_ui.rpy`.

## Selector

La pantalla `game/ui/screens/preferences.rpy` usa las acciones nativas de
Ren'Py:

- `Language(None)` activa el idioma base, español.
- `Language("english")` activa la traducción inglesa.

Ren'Py conserva la selección en los datos persistentes del jugador.

## Texto traducible

Todo texto visible nuevo debe envolverse con `_()`:

```renpy
textbutton _("Opciones") action ShowMenu("preferences")
```

Después se agrega su pareja al bloque `translate english strings`:

```renpy
old "Opciones"
new "Settings"
```

La traducción actual cubre el menú rápido, navegación lateral, preferencias,
guardado y carga, extras, pantallas provisionales y nombres de roles.

## Diálogo de la historia

Este archivo traduce la interfaz, no los capítulos. Cuando se traduzca la
historia, Ren'Py puede generar los bloques de diálogo dentro de
`game/tl/english/` sin alterar el sistema visual ni las paletas.
