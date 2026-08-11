################################################################################
## Extensible feature placeholders
################################################################################

screen menu_ui_feature_placeholder(title, description=menu_ui_placeholder_text):

    use game_menu(title):
        use menu_ui_empty_state(title, description)


screen gallery():
    tag menu
    use menu_ui_feature_placeholder(
        _("Gallery"),
        _("CG illustrations, character art, and unlocked scenes will be presented here."),
    )


screen music_room():
    tag menu
    use menu_ui_feature_placeholder(
        _("Music Room"),
        _("Unlocked tracks, playback controls, and track information will be presented here."),
    )


screen chapter_select():
    tag menu
    use menu_ui_feature_placeholder(
        _("Chapter Selection"),
        _("Available chapters, completion state, and safe starting points will be presented here."),
    )


screen achievements():
    tag menu
    use menu_ui_feature_placeholder(
        _("Achievements"),
        _("Progress, unlocked milestones, and hidden objectives will be presented here."),
    )
