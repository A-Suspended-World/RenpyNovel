
# Define personajes:
define e = Character("Eileen")
define prota = Character("Yuu", color="#FCFCFC")
define tv = Character("TV")

# Define texto
define config.default_text_cps = 40

# Define flags:
default abre = False


# El juego comienza en label start:

label start:

    jump capitulo1

#label start:

    # Capítulo 0 — Pesadilla
    centered "{size=40}Capítulo 0 — Pesadilla{/size}"

    scene fn

    "..."

    play sound "Despertador Efecto De Sonido.mp3" loop volume 0.2
    $ renpy.music.set_volume(1.0, delay=2.0, channel="sound")


    "Ring Ring Ring"

    "Un sonido leve se oye de fondo"

    "RING RING RING"

    "Un sonido familiar"

    stop sound

    play sound "Despertador Efecto De Sonido.mp3"

    "Muy irritante..."

    "Extendí mi brazo para poder apaciguar el ruido, pero..."

    "no lo alcanzaba"

    stop sound

    menu:
        "Abrir los ojos":
            $ abre = True
            jump terminar

        "Seguir durmiendo":
            $ abre = False
            jump terminar
    return
 
label terminar:



    if abre:
        "Hay mucha luz"
    else:
        "Intenté seguir durmiendo, pero algo no estaba bien..."

    "comencé a abrir los ojos gradualmente mientras la luz se colaba por las aberturas de mis ojos"

    scene fnw

    scene pesadilla

    "¡¿Qué es este lugar?! tan brillante...."
    "a mi alrededor yacía un campo extenso y completamente vacío"
    "mientras examinaba mi alrededor salto ante mi un peculiar detalle"
    "levante ambos brazos y los inspeccione"
    scene fnh
    "¿se encogieron o es mi imaginación.....?"

    "..." 

    "Intente tocar mi rostro"

    "mi rostro ahora es....mas esponjoso..."

    "Ya lo entendia"

    "me habia encogido"

    "RING RING RING"

    play sound "Despertador Efecto De Sonido.mp3"
    
    "ahora, el sonido se hacia cada vez mas fuerte"
    scene pesadilla

    hide fnh

   

    "Viene de esa dirección..."

    play sound "Despertador Efecto De Sonido.mp3" loop
    play music "Despertador Efecto De Sonido.mp3" loop volume 0.8

    stop sound
    stop music

    "En esa dirección se alcanzaba a ver algo rectangular"

    scene bg_tv

    tv "ZZZHZHHFFFFFFFFFF"

    "Que hace una pantalla aqui?"

    tv "HHHHRRRRRZZZHZHHFFFFFFFFFF"

    "Intente asercarme mas a aquella pantalla"

    tv "HHHHRRRRRZZZ.........."

    "La pantalla parecia estar sintonizando algo"

    show Clara
    tv ".............."
    
  

    "Una mujer se mostro por un segundo, atravez de la pantalla"
    hide Clara
    "Luego se desvanecio"

    tv "D#t1SDWAd"

    "Escuchaba un ruido salir de aquella pantalla"

    tv "DDet31wqdawsd"

    "trataba de comunicarse"

    tv "Detras de ti...."

    show Silueta Negra

    "Una sombra se mostro ante ti"

    "No me podia mover"

    "Es aterradora..."

    "Senti como mi conciencia empesaba a desbanecerse"

    "Hola{w=}... ¿sigues ahí?{w=} .... Te esto viendo"

    "{nw}letra por letra sin un auto skip"

    "Esto es {b}negrita{/b}"
    "Esto es {i}cursiva{/i}"
    "Esto es {u}subrayado{/u}"
    "Esto es {color=#f00}rojo{/color}"
    "Texto {size=+10}grande{/size}"















    "Este es el final"

    return
