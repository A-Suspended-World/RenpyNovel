################################################################################
## Extras hub
################################################################################

screen extras():

    tag menu

    use game_menu(_("Extras"), scroll="viewport"):

        vbox:
            style "menu_ui_feature_list"

            text _("Optional and unlockable content lives here. Each section is isolated so it can grow without coupling itself to the main menu."):
                style "menu_ui_feature_description"

            textbutton _("Gallery"):
                style "menu_ui_feature_button"
                action ShowMenu("gallery")

            textbutton _("Music Room"):
                style "menu_ui_feature_button"
                action ShowMenu("music_room")

            textbutton _("Chapter Selection"):
                style "menu_ui_feature_button"
                action ShowMenu("chapter_select")

            textbutton _("Achievements"):
                style "menu_ui_feature_button"
                action ShowMenu("achievements")
