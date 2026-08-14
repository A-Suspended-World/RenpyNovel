# Agregar un efecto de texto

## Usar un shader incluido

Primero consulta si Ren'Py ya proporciona el efecto. Para aplicarlo a una parte
del diálogo utiliza `{shader=...}`.

```renpy
"Texto {shader=wave}animado{/shader}."
```

## Cambiar el efecto normal

Edita `menu_ui_dialogue_text_shader` en
`game/ui/dialogue/effects.rpy`. El valor se aplica únicamente al estilo del
texto narrativo.

## Crear un shader propio

Los shaders personalizados deben registrarse en un módulo separado dentro de
`game/systems/dialogue/`. Documenta sus uniforms, plataformas probadas y una
alternativa sin animación. Después ejecuta compilación, lint y una prueba visual
con texto largo, historial, rollback y velocidad instantánea.
