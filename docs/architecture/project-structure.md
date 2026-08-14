# Estructura del proyecto

## Directorios principales

| Ruta | Responsabilidad |
| --- | --- |
| `game/assets/` | Imágenes, audio, fuentes y recursos visuales. |
| `game/data/` | Declaraciones de personajes, fondos y audio. |
| `game/engine/` | Motor visual y utilidades de escena. |
| `game/story/` | Guion narrativo y pruebas manuales. |
| `game/systems/` | Lógica reutilizable independiente de una pantalla. |
| `game/ui/` | Screens, estilos, componentes y temas de interfaz. |
| `game/tl/` | Traducciones administradas por Ren'Py. |
| `docs/` | Arquitectura, referencias y guías de ampliación. |

## Regla de dependencias

La historia puede utilizar sistemas y datos, pero los sistemas no deben
depender de capítulos concretos. La interfaz puede leer el estado del juego,
pero la lógica narrativa no debe contener medidas, colores o rutas de recursos
propias de una pantalla.

Ejemplo: el guion escribe `k "Hola"`; la identidad visual de Kuki se resuelve en
el registro de temas y no en el capítulo.

## Estado guardable

Las variables que cambien durante la partida deben declararse con `default`.
Las constantes visuales y funciones de construcción se crean durante `init` o
con `define`. Esto permite que Ren'Py gestione guardado, carga y rollback.
