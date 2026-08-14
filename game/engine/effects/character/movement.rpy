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

