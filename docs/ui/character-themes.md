# Temas de personajes

Los temas viven en `CHARACTER_DIALOGUE_THEMES`, dentro de
`game/systems/dialogue/00_character_themes.rpy`.

## Propiedades

| Propiedad | Uso |
| --- | --- |
| `name_color` | Nombre del personaje. |
| `accent_color` | Línea luminosa e indicador de continuación. |
| `dialogue_color` | Color del cuerpo del diálogo. |

`get_character_dialogue_theme(theme_id)` devuelve una paleta. Si el ID no
existe, utiliza el tema `narrator` para evitar que la interfaz falle.

`make_dialogue_character(name, theme_id, **kwargs)` crea el objeto `Character`
y conecta sus propiedades con los IDs del screen `say`.

## Paletas actuales

- `narrator`: azul grisáceo neutral.
- `yuu`: cian.
- `kuki`: rosa.
- `elen`: azul zafiro.
- `zofi`: dorado.
- `alice`: violeta azulado.
- `professor`: azul académico.
- `sis`: coral.
- `max`: ámbar.
- Personajes secundarios: variantes neutrales o violetas.

Los valores pueden ajustarse sin modificar capítulos ni pantallas.
