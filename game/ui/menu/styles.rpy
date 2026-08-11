################################################################################
## Menu styles
################################################################################

style menu_ui_navigation is vbox
style menu_ui_navigation_button is gui_button
style menu_ui_navigation_button_text is gui_button_text

style menu_ui_navigation:
    xpos gui.navigation_xpos
    yalign 0.5
    spacing gui.navigation_spacing

style menu_ui_navigation_button:
    size_group "menu_ui_navigation"
    properties gui.button_properties("navigation_button")

style menu_ui_navigation_button_text:
    properties gui.text_properties("navigation_button")


style menu_ui_main_title_box is vbox
style menu_ui_main_text is gui_text
style menu_ui_main_title is menu_ui_main_text
style menu_ui_main_version is menu_ui_main_text

style menu_ui_main_title_box:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style menu_ui_main_text:
    properties gui.text_properties("main_menu", accent=True)

style menu_ui_main_title:
    properties gui.text_properties("title")

style menu_ui_main_version:
    properties gui.text_properties("version")


style menu_ui_game_outer_frame is empty
style menu_ui_game_navigation_frame is empty
style menu_ui_game_content_frame is empty
style menu_ui_game_viewport is gui_viewport
style menu_ui_game_side is gui_side
style menu_ui_game_scrollbar is gui_vscrollbar
style menu_ui_game_label is gui_label
style menu_ui_game_label_text is gui_label_text
style menu_ui_return_button is menu_ui_navigation_button
style menu_ui_return_button_text is menu_ui_navigation_button_text

style menu_ui_game_outer_frame:
    bottom_padding 45
    top_padding 180
    background menu_ui_game_overlay

style menu_ui_game_navigation_frame:
    xsize 420
    yfill True

style menu_ui_game_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style menu_ui_game_viewport:
    xsize 1380

style menu_ui_game_scrollbar:
    unscrollable gui.unscrollable

style menu_ui_game_side:
    spacing 15

style menu_ui_game_label:
    xpos 75
    ysize 180

style menu_ui_game_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style menu_ui_return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


style menu_ui_feature_list is vbox
style menu_ui_feature_button is gui_button
style menu_ui_feature_button_text is gui_button_text
style menu_ui_feature_description is gui_text

style menu_ui_feature_list:
    xfill True
    spacing 18

style menu_ui_feature_button:
    xfill True
    properties gui.button_properties("navigation_button")

style menu_ui_feature_button_text:
    properties gui.text_properties("navigation_button")

style menu_ui_feature_description:
    xmaximum 1000
    color gui.insensitive_color


style menu_ui_game_navigation_frame:
    variant "small"
    xsize 510

style menu_ui_game_content_frame:
    variant "small"
    top_margin 0

style menu_ui_game_viewport:
    variant "small"
    xsize 1305
