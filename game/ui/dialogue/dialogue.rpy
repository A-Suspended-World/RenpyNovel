################################################################################
## Active dialogue screen
################################################################################

screen say(who, what):

    style_prefix "menu_ui_dialogue"

    window:
        id "window"
        style "menu_ui_dialogue_window"
        at menu_ui_dialogue_show

        frame:
            id "accent"
            style "menu_ui_dialogue_accent"

        if who is not None:

            frame:
                id "namebox"
                style "menu_ui_dialogue_namebox"

                text who:
                    id "who"
                    style "menu_ui_dialogue_name"

        text what:
            id "what"
            style "menu_ui_dialogue_text"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0
