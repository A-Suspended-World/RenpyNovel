label part_05:

    stop music

    play music BGM_INTRO

    "Aprovechando el momento justo cuando ella se dio la vuelta"

    "Me escabulli entre los pasillos"

    y "Creo que la escuche decir algo mas"

    y "Bueno, no importa, viniendo de ella, no debe ser nada importante"

    "Mientras caminaba si rumbo por los pasillos"
    
    "A lo lejos vi una maquina"

    y" ¡OH!, Justamente lo que necesitaba"

    "Me dirigi donde la maquina"

    "Frente a mi habia una gran caja, con una pantalla negra que cubria la mayor parte"

    $ escena.show (
        "dispensador_machine_off",
        POS_CEN,
        PLANO_COMPLETO,
        transition = dissolve
    )

    "Pase mi mano frente a la maquina"

    $ escena.hide("dispensador_machine_off")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        transition = dissolve
    )

    "Esta de inmediato se encendio"

    "Entre las imagenes que me mostraba, habian representaciones simplificas de frutas"

    label escena_fresa:

    "Coloque mi dedo sobre un icono muy parecido a una fresa"

label bucle_eleccion:

    "De inmediato la maquina me pidio que eligiera entre dos opciones"

    menu:
        "Confirmar pedido":
            jump pedido_confirmado

        "Declinar pedido":
            "Pero estoy sediento..."
            jump bucle_eleccion

label pedido_confirmado:

    # Colocar sonido.

    play sound SFX_allowing

    "La máquina emitió un sonido"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        temblar_loop,
        transition = dissolve,
    )
    "Luego comenzo a agitarse un poco"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        brinco
    )

    play sound SFX_CRACK

    "De inmediato un sonido salio de la misma maquina."

    "Habia una lata gris en el compartimiento"

    "Tome la lata y la abri."

    "Verti su contenido en mi boca"

    "Empece saboreaba el refrescante jugo de freza"

    "Termine de inclinar la lata para dejar que todo el liquitodo callera en mi boca."

    "No podía evitar soltar un suspiro cada vez que tomaba una."

    "Posteriormente la tire una compuerta especial de la misma maquina."

    y"Creo que ya deberia volver..."

    y"Solamente espero no econtrarme a cierta persona de camino"

    y "Aun que..."

    "Ya que estoy aquí, una soda mas no haria"

    y"Creo que aun tengo algunos puntos..."

    "Saque mi celular del bolsillo y comprobabe el saldo disponible."

    y "Menos mal"

    "Justamente me alcanza para una mas"
    
    y"veamos cual sera esta vez...."

    "Hasta ahora ya habia probado todos los sabores disponibles"
    
    "Realmente deberian ampliar el repertorio de sodas."

    "..."

    "Que raro...estoy casi segurio de que eso no estaba alli antes"

    "Un nuevo icono habia aperecio en la pantalla"

    y "Tampoco reconozco el nombre de esta bebida."

    "Bebida hidratante de MORA"

    y "Esto es muy sospechoso"

    "Mientras decia eso mi mano ya estaba sobre aquel icono"

    "La tentacion de averiguar el sabor era mayor"

    "Supongo que probare este."

    "Antes de confirmar, decidi mirar el precio de la bebida...."

    "Veamos...aqui esta, cuesta.....¡¡...!!"

    "Quede paralizado luego de ver lo que estaba frente a mi"

    "70000000000 Millones de puntos"

    "¿Eso si quiera es posible?"

    "De inmediato aparte bruscamente la mano."

    "¡¡Esa cantidad es absudamente cara!!"

    "Trate de calmarme"

    y"Menos mal, la maquina pedía la confirmación del usuario antes de ejecutar un pedido"
    
    "Me salve de cometer el peor error de mi vida."

    "Esta vez me asegure de cancelar el pedido"

    menu:
        "Confirmar pedido":
            play sound SFX_allowing
            "Alistando pedido"
            

        "Declinar pedido":
            play sound SFX_allowing
            "Alistando pedido"
    
    "...."
    
    y "¿Ese sonido acaso es...?"

    "No, no puede ser, estoy seguro de haber cancelado..."

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida
    )

    "Antes de que siquiera pudiera hacer algo"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida
    )

    "La maquina empezo a moverse de forma rara"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida
    )

    "¡¡...!!"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida
    )

    "Que rayos?"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida
    )

    "Esta averiada?"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        sacudida_loop
    )

    "Ahora no paraba de temblar"

    "Esto no se ve bien..."

    "Cuando las sacudidas se volvieron mas bruscas, instintivamente me cubir con mis manos"

    "Entonces..."

    "No paso nada"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO
    )

    "La maquina se calmo"

    "....¿Eso es todo....?"

    "Por alguna extraña razon, la maquina dejo de sacudirse"

    "...¿No vas a explotar o si?"

    $ escena.hide("dispensador_machine_on")

    $ escena.show (
        "dispensador_machine_on",
        POS_CEN,
        PLANO_COMPLETO,
        brinco
    )

    play sound SFX_CRACK

    "HIIII"

    $ escena.hide("dispensador_machine_on", transition = dissolve)

    "Otra vez estaba cubriendome con ambas manos"

    "....."

    "Je..je..je..."

    "Solo era el sonido de la lata cayendo"

    "'Cayendo'"

    "Comprobe lo que habia soltado la maquina"

    

    $ escena.show (
        "purple_soda",
        POS_CEN,
        PLANO_COMPLETO,
        transition = dissolve
    )

    "En mis manos ahora tenia una lata que nunca antes vista"

    "Esta tenia color"

    $ escena.hide("purple_soda", transition = dissolve)

    "Espera...."

    "NO ME DIGAS"

    "De inmediato saque mi celular"

    "Con una mano tembloro intente revisar saldo"

    "Mientras me imaginaba los números negativos en mi cuenta"

    "La sorpresa que me lleve"

    "Cuando vi mi saldo intacto"

    "¿Ningún cambio?, es mas, esta igual que hace un momento."

    "Obviamente era un error, no se porque me preocupe...."

   
    ## Establishing shot: the textbox and quick menu remain hidden while the
    ## academy lobby fills the screen, then return for the next line.
    call cinematic_still("bg academy_lobby", duration=3.5)

    "La luz de la tarde atravesaba el vestíbulo de la academia."

jump part_06
#jump parte_01_chapter_02
