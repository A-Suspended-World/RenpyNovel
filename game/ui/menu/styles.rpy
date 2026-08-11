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


style menu_ui_game_content_panel is frame
style menu_ui_game_content_viewport is viewport
style menu_ui_game_content_grid is vpgrid
style menu_ui_game_title is text

style menu_ui_game_content_panel:
    xpos 440
    ypos 240
    xsize 1340
    ysize 760
    padding (36, 34)
    background menu_ui_panel_background

style menu_ui_game_content_viewport:
    xfill True
    yfill True

style menu_ui_game_content_grid:
    xfill True
    yfill True

style menu_ui_game_title:
    xpos 448
    ypos 148
    xmaximum 1200
    font menu_ui_main_font
    size 58
    color menu_ui_main_button_text_color
    outlines [(1, "#eff6ff", 0, 0)]

style menu_ui_game_vscrollbar is vscrollbar

style menu_ui_game_vscrollbar:
    xsize 12
    base_bar Solid("#8fa9c5")
    thumb Solid("#49a7ff")

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


################################################################################
## Shared content screens
################################################################################

style about_label_text:
    font menu_ui_main_font
    size 28
    color menu_ui_main_button_text_color

style about_text:
    font gui.interface_text_font
    size 22
    color menu_ui_main_button_text_color


style page_label:
    xpadding 30
    ypadding 4
    background menu_ui_row_background

style page_label_text:
    font menu_ui_main_font
    size 22
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color

style page_button:
    xsize 48
    ysize 42
    background None
    hover_background Frame(menu_ui_main_button_idle, 18, 18)
    selected_background Frame(menu_ui_main_button_hover, 18, 18)

style page_button_text:
    font menu_ui_main_font
    size 18
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    textalign 0.5

style slot_button:
    xsize 404
    ysize 290
    padding (10, 10)
    background menu_ui_row_background
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    selected_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style slot_button_text:
    font gui.interface_text_font
    size 18
    color menu_ui_main_button_subtitle_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    xalign 0.5
    textalign 0.5

style slot_time_text:
    size 16

style slot_name_text:
    font menu_ui_main_font
    size 18


style history_window:
    xfill True
    ysize 190
    padding (18, 14)
    background menu_ui_row_background

style history_name:
    xpos 18
    ypos 10
    xanchor 0.0
    xsize 190

style history_name_text:
    min_width 190
    font menu_ui_main_font
    size 22
    color "#2869b4"
    textalign 0.0

style history_text:
    xpos 225
    ypos 12
    xanchor 0.0
    xsize 970
    min_width 970
    font gui.interface_text_font
    size 22
    color menu_ui_main_button_text_color
    textalign 0.0

style history_label_text:
    font menu_ui_main_font
    size 25
    color menu_ui_main_button_text_color


style help_button:
    xmargin 6
    xpadding 18
    ypadding 8
    background Frame(menu_ui_main_button_idle, 18, 18)
    hover_background Frame(menu_ui_main_button_hover, 18, 18)
    selected_background Frame(menu_ui_main_button_hover, 18, 18)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style help_button_text:
    font menu_ui_main_font
    size 19
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color

style help_label:
    xsize 310
    right_padding 24

style help_label_text:
    font menu_ui_main_font
    size 20
    color "#2869b4"
    xalign 1.0
    textalign 1.0

style help_text:
    font gui.interface_text_font
    size 21
    color menu_ui_main_button_text_color


style menu_ui_feature_button:
    xfill True
    ysize 64
    xpadding 24
    background Frame(menu_ui_main_button_idle, 24, 24)
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    selected_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_feature_button_text:
    font menu_ui_main_font
    size 22
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color

style menu_ui_feature_description:
    font gui.interface_text_font
    size 21
    color menu_ui_main_button_subtitle_color


style confirm_frame:
    xalign 0.5
    yalign 0.5
    xsize 760
    padding (48, 40)
    background menu_ui_panel_background

style confirm_prompt_text:
    font menu_ui_main_font
    size 28
    color menu_ui_main_button_text_color
    textalign 0.5

style confirm_button:
    xsize 230
    ysize 62
    background Frame(menu_ui_main_button_idle, 24, 24)
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style confirm_button_text:
    font menu_ui_main_font
    size 21
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    xalign 0.5
    textalign 0.5


################################################################################
## Save and load
################################################################################

style menu_ui_file_slots_root is vbox
style menu_ui_file_page_label is button
style menu_ui_file_page_label_text is input
style menu_ui_file_slot_grid is grid
style menu_ui_file_slot_button is button
style menu_ui_file_slot_content is vbox
style menu_ui_file_slot_preview is fixed
style menu_ui_file_slot_number is text
style menu_ui_file_slot_time is text
style menu_ui_file_slot_name is text
style menu_ui_file_page_navigation is hbox
style menu_ui_file_page_button is button
style menu_ui_file_page_button_text is text
style menu_ui_file_sync_button is button
style menu_ui_file_sync_button_text is text

style menu_ui_file_slots_root:
    xfill True
    yfill True
    spacing 10

style menu_ui_file_page_label:
    xalign 0.5
    xsize 320
    ysize 38
    background menu_ui_row_background

style menu_ui_file_page_label_text:
    font menu_ui_main_font
    size 19
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    xalign 0.5
    textalign 0.5

style menu_ui_file_slot_grid:
    xalign 0.5
    spacing 12

style menu_ui_file_slot_button:
    xsize 390
    ysize 240
    padding (8, 8)
    background menu_ui_row_background
    hover_background Frame(menu_ui_main_button_hover, 24, 24)
    selected_background Frame(menu_ui_main_button_hover, 24, 24)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_file_slot_content:
    xfill True
    spacing 2

style menu_ui_file_slot_preview:
    xalign 0.5
    xsize 350
    ysize 190

style menu_ui_file_slot_number:
    xpos 10
    ypos 8
    font menu_ui_main_font
    size 18
    color "#ffffff"
    outlines [(1, "#17335f", 0, 0)]

style menu_ui_file_slot_time:
    xalign 0.5
    font gui.interface_text_font
    size 15
    color menu_ui_main_button_subtitle_color
    textalign 0.5

style menu_ui_file_slot_name:
    xalign 0.5
    font menu_ui_main_font
    size 15
    color menu_ui_main_button_text_color
    textalign 0.5

style menu_ui_file_page_navigation:
    xalign 0.5
    spacing 4

style menu_ui_file_page_button:
    xsize 48
    ysize 38
    background None
    hover_background Frame(menu_ui_main_button_idle, 16, 16)
    selected_background Frame(menu_ui_main_button_hover, 16, 16)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_file_page_button_text:
    font menu_ui_main_font
    size 17
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    selected_color menu_ui_main_button_hover_color
    xalign 0.5
    yalign 0.5
    textalign 0.5

style menu_ui_file_sync_button:
    xalign 0.5
    xsize 310
    ysize 42
    background Frame(menu_ui_main_button_idle, 18, 18)
    hover_background Frame(menu_ui_main_button_hover, 18, 18)
    hover_sound menu_ui_hover_sound
    activate_sound menu_ui_activate_sound

style menu_ui_file_sync_button_text:
    font menu_ui_main_font
    size 17
    color menu_ui_main_button_text_color
    hover_color menu_ui_main_button_hover_color
    xalign 0.5
    yalign 0.5
    textalign 0.5
