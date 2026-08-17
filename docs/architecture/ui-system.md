# Sistema de interfaz

La UI comparte tokens visuales para evitar que cada pantalla defina sus propios
colores, fuentes y sonidos.

## Núcleo

- `game/ui/core/theme.rpy`: rutas de recursos, colores y fuentes compartidas.
- `game/ui/core/transforms.rpy`: animaciones reutilizables.
- `game/ui/menu/styles.rpy`: estilos de los menús principales y secundarios.

## Diálogo

- `game/ui/dialogue/dialogue.rpy`: screen `say` activo.
- `game/ui/dialogue/styles.rpy`: geometría y apariencia del diálogo.
- `game/ui/dialogue/effects.rpy`: animación de entrada y shader de texto.
- `game/ui/dialogue/quick_menu.rpy`: accesos durante la historia.

## Cinemáticas

- `game/systems/cinematic/cinematic_mode.rpy`: oculta y restaura la interfaz
  para planos generales o ilustraciones a pantalla completa.
- `cinematic_still(...)`: API recomendada para un plano sin textbox.

## Convenciones

1. Los estilos nuevos usan el prefijo `menu_ui_`.
2. Las rutas de recursos se centralizan cuando se reutilizan.
3. Los strings visibles se envuelven con `_()` para poder traducirse.
4. Las variantes táctiles se declaran con `variant "touch"`.
5. La implementación generada originalmente se conserva con prefijo `legacy_`
   mientras exista una versión modular activa.
