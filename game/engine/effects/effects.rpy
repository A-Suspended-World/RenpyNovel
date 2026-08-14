#=========================================================
# VN ENGINE
# EFECTOS ATL
#=========================================================



#---------------------------------------------------------
# ASENTIR (SI)
#---------------------------------------------------------

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