# Funciones y dependencias de Ren'Py

## Versión objetivo

El proyecto se desarrolla y valida actualmente con Ren'Py 8.5.3.

## Funciones utilizadas

| Función | Uso en el proyecto |
| --- | --- |
| Screen Language | Diálogo, menús, preferencias y slots. |
| `Character` | Hablantes y propiedades visuales por personaje. |
| Character ID prefixes | Aplicación del color de acento al screen `say`. |
| Text shaders | Aparición progresiva y efectos emocionales. |
| `preferences.text_cps` | Velocidad configurable del texto. |
| Actions | Menú rápido y navegación. |
| Translation framework | Español base y traducción inglesa. |
| ATL transforms | Entrada del cuadro y movimiento reutilizable. |

## Librerías externas

Actualmente el sistema de diálogo no incorpora paquetes ni librerías de
terceros. Utiliza APIs incluidas en Ren'Py para reducir incompatibilidades con
guardado, rollback y distribuciones multiplataforma.

Antes de añadir una dependencia externa se debe registrar:

1. Repositorio y versión exacta.
2. Licencia y atribución requerida.
3. Plataformas compatibles.
4. Impacto sobre guardado y rollback.
5. Procedimiento de actualización o eliminación.
