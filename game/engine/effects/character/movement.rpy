#---------------------------------------------------------
# TEMBLAR
#---------------------------------------------------------

transform mover_suave:

    ease .20 xoffset -6
    ease .20 xoffset 6
    ease .20 xoffset -5
    ease .20 xoffset 5
    ease .20 xoffset -3
    ease .20 xoffset 3
    ease .20 xoffset 0

transform mover_suave_fuerte:

    easein .15 xoffset -8
    easeout .15 xoffset 8
    easein .15 xoffset -7
    easeout .15 xoffset 7
    easein .15 xoffset -5
    easeout .15 xoffset 0

transform mover_muy_fuerte:

    easein .15 xoffset -14
    easeout .15 xoffset 14
    easein .15 xoffset -10
    easeout .15 xoffset 10
    easein .15 xoffset -8
    easeout .15 xoffset 0

transform temblar_loop:

    block:

        easein .04 xoffset 2
        easeout .04 xoffset -2

        repeat

transform temblor_leve:

    easein .05 xoffset 4
    easeout .05 xoffset -4

    easein .05 xoffset 3
    easeout .05 xoffset -3

    easein .05 xoffset 0

transform temblor_fuerte:

    block:

        easein .04 xoffset 5
        easeout .04 xoffset -5

        repeat 8
#---------------------------------------------------------
# BRINCO
#---------------------------------------------------------

transform brinco:

    easein .10 yoffset -35
    easeout .15 yoffset 0


#---------------------------------------------------------
# SACUDIDA
#---------------------------------------------------------

transform sacudida:

    xoffset 0
    yoffset 0

    easein .03 xoffset 15 yoffset -10
    easein .03 xoffset -12 yoffset 12
    easein .03 xoffset 10 yoffset -15
    easein .03 xoffset -15 yoffset 8
    easein .03 xoffset 8 yoffset -5
    easein .03 xoffset 0 yoffset 0


#---------------------------------------------------------
# FLOTAR
#---------------------------------------------------------
transform flotar:

    block:

        easein 1.5 yoffset -15
        easeout 1.5 yoffset 15

        repeat

#=========================================================
# MOVIMIENTOS Y REACCIONES
#=========================================================



#---------------------------------------------------------
# 2. RETROCEDER
#---------------------------------------------------------
# El personaje se mueve ligeramente hacia atrás
# y recupera su posición.
#
# Útil para:
# - Sorpresa
# - Miedo leve
# - Incomodidad
# - Reacción ante algo inesperado
#
# El movimiento es corto para que no parezca una
# salida del personaje de su posición.
#---------------------------------------------------------

transform sobresalto_leve:

    easein .12 yoffset -18
    easeout .20 yoffset 0


#---------------------------------------------------------
# 3. ACERCARSE
#---------------------------------------------------------
# El personaje se inclina/mueve ligeramente hacia
# delante y vuelve.
#
# Útil para:
# - Interés
# - Curiosidad
# - Escuchar mejor
# - Confidencia
# - Atención
#
# Al usar yoffset, el movimiento es muy pequeño.
#---------------------------------------------------------

transform acercarse:

    easein .15 yoffset 12
    easeout .25 yoffset 0



#---------------------------------------------------------
# 6. SACUDIRSE
#---------------------------------------------------------
# Movimiento corto de izquierda a derecha.
#
# NO es un temblor continuo.
#
# Es una reacción única y rápida.
#
# Útil para:
# - Recuperarse después de un susto
# - Quitarse algo de encima
# - Reacción física
# - "¡No, no!"
# - Sacudirse después de estar incómodo
#---------------------------------------------------------

transform sacudirse:

    easein .07 xoffset -8
    easeout .07 xoffset 8

    easein .06 xoffset -6
    easeout .06 xoffset 6

    easein .05 xoffset 0


#---------------------------------------------------------
# 7. REBOTE
#---------------------------------------------------------
# Pequeño salto vertical muy suave.
#
# Es considerablemente más pequeño que "brinco".
#
# Útil para:
# - Alegría
# - Entusiasmo
# - Energía
# - Reacción positiva
# - Personajes más expresivos
#---------------------------------------------------------

transform rebote:

    easein .10 yoffset -12
    easeout .16 yoffset 0


#---------------------------------------------------------
# 8. ZOOM DE REACCIÓN
#---------------------------------------------------------
# Pequeño acercamiento visual mediante zoom.
#
# El personaje aumenta ligeramente de tamaño
# y vuelve a la normalidad.
#
# Útil para:
# - Sorpresa
# - Énfasis
# - Reacción dramática
# - Momento importante
#
# Es deliberadamente muy pequeño para evitar
# que parezca un cambio de plano.
#---------------------------------------------------------

transform reaccion_zoom:

    easein .12 zoom 1.03
    easeout .20 zoom 1.0




#---------------------------------------------------------
# 10. RISA / SACUDIDA DE HOMBROS
#---------------------------------------------------------
# Pequeña vibración horizontal limitada.
#
# NO es "temblar".
#
# La intención es simular el movimiento del cuerpo
# producido por una risa.
#
# Útil para:
# - Risa
# - Risa contenida
# - Nervios
# - Vergüenza
# - Carcajada ligera
#
# La animación termina sola.
#---------------------------------------------------------

transform risa:

    easein .07 xoffset -3
    easeout .07 xoffset 3

    easein .07 xoffset -3
    easeout .07 xoffset 3

    easein .06 xoffset -2
    easeout .06 xoffset 2

    easein .06 xoffset 0

