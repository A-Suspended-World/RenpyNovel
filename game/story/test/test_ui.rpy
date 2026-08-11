## Manual UI smoke test used by the developer test launcher.
label test_ui:

    $ quick_menu = False
    call screen preferences
    $ quick_menu = True
    jump test_launcher
