## Manual UI smoke test used by the developer test launcher.
label test_ui:

    $ quick_menu = False
    call screen preferences
    $ quick_menu = True
    jump test_launcher


label test_ui_menu_shell:

    $ quick_menu = False
    call screen extras
    $ quick_menu = True
    jump test_launcher


label test_ui_file_slots:

    $ quick_menu = False
    call screen save
    $ quick_menu = True
    jump test_launcher
