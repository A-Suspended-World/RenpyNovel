transform asentir:

    easein .12 yoffset 15
    easeout .12 yoffset 0

    easein .10 yoffset 8
    easeout .10 yoffset 0


#---------------------------------------------------------
# NEGAR (NO)
#---------------------------------------------------------

transform negar:

    easein .08 xoffset -12
    easeout .08 xoffset 12

    easein .08 xoffset -8
    easeout .08 xoffset 8

    easein .08 xoffset 0

#=========================================================
# REACCIONES EMOCIONALES
#=========================================================


#---------------------------------------------------------
# 1. NERVIOSO
#---------------------------------------------------------
# Movimiento pequeño y rápido.
#
# Sensación:
# - Nervios
# - Inquietud
# - Ansiedad leve
# - Incertidumbre
#
# No debe sentirse como un temblor fuerte.
#---------------------------------------------------------

transform nervioso:

    easein .08 xoffset -3
    easeout .08 xoffset 3

    easein .07 xoffset -4
    easeout .07 xoffset 4

    easein .08 xoffset -3
    easeout .08 xoffset 3

    easein .10 xoffset 0


#---------------------------------------------------------
# 2. VERGÜENZA
#---------------------------------------------------------
# El personaje baja ligeramente y permanece un instante
# antes de volver lentamente a su posición.
#
# Sensación:
# - Vergüenza
# - Timidez
# - Incomodidad emocional
#
# Es deliberadamente sutil.
#---------------------------------------------------------

transform verguenza:

    easein .20 yoffset 8
    pause .15
    easeout .35 yoffset 0


#---------------------------------------------------------
# 3. ENOJO
#---------------------------------------------------------
# Pequeño movimiento brusco del cuerpo.
#
# Sensación:
# - Irritación
# - Enojo
# - Molestia
# - Impaciencia emocional
#
# Es una reacción corta, no un temblor continuo.
#---------------------------------------------------------

transform enojo:

    easein .06 xoffset -5
    easeout .06 xoffset 5

    easein .05 xoffset -4
    easeout .05 xoffset 4

    easein .08 xoffset 0


#---------------------------------------------------------
# 4. FRUSTRACIÓN
#---------------------------------------------------------
# El personaje cae ligeramente y después hace un pequeño
# rebote.
#
# Sensación:
# - Frustración
# - Decepción
# - Resignación
# - "Ugh..."
#---------------------------------------------------------

transform frustracion:

    easein .18 yoffset 10
    easeout .12 yoffset -3
    easeout .20 yoffset 0


#---------------------------------------------------------
# 5. MIEDO
#---------------------------------------------------------
# Temblor rápido e intenso, pero limitado.
#
# A diferencia de temblar_loop:
# este efecto termina automáticamente.
#
# Sensación:
# - Miedo
# - Terror leve
# - Nervios intensos
#---------------------------------------------------------

transform miedo:

    easein .05 xoffset -6
    easeout .05 xoffset 6

    easein .05 xoffset -7
    easeout .05 xoffset 7

    easein .05 xoffset -5
    easeout .05 xoffset 5

    easein .06 xoffset -4
    easeout .06 xoffset 4

    easein .08 xoffset 0


#---------------------------------------------------------
# 6. INCOMODIDAD
#---------------------------------------------------------
# Movimiento lateral lento y pequeño.
#
# Sensación:
# - Incomodidad
# - No saber qué hacer
# - Evitar una situación
# - Vergüenza social
#
# Debe sentirse diferente de "nervioso".
#---------------------------------------------------------

transform incomodidad:

    easein .25 xoffset -5
    easeout .30 xoffset 5

    easein .25 xoffset -4
    easeout .30 xoffset 4

    easeout .20 xoffset 0


#---------------------------------------------------------
# 7. ALEGRÍA
#---------------------------------------------------------
# Dos pequeños rebotes consecutivos.
#
# Sensación:
# - Alegría
# - Entusiasmo
# - Emoción
# - Felicidad
#
# Más energético que "rebote".
#---------------------------------------------------------

transform alegria:

    easein .10 yoffset -10
    easeout .14 yoffset 0

    easein .09 yoffset -7
    easeout .14 yoffset 0


#---------------------------------------------------------
# 8. CANSANCIO
#---------------------------------------------------------
# El personaje baja lentamente y después recupera
# su posición con suavidad.
#
# Sensación:
# - Cansancio
# - Agotamiento
# - Pesadez
# - Suspiro
#
# El movimiento es deliberadamente lento.
#---------------------------------------------------------

transform cansancio:

    easein 0.45 yoffset 10
    pause .20
    easeout .60 yoffset 0


#---------------------------------------------------------
# 9. IMPACIENCIA
#---------------------------------------------------------
# Pequeños movimientos verticales repetidos.
#
# Sensación:
# - Impaciencia
# - Querer que algo ocurra
# - Esperar demasiado
# - Irritación leve
#
# Es más rítmico que "nervioso".
#---------------------------------------------------------

transform impaciencia:

    easein .08 yoffset -4
    easeout .08 yoffset 0

    easein .08 yoffset -4
    easeout .08 yoffset 0

    easein .08 yoffset -5
    easeout .08 yoffset 0

    easein .10 yoffset 0


#---------------------------------------------------------
# 10. SUSTO
#---------------------------------------------------------
# Reacción instantánea.
#
# El personaje se desplaza rápidamente hacia arriba
# y vuelve inmediatamente.
#
# Diferencia:
#
# susto  = reacción instantánea
# miedo  = temblor prolongado
#
#---------------------------------------------------------

transform susto:

    easein .05 yoffset -15
    easeout .12 yoffset 0