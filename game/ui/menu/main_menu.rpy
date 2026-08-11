################################################################################
## Main menu
################################################################################

screen main_menu():

    tag menu

    use menu_ui_background(menu_ui_main_background, menu_ui_main_overlay)
    use menu_ui_main_navigation

    if gui.show_name:

        vbox:
            style "menu_ui_main_title_box"
            at menu_ui_fade_in(0.1)

            text "[config.name!t]":
                style "menu_ui_main_title"

            text "[config.version]":
                style "menu_ui_main_version"
