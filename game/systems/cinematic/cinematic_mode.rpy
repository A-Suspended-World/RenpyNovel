################################################################################
## Cinematic still scenes
################################################################################

## Public state that other screens may inspect when they need to avoid drawing
## non-essential overlays during an establishing shot.
default cinematic_mode_active = False

## Stack-based restoration keeps nested cinematic calls from losing the value
## that quick_menu had before the scene started.
default _cinematic_quick_menu_stack = []


define cinematic_enter_transition = Fade(0.35, 0.15, 0.65)


transform cinematic_fullscreen:
    xysize (config.screen_width, config.screen_height)
    xalign 0.5
    yalign 0.5


transform cinematic_establishing_shot(duration=4.0):
    xysize (config.screen_width, config.screen_height)
    xalign 0.5
    yalign 0.5
    zoom 1.035
    ease duration zoom 1.0


## Starts a textbox-free section. Prefer cinematic_still for normal use; these
## begin/end labels remain public for sequences containing several shots.
label cinematic_begin:

    $ _cinematic_quick_menu_stack = _cinematic_quick_menu_stack + [quick_menu]
    $ cinematic_mode_active = True
    $ quick_menu = False
    window hide

    return


label cinematic_end:

    $ quick_menu = _cinematic_quick_menu_stack[-1] if _cinematic_quick_menu_stack else True
    $ _cinematic_quick_menu_stack = _cinematic_quick_menu_stack[:-1]
    $ cinematic_mode_active = bool(_cinematic_quick_menu_stack)
    window auto

    return


## Displays one clean full-screen image and restores the dialogue UI afterward.
## duration=None waits for player input. A numeric duration may still be skipped
## unless skippable is False.
label cinematic_still(
        image_name,
        duration=3.0,
        transition=cinematic_enter_transition,
        motion=True,
        skippable=True):

    call cinematic_begin

    $ _cinematic_motion_duration = duration if duration is not None else 5.0
    $ renpy.scene()

    if motion:
        $ renpy.show(image_name, at_list=[cinematic_establishing_shot(_cinematic_motion_duration)])
    else:
        $ renpy.show(image_name, at_list=[cinematic_fullscreen])

    with transition

    if duration is None:
        pause
    else:
        $ renpy.pause(duration, hard=not skippable)

    call cinematic_end

    return
