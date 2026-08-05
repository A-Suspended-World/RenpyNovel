#=========================================================
# VN ENGINE
# SISTEMA DE PERSONAJES
#=========================================================

init -90 python:

    class VNCharacterSystem:

        def __init__(self):

            self.planos = {

                PLANO_COMPLETO: {

                    "zoom": 0.85,

                    "ypos": 1.00,

                    "sprite_type": SPRITE_FULL,

                },

                PLANO_MEDIO: {

                    "zoom": 1.30,

                    "ypos": 1.50,

                    "sprite_type": SPRITE_FULL,

                },

                PLANO_CERCANO: {

                    "zoom": 1.70,

                    "ypos": 1.85,

                    "sprite_type": SPRITE_FULL,

                }

            }


        def build(self, posicion, plano):

            datos = self.planos[plano]

            return Transform(

                reset=True,

                xpos=posicion,

                ypos=datos["ypos"],

                xanchor=0.5,

                yanchor=1.0,

                zoom=datos["zoom"]

            )


    vn_character = VNCharacterSystem()


    def personaje(posicion, plano):

        return vn_character.build(posicion, plano)

#----------------------------------------------------------
# ENTRAR DESDE LA IZQUIERDA
#----------------------------------------------------------

transform entrar_izq(posicion, plano):

    xpos -0.30

    contains:

        personaje(posicion, plano)

    ease .40 xpos posicion


#----------------------------------------------------------
# ENTRAR DESDE LA DERECHA
#----------------------------------------------------------

transform entrar_der(posicion, plano):

    xpos 1.30

    contains:

        personaje(posicion, plano)

    ease .40 xpos posicion