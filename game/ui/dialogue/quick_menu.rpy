################################################################################
## In-story quick menu
################################################################################

screen quick_menu():

    zorder 100
    style_prefix "menu_ui_quick"

    if quick_menu:

        frame:
            style "menu_ui_quick_panel"

            hbox:
                style "menu_ui_quick_list"

                textbutton _("Atrás") action Rollback()
                textbutton _("Historial") action ShowMenu("history")
                textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Guardar") action ShowMenu("save")
                textbutton _("G. rápido") action QuickSave()
                textbutton _("C. rápida") action QuickLoad()
                textbutton _("Opciones") action ShowMenu("preferences")


screen quick_menu():
    variant "touch"

    zorder 100
    style_prefix "menu_ui_quick"

    if quick_menu:

        frame:
            style "menu_ui_quick_panel"

            hbox:
                style "menu_ui_quick_list"

                textbutton _("Atrás") action Rollback()
                textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Menú") action ShowMenu()
