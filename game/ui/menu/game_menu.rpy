################################################################################
## Shared game-menu shell
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "menu_ui_game"

    if main_menu:
        use menu_ui_background(menu_ui_main_background)
    else:
        use menu_ui_background(menu_ui_game_background)

    frame:
        style "menu_ui_game_outer_frame"

        hbox:

            frame:
                style "menu_ui_game_navigation_frame"

            frame:
                style "menu_ui_game_content_frame"

                if scroll == "viewport":

                    viewport:
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

    use menu_ui_game_navigation

    textbutton _("Return"):
        style "menu_ui_return_button"
        action Return()

    label title:
        style "menu_ui_game_label"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
