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


transform flotar:

    block:

        easein 1.5 yoffset -15
        easeout 1.5 yoffset 15

        repeat

