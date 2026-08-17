# Agregar una escena cinematográfica

## 1. Guardar el recurso

Coloca el fondo en la categoría correspondiente dentro de
`game/assets/backgrounds/`. Para la academia:

```text
game/assets/backgrounds/academy/nombre_del_fondo.png
```

El formato recomendado es `1920x1080` y relación `16:9`. El sistema escala
recursos de otras medidas a la resolución del proyecto, aunque una fuente más
pequeña puede perder nitidez.

## 2. Registrar la imagen

En `game/data/definitions/bg_images.rpy`:

```renpy
image bg nombre_del_fondo = "assets/backgrounds/academy/nombre_del_fondo.png"
```

## 3. Usarla en el capítulo

```renpy
call cinematic_still("bg nombre_del_fondo", duration=3.0)
```

No es necesario cambiar `quick_menu`, llamar `window hide` ni restaurar el
textbox manualmente. El sistema concentra esas responsabilidades para evitar
que una escena deje la interfaz oculta por accidente.

## 4. Probar

Ejecuta `test_launcher` y selecciona **Escena cinematográfica**. Comprueba que:

- el textbox desaparezca durante el plano;
- no aparezca el menú rápido;
- la imagen cubra la pantalla;
- ambos elementos regresen en el siguiente diálogo.
