################################################################################
## Menu navigation
################################################################################

## Compatibility entry point for screens that still use the generated name.
screen navigation():

    if main_menu:
        use menu_ui_main_navigation
    else:
        use menu_ui_game_navigation


screen menu_ui_main_navigation():

    vbox:
        style "menu_ui_main_navigation"
        at menu_ui_slide_in

        use menu_ui_main_button(_("NEW GAME"), _("BEGIN THE STORY"), Start())
        use menu_ui_main_button(_("LOAD GAME"), _("CONTINUE YOUR JOURNEY"), ShowMenu("load"))
        use menu_ui_main_button(_("SETTINGS"), _("CONFIGURE EXPERIENCE"), ShowMenu("preferences"))
        use menu_ui_main_button(_("GALLERY"), _("UNLOCKED MEMORIES"), ShowMenu("gallery"))
        use menu_ui_main_button(_("EXTRAS"), _("ADDITIONAL CONTENT"), ShowMenu("extras"))

        if renpy.variant("pc"):
            use menu_ui_main_button(_("EXIT"), _("CLOSE APPLICATION"), Quit(confirm=False))


screen menu_ui_main_button(label, subtitle, action):

    button:
        style "menu_ui_main_button"
        action action

        vbox:
            style "menu_ui_main_button_content"

            text label:
                style "menu_ui_main_button_label"

            text subtitle:
                style "menu_ui_main_button_subtitle"


screen menu_ui_game_navigation():

    vbox:
        style "menu_ui_navigation"
        style_prefix "menu_ui_navigation"
        at menu_ui_slide_in

        if not main_menu:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Extras") action ShowMenu("extras")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=not main_menu)


################################################################################
## Shared side navigation
################################################################################

screen menu_ui_side_navigation(active_screen=None):

    frame:
        style "menu_ui_preferences_sidebar"

        vbox:
            style "menu_ui_preferences_sidebar_list"

            use menu_ui_side_nav_button("◷", _("Historial"), ShowMenu("history"), active_screen == "history", not main_menu)
            use menu_ui_side_nav_button("▣", _("Guardar"), ShowMenu("save"), active_screen == "save", not main_menu)
            use menu_ui_side_nav_button("□", _("Cargar"), ShowMenu("load"), active_screen == "load")
            use menu_ui_side_nav_button("⚙", _("Preferencias"), ShowMenu("preferences"), active_screen == "preferences")
            use menu_ui_side_nav_button("★", _("Extras"), ShowMenu("extras"), active_screen in ("extras", "gallery", "music_room", "chapter_select", "achievements"))
            use menu_ui_side_nav_button("⌂", _("Menú principal"), ShowMenu("main_menu") if main_menu else MainMenu())
            use menu_ui_side_nav_button("i", _("Acerca de"), ShowMenu("about"), active_screen == "about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                use menu_ui_side_nav_button("?", _("Ayuda"), ShowMenu("help"), active_screen in ("help", "keyboard_help", "mouse_help", "gamepad_help"))

            if renpy.variant("pc"):
                use menu_ui_side_nav_button("X", _("Salir"), Quit(confirm=not main_menu))

    textbutton _("‹    Volver"):
        style "menu_ui_preferences_back_button"
        action Return()


screen menu_ui_side_nav_button(icon, label, action, is_selected=False, sensitive=True):

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
