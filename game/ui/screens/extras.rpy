################################################################################
## Extras hub
################################################################################

screen extras():

    tag menu

    use game_menu(_("Extras"), scroll="viewport"):

        vbox:
            style "menu_ui_feature_list"

            text _("Aquí encontrarás contenido opcional y desbloqueable. Cada sección es independiente para que pueda crecer sin acoplarse al menú principal."):
                style "menu_ui_feature_description"

            textbutton _("Galería"):
                style "menu_ui_feature_button"
                action ShowMenu("gallery")

            textbutton _("Sala de música"):
                style "menu_ui_feature_button"
                action ShowMenu("music_room")

            textbutton _("Selección de capítulos"):
                style "menu_ui_feature_button"
                action ShowMenu("chapter_select")

            textbutton _("Logros"):
                style "menu_ui_feature_button"
                action ShowMenu("achievements")
