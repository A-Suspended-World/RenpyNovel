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


style menu_ui_main_navigation is vbox
style menu_ui_main_button is button
style menu_ui_main_button_content is vbox
style menu_ui_main_button_label is text
style menu_ui_main_button_subtitle is text

style menu_ui_main_navigation:
    xalign 0.5
    ypos 356
    spacing 14

style menu_ui_main_button:
    xsize 360
    ysize 82
    xpadding 20
    ypadding 7
    background menu_ui_main_button_idle
    hover_background menu_ui_main_button_hover
    selected_background menu_ui_main_button_hover
    insensitive_background menu_ui_main_button_idle
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_main_button_content:
    xfill True
    yfill True
    xalign 0.5
    yalign 0.5
    spacing 1

style menu_ui_main_button_label:
    font menu_ui_main_font
    size 29
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    insensitive_color gui.insensitive_color
    kerning 2.0
    xalign 0.5
    textalign 0.5

style menu_ui_main_button_subtitle:
    font gui.interface_text_font
    size 11
    color menu_ui_main_button_subtitle_color
    hover_color menu_ui_main_button_hover_color
    insensitive_color gui.insensitive_color
    kerning 1.0
    xalign 0.5
    textalign 0.5


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

style menu_ui_main_navigation:
    variant "small"
    ypos 300
    spacing 10

style menu_ui_main_button:
    variant "small"
    xsize 420
    ysize 86

style menu_ui_main_button_label:
    variant "small"
    size 32


################################################################################
## Preferences
################################################################################

style menu_ui_preferences_content_panel is frame
style menu_ui_preferences_content is vbox
style menu_ui_preferences_toggle_groups is hbox
style menu_ui_preferences_group is vbox
style menu_ui_preferences_group_label is gui_label
style menu_ui_preferences_group_label_text is gui_label_text
style menu_ui_preferences_radio_button is button
style menu_ui_preferences_radio_button_text is gui_button_text
style menu_ui_preferences_check_button is menu_ui_preferences_radio_button
style menu_ui_preferences_check_button_text is menu_ui_preferences_radio_button_text

style menu_ui_preferences_content_panel:
    xpos 440
    ypos 266
    xsize 1340
    ysize 710
    padding (36, 30)
    background menu_ui_panel_background

style menu_ui_preferences_content:
    xfill True
    yfill True
    spacing 20

style menu_ui_preferences_toggle_groups:
    xfill True
    ysize 190
    spacing 28

style menu_ui_preferences_group:
    xsize 620
    spacing 4

style menu_ui_preferences_group_label:
    xfill True
    bottom_margin 8
    bottom_padding 6

style menu_ui_preferences_group_label_text:
    font menu_ui_main_font
    size 25
    color menu_ui_main_button_text_color

style menu_ui_preferences_radio_button:
    xfill True
    ysize 48
    left_padding 44
    background None
    hover_background Solid("#d6e8ff80")
    foreground "assets/ui/menu/buttons/pref_radio_[prefix_]foreground.svg"
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_preferences_radio_button_text:
    font gui.interface_text_font
    size 22
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    insensitive_color gui.insensitive_color
    yalign 0.5

style menu_ui_preferences_check_button:
    foreground "assets/ui/menu/buttons/pref_check_[prefix_]foreground.svg"


style menu_ui_preferences_slider_columns is hbox
style menu_ui_preferences_slider_column is vbox
style menu_ui_preferences_slider_row is frame
style menu_ui_preferences_slider_row_content is hbox
style menu_ui_preferences_slider_icon is text
style menu_ui_preferences_slider_body is vbox
style menu_ui_preferences_slider_header is hbox
style menu_ui_preferences_slider_label is text
style menu_ui_preferences_slider_value is text
style menu_ui_preferences_slider is bar
style menu_ui_preferences_mute_button is button
style menu_ui_preferences_mute_button_text is gui_button_text

style menu_ui_preferences_slider_columns:
    xfill True
    spacing 28

style menu_ui_preferences_slider_column:
    xsize 620
    spacing 12

style menu_ui_preferences_slider_row:
    xfill True
    ysize 92
    padding (16, 12)
    background menu_ui_row_background

style menu_ui_preferences_slider_row_content:
    xfill True
    yfill True
    spacing 14

style menu_ui_preferences_slider_icon:
    font gui.interface_text_font
    size 24
    color menu_ui_main_button_text_color
    xsize 48
    xalign 0.5
    yalign 0.5
    textalign 0.5

style menu_ui_preferences_slider_body:
    xfill True
    yalign 0.5
    spacing 5

style menu_ui_preferences_slider_header:
    xfill True

style menu_ui_preferences_slider_label:
    font gui.interface_text_font
    size 20
    color menu_ui_main_button_text_color

style menu_ui_preferences_slider_value:
    font gui.interface_text_font
    size 18
    color "#2869b4"
    xalign 1.0

style menu_ui_preferences_slider:
    xfill True
    ysize 12
    left_gutter 10
    right_gutter 10
    left_bar Solid("#49a7ff")
    right_bar Solid("#8fa9c5")
    thumb "assets/ui/menu/buttons/pref_slider_thumb.svg"
    thumb_offset 1

style menu_ui_preferences_mute_button:
    xalign 1.0
    xsize 360
    ysize 54
    background Frame(menu_ui_main_button_idle, 24, 24)
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    selected_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_preferences_mute_button_text:
    font gui.interface_text_font
    size 20
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    xalign 0.5
    yalign 0.5
    textalign 0.5


style menu_ui_preferences_sidebar is frame
style menu_ui_preferences_sidebar_list is vbox
style menu_ui_preferences_nav_button is button
style menu_ui_preferences_nav_button_content is hbox
style menu_ui_preferences_nav_icon is text
style menu_ui_preferences_nav_label is text
style menu_ui_preferences_back_button is button
style menu_ui_preferences_back_button_text is gui_button_text

style menu_ui_preferences_sidebar:
    xpos 75
    ypos 276
    xsize 320
    ysize 602
    padding (14, 18)
    background menu_ui_panel_background

style menu_ui_preferences_sidebar_list:
    xfill True
    spacing 4

style menu_ui_preferences_nav_button:
    xfill True
    ysize 56
    xpadding 12
    background None
    hover_background Frame(menu_ui_main_button_idle, 24, 24)
    selected_background Frame(menu_ui_main_button_hover, 24, 24)
    insensitive_background None
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_preferences_nav_button_content:
    xfill True
    yfill True
    spacing 12

style menu_ui_preferences_nav_icon:
    font gui.interface_text_font
    size 25
    color "#2d5d92"
    insensitive_color gui.insensitive_color
    xsize 36
    yalign 0.5
    textalign 0.5

style menu_ui_preferences_nav_label:
    font menu_ui_main_font
    size 19
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    insensitive_color gui.insensitive_color
    yalign 0.5

style menu_ui_preferences_back_button:
    xpos 75
    ypos 914
    xsize 320
    ysize 70
    background Frame(menu_ui_main_button_idle, 24, 24)
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_preferences_back_button_text:
    font menu_ui_main_font
    size 21
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    xalign 0.5
    yalign 0.5
    textalign 0.5
