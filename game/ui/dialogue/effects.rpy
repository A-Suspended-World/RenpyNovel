################################################################################
## Dialogue motion
################################################################################

## The shader is applied only to story dialogue. UI labels and menus remain
## static, and the player's text-speed preference still controls reveal speed.
define menu_ui_dialogue_text_shader = "dissolve"

transform menu_ui_dialogue_show:
    alpha 0.0
    yoffset 18
    parallel:
        linear 0.18 alpha 1.0
    parallel:
        easeout 0.18 yoffset 0

transform menu_ui_dialogue_ctc_pulse:
    alpha 0.55
    linear 0.55 alpha 1.0
    linear 0.55 alpha 0.55
    repeat
