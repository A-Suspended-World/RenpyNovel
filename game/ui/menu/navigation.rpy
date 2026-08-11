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
        style "menu_ui_navigation"
        style_prefix "menu_ui_navigation"
        at menu_ui_slide_in

        textbutton _("Start") action Start()
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Extras") action ShowMenu("extras")
        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            textbutton _("Quit") action Quit(confirm=False)


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
