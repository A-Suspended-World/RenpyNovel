# Sistema de diálogo

## Flujo

1. El guion invoca un objeto `Character`, por ejemplo `k "Hola"`.
2. El personaje aporta colores y el indicador de continuación.
3. Ren'Py muestra el screen especial `say(who, what)`.
4. Los elementos con ID `who`, `what`, `window`, `namebox` y `accent` reciben
   las propiedades configuradas por el personaje.
5. El estilo `menu_ui_dialogue_text` revela el texto progresivamente y aplica
   el shader de aparición.

## Archivos

| Archivo | Función |
| --- | --- |
| `game/data/characters.rpy` | Identificadores que utiliza el guion. |
| `game/systems/dialogue/00_character_themes.rpy` | Paletas y constructor común. |
| `game/ui/dialogue/dialogue.rpy` | Estructura visual del cuadro. |
| `game/ui/dialogue/styles.rpy` | Posiciones, tamaños y tipografía. |
| `game/ui/dialogue/effects.rpy` | Aparición del cuadro y de las letras. |

## Legibilidad

El cuerpo usa `DIALOGUE_BODY_COLOR` por defecto para garantizar un contraste
estable en escenas largas. Cada tema conserva `dialogue_color`, por lo que se
puede asignar un color distinto a un personaje sin cambiar el screen.

La identidad del hablante se comunica principalmente mediante el nombre, la
línea luminosa, el cuadro del nombre y el indicador `◆`.

## Velocidad

`preferences.text_cps` tiene un valor inicial de 42 caracteres por segundo. El
jugador puede modificarlo en Preferencias o seleccionar velocidad instantánea.
El sistema no fuerza una velocidad durante la historia.
