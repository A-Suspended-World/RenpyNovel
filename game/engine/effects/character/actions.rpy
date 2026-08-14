#=========================================================
# VN ENGINE
# ACCIONES DE PERSONAJE
#=========================================================


#---------------------------------------------------------
# 1. ESCAPAR HACIA LA DERECHA
#---------------------------------------------------------
# El personaje sale corriendo rápidamente hacia la derecha.
#
# Secuencia:
#   1. Pequeño impulso inicial.
#   2. Aceleración.
#   3. Carrera rápida.
#   4. Sale completamente de pantalla.
#
# Ideal para:
# - Escenas cómicas
# - Personaje huyendo
# - Salidas repentinas
#
# NOTA:
# Este ALT mueve la posición completa del personaje.
# Está pensado para terminar fuera de pantalla.
#---------------------------------------------------------

transform escapar_derecha:

    easein .08 xoffset 20

    easein .18 xoffset 80

    linear .35 xoffset 500

    linear .35 xpos 1.35


#---------------------------------------------------------
# 2. ESCAPAR HACIA LA IZQUIERDA
#---------------------------------------------------------
# Igual que escapar_derecha, pero hacia el lado contrario.
#
# Secuencia:
#   1. Pequeño impulso.
#   2. Aceleración.
#   3. Carrera rápida.
#   4. Sale completamente de pantalla.
#
# Ideal para:
# - Escapes cómicos
# - Salidas repentinas
# - Personajes huyendo
#---------------------------------------------------------

transform escapar_izquierda:

    easein .08 xoffset -20

    easein .18 xoffset -80

    linear .35 xoffset -500

    linear .35 xpos -0.35


#---------------------------------------------------------
# CAMINAR ENTRANDO DESDE LA IZQUIERDA
#---------------------------------------------------------
# El personaje entra caminando desde fuera de pantalla.
#
# Cada paso:
#   - avanza hacia la derecha
#   - hace un pequeño movimiento vertical
#   - recupera su posición
#
# A diferencia de la prueba anterior, aquí NO usamos
# xoffset para volver al mismo punto.
#
# La posición horizontal avanza progresivamente mediante
# xpos.
#---------------------------------------------------------

transform espiar_entrada_izquierda:

    # Posición inicial: fuera de pantalla
    xpos -0.25

    # PASO 1
    parallel:
        easein .20 xpos 0.00

    parallel:
        easein .10 yoffset -4
        easeout .10 yoffset 0

    pause .10


    # PASO 2
    parallel:
        easein .20 xpos 0.08

    parallel:
        easein .10 yoffset -4
        easeout .10 yoffset 0

    pause .10


    # PASO 3
    parallel:
        easein .20 xpos 0.16

    parallel:
        easein .10 yoffset -4
        easeout .10 yoffset 0

    pause .10


    # PASO 4
    parallel:
        easein .20 xpos 0.24

    parallel:
        easein .10 yoffset -4
        easeout .10 yoffset 0


    # Posición final
    yoffset 0


    #---------------------------------------------------------
# ENTRAR CAMINANDO DESDE LA IZQUIERDA
#---------------------------------------------------------
# El personaje entra caminando desde fuera de pantalla
# y termina en la posición IZQUIERDA de la escena.
#
# Movimiento de cada paso:
#
#       sube ligeramente
#            ↓
#       baja un poco más rápido
#            ↓
#       siguiente paso
#
# La posición horizontal SIEMPRE avanza.
#
# Al terminar:
#       xpos 0.00
#
# Esto está pensado para que el personaje pueda
# quedarse en esta posición y posteriormente cambiar
# al sprite/pose normal de la posición izquierda.
#---------------------------------------------------------

#---------------------------------------------------------
# ENTRAR CAMINANDO DESDE LA IZQUIERDA
#---------------------------------------------------------
# El personaje entra desde fuera de pantalla y avanza
# continuamente hacia la derecha.
#
# Cada paso produce un pequeño movimiento vertical,
# pero el desplazamiento horizontal NUNCA retrocede.
#
# IMPORTANTE:
# Esta versión no fija una xpos final.
# El movimiento horizontal se realiza mediante xoffset,
# por lo que podemos comprobar primero el movimiento
# independientemente de las posiciones del SceneManager.
#---------------------------------------------------------

transform entrar_corriendo:

    xoffset -700
    yoffset 0


    #-----------------------------------------------------
    # PASO 1
    #-----------------------------------------------------

    parallel:

        easein .35 xoffset -560

    parallel:

        easein .14 yoffset -4
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 2
    #-----------------------------------------------------

    parallel:

        easein .35 xoffset -420

    parallel:

        easein .14 yoffset -4
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 3
    #-----------------------------------------------------

    parallel:

        easein .35 xoffset -280

    parallel:

        easein .14 yoffset -4
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 4
    #-----------------------------------------------------

    parallel:

        easein .35 xoffset -140

    parallel:

        easein .14 yoffset -4
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 5
    #-----------------------------------------------------

    parallel:

        easein .35 xoffset 0

    parallel:

        easein .14 yoffset -4
        easeout .08 yoffset 0


    yoffset 0

#---------------------------------------------------------
# ENTRAR CAMINANDO
#---------------------------------------------------------
# El personaje entra desde fuera de la pantalla por la
# izquierda y termina en la posición que ya tenía asignada.
#
# Movimiento:
#
#   avanza → levanta ligeramente el cuerpo → baja
#   avanza → levanta ligeramente el cuerpo → baja
#   avanza → levanta ligeramente el cuerpo → baja
#
# La animación es deliberadamente lenta y suave.
#
# Diferencia con "entrar_corriendo":
#
#   entrar_caminando = lento y tranquilo
#   entrar_corriendo = rápido y directo
#---------------------------------------------------------

transform entrar_caminando:

    #-----------------------------------------------------
    # POSICIÓN INICIAL
    #-----------------------------------------------------

    xoffset -700
    yoffset 0


    #-----------------------------------------------------
    # PASO 1
    #-----------------------------------------------------

    parallel:

        easein .48 xoffset -560

    parallel:

        easein .16 yoffset -9
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 2
    #-----------------------------------------------------

    parallel:

        easein .48 xoffset -420

    parallel:

        easein .16 yoffset -9
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 3
    #-----------------------------------------------------

    parallel:

        easein .48 xoffset -280

    parallel:

        easein .16 yoffset -9
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 4
    #-----------------------------------------------------

    parallel:

        easein .48 xoffset -140

    parallel:

        easein .16 yoffset -9
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # PASO 5
    #-----------------------------------------------------

    parallel:

        easein .48 xoffset 0

    parallel:

        easein .16 yoffset -9
        easeout .08 yoffset 0


    #-----------------------------------------------------
    # ASEGURAR POSICIÓN FINAL
    #-----------------------------------------------------

    xoffset 0
    yoffset 0