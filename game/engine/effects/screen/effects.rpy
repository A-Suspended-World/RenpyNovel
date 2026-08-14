#=========================================================
# VN ENGINE
# EFECTOS ATL
#=========================================================

transform aparecer_expresion:

    alpha 0.0

    ease .12 alpha 1.0

#---------------------------------------------------------
# RESPIRACIÓN
#---------------------------------------------------------

transform respirar:

    block:

        easein 2.0 yoffset -4
        easeout .3 yoffset -4

        easeout 2.2 yoffset 0
        easein .3 yoffset 0

        repeat

transform respirar_suave:

    block:

        easein 2.5 yoffset -3
        ease 0.8 yoffset -2

        easeout 2.8 yoffset 0

        pause .5

        repeat

transform respirar_anime:

    block:

        easein 1.8 yoffset -5
        easeout 1.8 yoffset 0

        pause .4

        repeat
transform respirar_minima:

    block:

        easein 3.0 yoffset -2
        easeout 3.0 yoffset 0

        repeat
#---------------------------------------------------------
# ASENTIR (SI)
#---------------------------------------------------------

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


#---------------------------------------------------------
# FANTASMA
#---------------------------------------------------------

transform aparecer_fantasma:

    alpha 0.0

    easein 1.0 alpha .8


#---------------------------------------------------------
# PARPADEO DE LUZ
#---------------------------------------------------------

transform parpadeo_luz:

    block:

        alpha 1.0

        choice:

            .2

        choice:

            .5

        alpha .6

        .05

        repeat


#---------------------------------------------------------
# ENFOCADO
#---------------------------------------------------------

transform enfocado:

    matrixcolor BrightnessMatrix(0.0)

    easein .2 matrixcolor BrightnessMatrix(0.0)


#---------------------------------------------------------
# DESENFOCADO
#---------------------------------------------------------

transform desenfocado:

    easein .2 matrixcolor BrightnessMatrix(-0.25)


#---------------------------------------------------------
# SACUDIDA DE PANTALLA
#---------------------------------------------------------

transform sacudida_pantalla:

    xoffset 0
    yoffset 0

    easein .03 xoffset 12 yoffset -8
    easein .03 xoffset -10 yoffset 10
    easein .03 xoffset 8 yoffset -12
    easein .03 xoffset -12 yoffset 6
    easein .03 xoffset 6 yoffset -4
    easein .03 xoffset 0 yoffset 0