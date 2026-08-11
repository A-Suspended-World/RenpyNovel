################################################################################
## Reusable UI motion
################################################################################

transform menu_ui_fade_in(delay=0.0):
    alpha 0.0
    pause delay
    linear 0.25 alpha 1.0

transform menu_ui_slide_in(delay=0.0, distance=24):
    alpha 0.0
    xoffset -distance
    pause delay
    parallel:
        linear 0.25 alpha 1.0
    parallel:
        easeout 0.25 xoffset 0

transform menu_ui_soft_focus:
    on idle:
        linear 0.12 alpha 0.86
    on hover:
        linear 0.12 alpha 1.0
