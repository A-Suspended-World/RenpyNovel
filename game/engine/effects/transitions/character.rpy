##############################################################################
# ENTRADAS
##############################################################################

# ---------- IZQUIERDA ----------

transform entrar_izquierda:

    xoffset -800
    alpha 0.0

    ease .35:
        xoffset 0
        alpha 1.0


transform entrar_derecha:

    xoffset 800
    alpha 0.0

    ease .35:
        xoffset 0
        alpha 1.0

##############################################################################
# SALIDAS
##############################################################################

transform exit_left:

    linear 0.35 xpos -0.35 alpha 0.0


transform exit_right:

    linear 0.35 xpos 1.35 alpha 0.0