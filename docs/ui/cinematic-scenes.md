# Escenas cinematográficas sin textbox

El sistema cinematográfico muestra fondos o ilustraciones a pantalla completa
sin el cuadro de diálogo ni el menú rápido. Al terminar, restaura automáticamente
el estado anterior de la interfaz.

## Archivos

| Ruta | Responsabilidad |
| --- | --- |
| `game/systems/cinematic/cinematic_mode.rpy` | Estado, transiciones, movimiento y API reutilizable. |
| `game/data/definitions/bg_images.rpy` | Registro de imágenes que puede mostrar el sistema. |
| `game/assets/backgrounds/academy/lobby_cinematic.png` | Fondo del vestíbulo proporcionado como referencia. |
| `game/story/test/test_ui.rpy` | Prueba manual `test_cinematic_scene`. |

## Uso normal

```renpy
call cinematic_still("bg academy_lobby", duration=3.5)
```

La llamada realiza este ciclo:

1. Guarda el estado actual de `quick_menu`.
2. Oculta el menú rápido y ejecuta `window hide`.
3. Limpia la escena y muestra la imagen a `1920x1080`.
4. Aplica una entrada suave y un movimiento de cámara mínimo.
5. Espera el tiempo indicado o la interacción del jugador.
6. Ejecuta `window auto` y restaura el menú rápido.

## Parámetros

| Parámetro | Valor inicial | Función |
| --- | --- | --- |
| `image_name` | obligatorio | Nombre registrado de la imagen. |
| `duration` | `3.0` | Segundos visibles; `None` espera un clic. |
| `transition` | `cinematic_enter_transition` | Transición de entrada. |
| `motion` | `True` | Activa el zoom lento de plano general. |
| `skippable` | `True` | Permite adelantar una duración con interacción. |

Ejemplos:

```renpy
# Permanece hasta que el jugador continúe.
call cinematic_still("bg academy_lobby", duration=None)

# Plano fijo obligatorio de dos segundos.
call cinematic_still(
    "bg academy_lobby",
    duration=2.0,
    motion=False,
    skippable=False,
)
```

## Secuencias de varios planos

Para controlar manualmente varias imágenes dentro del mismo bloque, se puede
usar `call cinematic_begin` una vez, cambiar escenas y terminar siempre con
`call cinematic_end`. No debe abandonarse el bloque con `jump` antes del final,
porque la restauración de la interfaz quedaría pendiente.

## Estado y guardado

`cinematic_mode_active` indica si el modo está activo. La restauración del menú
usa una pila declarada con `default`, por lo que admite rollback, guardado y
llamadas cinematográficas anidadas sin fijar permanentemente `quick_menu`.
