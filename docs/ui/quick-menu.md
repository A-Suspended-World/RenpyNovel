# Menú rápido

El screen `quick_menu` se muestra como overlay mientras `quick_menu` sea `True`.
Su implementación está en `game/ui/dialogue/quick_menu.rpy`.

## Acciones de escritorio

| Opción | Acción Ren'Py |
| --- | --- |
| Atrás | `Rollback()` |
| Historial | `ShowMenu("history")` |
| Saltar | `Skip()` |
| Auto | `Preference("auto-forward", "toggle")` |
| Guardar | `ShowMenu("save")` |
| G. rápido | `QuickSave()` |
| C. rápida | `QuickLoad()` |
| Opciones | `ShowMenu("preferences")` |

La variante táctil muestra menos botones y aumenta su área interactiva.

## Idiomas

Todos los rótulos se envuelven con `_()`. La traducción inglesa está en
`game/tl/english/dialogue_ui.rpy`. El jugador puede cambiar de idioma desde
Preferencias mediante las acciones `Language(None)` y `Language("english")`.
