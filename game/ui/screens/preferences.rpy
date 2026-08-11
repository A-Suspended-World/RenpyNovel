################################################################################
## Preferences
################################################################################

screen preferences():

    tag menu

    $ text_speed_label = _("Instantánea") if preferences.text_cps == 0 else str(int(preferences.text_cps))
    $ auto_forward_label = "{:.1f} s".format(preferences.afm_time)
    $ music_volume_label = "{}".format(int(preferences.get_volume("music") * 100))
    $ sound_volume_label = "{}".format(int(preferences.get_volume("sound") * 100))
    $ voice_volume_label = "{}".format(int(preferences.get_volume("voice") * 100))

    use menu_ui_background(menu_ui_preferences_background)
    use menu_ui_preferences_sidebar

    frame:
        style "menu_ui_preferences_content_panel"

        vbox:
            style "menu_ui_preferences_content"

            hbox:
                style "menu_ui_preferences_toggle_groups"

                vbox:
                    style "menu_ui_preferences_group"

                    label _("Pantalla"):
                        style "menu_ui_preferences_group_label"

                    textbutton _("Ventana"):
                        style "menu_ui_preferences_radio_button"
                        action Preference("display", "window")

                    textbutton _("Pantalla completa"):
                        style "menu_ui_preferences_radio_button"
                        action Preference("display", "fullscreen")

                vbox:
                    style "menu_ui_preferences_group"

                    label _("Saltar"):
                        style "menu_ui_preferences_group_label"

                    textbutton _("Texto no visto"):
                        style "menu_ui_preferences_check_button"
                        action Preference("skip", "toggle")

                    textbutton _("Después de elecciones"):
                        style "menu_ui_preferences_check_button"
                        action Preference("after choices", "toggle")

                    textbutton _("Transiciones"):
                        style "menu_ui_preferences_check_button"
                        action InvertSelected(Preference("transitions", "toggle"))

            hbox:
                style "menu_ui_preferences_slider_columns"

                vbox:
                    style "menu_ui_preferences_slider_column"

                    use menu_ui_preferences_slider(
                        _("Velocidad de texto"),
                        text_speed_label,
                        Preference("text speed"),
                        "A",
                    )

                    use menu_ui_preferences_slider(
                        _("Tiempo de autoavance"),
                        auto_forward_label,
                        Preference("auto-forward time"),
                        ">>",
                    )

                vbox:
                    style "menu_ui_preferences_slider_column"

                    if config.has_music:
                        use menu_ui_preferences_slider(
                            _("Volumen de música"),
                            music_volume_label,
                            Preference("music volume"),
                            "♫",
                        )

                    if config.has_sound:
                        use menu_ui_preferences_slider(
                            _("Volumen de sonido"),
                            sound_volume_label,
                            Preference("sound volume"),
                            "♪",
                        )

                    if config.has_voice:
                        use menu_ui_preferences_slider(
                            _("Volumen de voz"),
                            voice_volume_label,
                            Preference("voice volume"),
                            "V",
                        )

                    if config.has_music or config.has_sound or config.has_voice:
                        textbutton _("Silenciar todo"):
                            style "menu_ui_preferences_mute_button"
                            action Preference("all mute", "toggle")

    key "game_menu" action Return()


screen menu_ui_preferences_slider(label, value_label, preference_value, icon):

    frame:
        style "menu_ui_preferences_slider_row"

        hbox:
            style "menu_ui_preferences_slider_row_content"

            text icon:
                style "menu_ui_preferences_slider_icon"

            vbox:
                style "menu_ui_preferences_slider_body"

                hbox:
                    style "menu_ui_preferences_slider_header"

                    text label:
                        style "menu_ui_preferences_slider_label"

                    text value_label:
                        style "menu_ui_preferences_slider_value"

                bar:
                    style "menu_ui_preferences_slider"
                    value preference_value


screen menu_ui_preferences_sidebar():

    frame:
        style "menu_ui_preferences_sidebar"

        vbox:
            style "menu_ui_preferences_sidebar_list"

            use menu_ui_preferences_nav_button("◷", _("Historial"), ShowMenu("history"), sensitive=not main_menu)
            use menu_ui_preferences_nav_button("▣", _("Guardar"), ShowMenu("save"), sensitive=not main_menu)
            use menu_ui_preferences_nav_button("□", _("Cargar"), ShowMenu("load"))
            use menu_ui_preferences_nav_button("⚙", _("Preferencias"), NullAction(), is_selected=True)
            use menu_ui_preferences_nav_button("★", _("Extras"), ShowMenu("extras"))
            use menu_ui_preferences_nav_button("⌂", _("Menú principal"), ShowMenu("main_menu") if main_menu else MainMenu())
            use menu_ui_preferences_nav_button("i", _("Acerca de"), ShowMenu("about"))

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                use menu_ui_preferences_nav_button("?", _("Ayuda"), ShowMenu("help"))

            if renpy.variant("pc"):
                use menu_ui_preferences_nav_button("X", _("Salir"), Quit(confirm=not main_menu))

    textbutton _("‹    Volver"):
        style "menu_ui_preferences_back_button"
        action Return()


screen menu_ui_preferences_nav_button(icon, label, action, is_selected=False, sensitive=True):

    button:
        style "menu_ui_preferences_nav_button"
        action action
        selected is_selected
        sensitive sensitive

        hbox:
            style "menu_ui_preferences_nav_button_content"

            text icon:
                style "menu_ui_preferences_nav_icon"

            text label:
                style "menu_ui_preferences_nav_label"
