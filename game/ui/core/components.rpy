################################################################################
## Reusable UI components
################################################################################

screen menu_ui_background(background, overlay=None):

    add background

    if overlay:
        add overlay


screen menu_ui_empty_state(title, description=menu_ui_placeholder_text):

    vbox:
        style "menu_ui_empty_state"

        label title:
            style "menu_ui_empty_state_title"

        text description:
            style "menu_ui_empty_state_text"


style menu_ui_empty_state is vbox
style menu_ui_empty_state_title is gui_label
style menu_ui_empty_state_title_text is gui_label_text
style menu_ui_empty_state_text is gui_text

style menu_ui_empty_state:
    xfill True
    spacing 24
    xalign 0.5
    yalign 0.35

style menu_ui_empty_state_title:
    xalign 0.5

style menu_ui_empty_state_title_text:
    textalign 0.5

style menu_ui_empty_state_text:
    xalign 0.5
    xmaximum 900
    textalign 0.5
