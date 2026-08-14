## Manual UI smoke test used by the developer test launcher.
label test_ui:

    $ quick_menu = False
    call screen preferences
    $ quick_menu = True
    jump test_launcher


label test_ui_menu_shell:

    $ quick_menu = False
    call screen extras
    $ quick_menu = True
    jump test_launcher


label test_ui_file_slots:

    $ quick_menu = False
    call screen save
    $ quick_menu = True
    jump test_launcher


label test_dialogue_ui:

    scene bg classroom

    narrator "Prueba del narrador y del color de cuerpo compartido."
    y "Soy Yuu. Mi identidad visual utiliza un acento cian."
    k "Soy Kuki. Mi identidad utiliza rosa y el texto aparece progresivamente."
    a "Soy Alice. Este es el tema violeta azulado."
    prof "Los títulos también pueden traducirse al cambiar de idioma."
    k "Una señal comienza a {shader=jitter:0.7,2.0}fallar{/shader}."

    jump test_launcher
