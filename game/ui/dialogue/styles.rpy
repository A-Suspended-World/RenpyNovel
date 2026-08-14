################################################################################
## Dialogue and quick-menu styles
################################################################################

style menu_ui_dialogue_window is window
style menu_ui_dialogue_accent is frame
style menu_ui_dialogue_namebox is frame
style menu_ui_dialogue_name is text
style menu_ui_dialogue_text is text

style menu_ui_dialogue_window:
    xalign 0.5
    yalign 1.0
    xfill True
    ysize 300
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style menu_ui_dialogue_accent:
    xpos 286
    ypos 4
    xsize 1348
    ysize 4
    padding (0, 0)

style menu_ui_dialogue_namebox:
    xpos 330
    ypos 18
    xminimum 290
    ysize 60
    xpadding 30
    ypadding 8

style menu_ui_dialogue_name:
    font menu_ui_main_font
    size 30
    kerning 1.5
    yalign 0.5

style menu_ui_dialogue_text:
    xpos 356
    ypos 92
    xsize 1210
    ysize 120
    font gui.text_font
    size 30
    line_spacing 7
    color DIALOGUE_BODY_COLOR
    adjust_spacing False
    textshader menu_ui_dialogue_text_shader


style menu_ui_quick_panel is frame
style menu_ui_quick_list is hbox
style menu_ui_quick_button is button
style menu_ui_quick_button_text is text

style menu_ui_quick_panel:
    xalign 0.5
    yalign 1.0
    yoffset -10
    xpadding 14
    ypadding 5
    background Frame("assets/ui/menu/panels/crystal_row.svg", 24, 24)

style menu_ui_quick_list:
    spacing 3

style menu_ui_quick_button:
    xminimum 94
    ysize 38
    xpadding 12
    background None
    hover_background Solid("#8fd4ff55")
    selected_background Solid("#66bfff66")
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_quick_button_text:
    font menu_ui_main_font
    size 15
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color "#1768ad"
    insensitive_color "#6f7f94"
    xalign 0.5
    yalign 0.5
    textalign 0.5

style menu_ui_quick_panel:
    variant "touch"
    yoffset -14

style menu_ui_quick_button:
    variant "touch"
    xminimum 170
    ysize 56

style menu_ui_quick_button_text:
    variant "touch"
    size 20
