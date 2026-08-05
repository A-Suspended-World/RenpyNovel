#=========================================================
# VN ENGINE
# SCENE MANAGER
#=========================================================

init -80 python:

    import renpy.exports as renpy


    class SceneManager:

        def __init__(self):

            self.characters = {}

        def pose(self, posicion, plano):

            return personaje(posicion, plano)
        #--------------------------------------------------
        # REGISTRO
        #--------------------------------------------------

        def register(self, nombre):

            if nombre not in self.characters:

                self.characters[nombre] = {

                    "visible": False,
                    "posicion": None,
                    "plano": None,
                    "estado": None,
                    "expresion": None,

                }


        #--------------------------------------------------
        # MOSTRAR PERSONAJE
        #--------------------------------------------------
        # Los efectos ATL van en at_list.
        # Las transiciones (dissolve, fade...) se ejecutan aparte
        # mediante with_statement().
        def show(
                self,
                image_name,
                posicion,
                plano,
                *effects,
                transition=None):

            #--------------------------------------------------
            # Reinicia el displayable si ya existe.
            #--------------------------------------------------

            if renpy.showing(image_name):
                renpy.hide(image_name)

            at_list = [ personaje(posicion, plano) ]

            at_list.extend(effects)

            renpy.show(
                image_name,
                at_list=at_list
            )

            if transition:
                renpy.with_statement(transition)

            if image_name in self.characters:
                
                self.characters[image_name]["visible"] = True
                self.characters[image_name]["posicion"] = posicion
                self.characters[image_name]["plano"] = plano
                self.characters[image_name]["expresion"] = image_name
                


        #--------------------------------------------------
        # OCULTAR
        #--------------------------------------------------

        def hide(self,
                image_name,
                transition=None):

            renpy.hide(image_name)

            if transition:

                renpy.with_statement(transition)

            if image_name in self.characters:

                self.characters[image_name]["visible"] = False


        def expression(
            self,
            old_image,
            new_image,
            transition=None
        ):

            datos = self.characters.get(old_image)

            if not datos:
                return


            posicion = datos["posicion"]
            plano = datos["plano"]


            self.show(
                new_image,
                posicion,
                plano,
                transition
            )


            self.hide(old_image)


        #--------------------------------------------------
        # INFORMACIÓN
        #--------------------------------------------------

        def exists(self, nombre):

            return nombre in self.characters


        def get(self, nombre):

            return self.characters.get(nombre)


    escena = SceneManager()