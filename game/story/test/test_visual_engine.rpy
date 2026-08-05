label test_visual_engine:

    scene bg entrance
    with fade

    "===== VISUAL ENGINE STRESS TEST ====="

    ####################################################
    # APARICIÓN
    ####################################################

    $ escena.show(
        "kuki_idle",
        POS_CEN,
        PLANO_MEDIO,
        entrar_izquierda,
        respirar
    )

    "Entrada."

    ####################################################
    # CAMBIOS DE EXPRESIÓN
    ####################################################

    $ escena.hide("kuki_idle", transition=dissolve)

    $ escena.show(
        "kuki_smile",
        POS_CEN,
        PLANO_MEDIO,
        respirar,
        transition=dissolve
    )

    "Smile."

    $ escena.hide("kuki_smile", transition=dissolve)

    $ escena.show(
        "kuki_happy",
        POS_CEN,
        PLANO_MEDIO,
        respirar,
        transition=dissolve
    )

    "Happy."

    $ escena.hide("kuki_happy", transition=dissolve)

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        respirar,
        transition=dissolve
    )

    "Confused."

    ####################################################
    # EFECTOS ATL
    ####################################################

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        asentir
    )

    "Asiente."

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        negar
    )

    "Niega."

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        brinco
    )

    "Brinca."

    ####################################################
    # CAMBIO DE POSICIÓN
    ####################################################

    $ escena.show(
        "kuki_confused",
        POS_IZQ,
        PLANO_MEDIO,
        respirar
    )

    "Izquierda."

    $ escena.show(
        "kuki_confused",
        POS_DER,
        PLANO_MEDIO,
        respirar
    )

    "Derecha."

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        respirar
    )

    "Centro."

    ####################################################
    # CAMBIO DE PLANO
    ####################################################

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_COMPLETO,
        respirar
    )

    "Plano completo."

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_CERCANO,
        respirar
    )

    "Plano cercano."

    $ escena.show(
        "kuki_confused",
        POS_CEN,
        PLANO_MEDIO,
        respirar
    )

    "Plano medio."

    ####################################################
    # CAMBIO DE ESCENARIO
    ####################################################

    scene bg classroom
    with dissolve

    "Classroom."

    ####################################################
    # NUEVA EXPRESIÓN
    ####################################################

    $ escena.hide("kuki_confused", transition=dissolve)

    $ escena.show(
        "kuki_teasing",
        POS_CEN,
        PLANO_MEDIO,
        respirar,
        transition=dissolve
    )

    "Teasing."

    ####################################################
    # MIRADAS
    ####################################################

    $ escena.hide("kuki_teasing", transition=dissolve)

    $ escena.show(
        "kuki_teasing_looking_right",
        POS_CEN,
        PLANO_MEDIO,
        respirar,
        transition=dissolve
    )

    "Looking."

    ####################################################
    # ENFOQUE
    ####################################################

    $ escena.show(
        "kuki_teasing_looking_right",
        POS_CEN,
        PLANO_MEDIO,
        enfocado
    )

    "Focused."

    ####################################################
    # SACUDIDA
    ####################################################

    camera at sacudida_pantalla

    "Shake."

    ####################################################
    # FONDO
    ####################################################

    scene bg laboratory
    with fade

    "Laboratory."

    ####################################################
    # REAPARECER
    ####################################################

    $ escena.hide("kuki_teasing_looking_right")

    $ escena.show(
        "kuki_serious",
        POS_DER,
        PLANO_MEDIO,
        entrar_derecha,
        respirar
    )

    "Serious."

    ####################################################
    # CAMBIOS RÁPIDOS
    ####################################################

    $ escena.hide("kuki_serious", transition=dissolve)

    $ escena.show(
        "kuki_sad",
        POS_DER,
        PLANO_MEDIO,
        transition=dissolve
    )

    "Sad."

    $ escena.hide("kuki_sad", transition=dissolve)

    $ escena.show(
        "kuki_grin",
        POS_DER,
        PLANO_MEDIO,
        transition=dissolve
    )

    "Grin."

    $ escena.hide("kuki_grin", transition=dissolve)

    $ escena.show(
        "kuki_disgust",
        POS_DER,
        PLANO_MEDIO,
        transition=dissolve
    )

    "Disgust."

    ####################################################
    # LIMPIEZA
    ####################################################

    $ escena.hide("kuki_disgust", transition=dissolve)

    ####################################################
    # TEST CAMBIO DE EXPRESIÓN
    ####################################################

    scene bg classroom
    with dissolve

    $ escena.show(
    "kuki_idle",
    POS_CEN,
    PLANO_MEDIO,
    respirar
    )

    "Expresión inicial."

    $ escena.show(
    "kuki_smile",
    POS_CEN,
    PLANO_MEDIO,
    respirar,
    transition=dissolve
    )

    "Idle → Smile"

    $ escena.show(
    "kuki_thinking",
    POS_CEN,
    PLANO_MEDIO,
    respirar,
    transition=dissolve
    )

    "Smile → Thinking"

    $ escena.show(
    "kuki_confused",
    POS_CEN,
    PLANO_MEDIO,
    respirar,
    transition=dissolve
    )

    "Thinking → Confused"

    $ escena.show(
    "kuki_happy",
    POS_CEN,
    PLANO_MEDIO,
    respirar,
    transition=dissolve
    )

    "Confused → Happy"

    $ escena.show(
    "kuki_serious",
    POS_CEN,
    PLANO_MEDIO,
    respirar,
    transition=dissolve
    )

    "Happy → Serious"

    return