################################################################################
## Shared UI theme tokens
################################################################################

## These aliases keep asset changes out of layout code. The current background
## is a temporary visual target and can be replaced without touching screens.
define menu_ui_main_background = "assets/ui/menu/backgrounds/main_menu_background.png"
define menu_ui_main_overlay = None
define menu_ui_preferences_background = "assets/ui/menu/backgrounds/preferences_concept.png"
define menu_ui_game_background = gui.game_menu_background
define menu_ui_game_overlay = "gui/overlay/game_menu.png"

## Main-menu typography and interactive artwork.
define menu_ui_main_font = "assets/fonts/Cinzel-Variable.ttf"
define menu_ui_main_button_idle = "assets/ui/menu/buttons/main_button_idle.svg"
define menu_ui_main_button_hover = "assets/ui/menu/buttons/main_button_hover.svg"
define menu_ui_main_button_text_color = "#172b59"
define menu_ui_main_button_hover_color = "#07183b"
define menu_ui_main_button_subtitle_color = "#44577c"
define menu_ui_panel_background = Frame("assets/ui/menu/panels/crystal_panel.svg", 28, 28)
define menu_ui_row_background = Frame("assets/ui/menu/panels/crystal_row.svg", 24, 24)

## The concept background already includes its title treatment. Enable this
## after replacing it with separated production artwork.
define menu_ui_show_dynamic_title = False

## UI feedback can be replaced globally from this file.
define menu_ui_hover_sound = "assets/audio/ui/UI Sci-Fi Select.wav"
define menu_ui_activate_sound = "assets/audio/ui/UI Sci-Fi Confirm.wav"

## Optional menu music can be assigned later without changing screen code.
define menu_ui_main_music = None

## Shared copy for scaffolded sections.
define menu_ui_placeholder_text = _("This section is ready for its future content and visual design.")
