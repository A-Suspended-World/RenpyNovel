################################################################################
## Shared game-menu shell
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    $ active_screen = CurrentScreenName()
    style_prefix "menu_ui_game"

    use menu_ui_background(menu_ui_main_background)
    add Solid("#e9f3ff66")

    frame:
        style "menu_ui_game_content_panel"

        if scroll == "viewport":

            viewport:
                style "menu_ui_game_content_viewport"
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True

                vbox:
                    spacing spacing
                    transclude

        elif scroll == "vpgrid":

            vpgrid:
                style "menu_ui_game_content_grid"
                cols 1
                yinitial yinitial
                scrollbars "vertical"
                mousewheel True
                draggable True
                pagekeys True
                side_yfill True
                spacing spacing
                transclude

        else:
            transclude

    use menu_ui_side_navigation(active_screen)

    text title:
        style "menu_ui_game_title"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
    else:
        key "game_menu" action Return()
