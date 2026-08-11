################################################################################
## Extensible feature placeholders
################################################################################

screen menu_ui_feature_placeholder(title, description=menu_ui_placeholder_text):

    use game_menu(title):
        use menu_ui_empty_state(title, description)


screen gallery():
    tag menu
    use menu_ui_feature_placeholder(
        _("Galería"),
        _("Aquí se mostrarán ilustraciones, arte de personajes y escenas desbloqueadas."),
    )


screen music_room():
    tag menu
    use menu_ui_feature_placeholder(
        _("Sala de música"),
        _("Aquí se mostrarán las pistas desbloqueadas, sus controles y su información."),
    )


screen chapter_select():
    tag menu
    use menu_ui_feature_placeholder(
        _("Selección de capítulos"),
        _("Aquí se mostrarán los capítulos disponibles, su progreso y los puntos de inicio seguros."),
    )


screen achievements():
    tag menu
    use menu_ui_feature_placeholder(
        _("Logros"),
        _("Aquí se mostrarán el progreso, los hitos desbloqueados y los objetivos ocultos."),
    )
