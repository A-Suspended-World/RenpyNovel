################################################################################
## Shared UI theme tokens
################################################################################

## These aliases keep asset changes out of layout code. They deliberately point
## to the current generated artwork until the final visual direction is chosen.
define menu_ui_main_background = gui.main_menu_background
define menu_ui_main_overlay = "gui/overlay/main_menu.png"
define menu_ui_game_background = gui.game_menu_background
define menu_ui_game_overlay = "gui/overlay/game_menu.png"

## Optional menu music can be assigned later without changing screen code.
define menu_ui_main_music = None

## Shared copy for scaffolded sections.
define menu_ui_placeholder_text = _("This section is ready for its future content and visual design.")
