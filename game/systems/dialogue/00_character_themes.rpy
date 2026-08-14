################################################################################
## Character dialogue themes
################################################################################

## This module is initialized before character declarations. It is the single
## source of truth for speaker colors and keeps visual configuration out of the
## story scripts.
init -100 python:

    DIALOGUE_BODY_COLOR = "#eef6ff"

    CHARACTER_DIALOGUE_THEMES = {
        "narrator": {
            "name_color": "#dceaff",
            "accent_color": "#8fb8e8",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "yuu": {
            "name_color": "#80e8ff",
            "accent_color": "#36bfe8",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "kuki": {
            "name_color": "#ff8fcb",
            "accent_color": "#ef4fa7",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "elen": {
            "name_color": "#91adff",
            "accent_color": "#557fe8",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "zofi": {
            "name_color": "#ffd889",
            "accent_color": "#e9a93b",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "alice": {
            "name_color": "#b5a8ff",
            "accent_color": "#7867df",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "professor": {
            "name_color": "#9ec8ff",
            "accent_color": "#438bd6",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "sis": {
            "name_color": "#ffaaa2",
            "accent_color": "#e56962",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "max": {
            "name_color": "#ffc777",
            "accent_color": "#db8735",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "unknown": {
            "name_color": "#c5cfdd",
            "accent_color": "#71839c",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "student": {
            "name_color": "#9bdcf2",
            "accent_color": "#4cabc9",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "mysterious_girl": {
            "name_color": "#d9a7ff",
            "accent_color": "#9d5ed3",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
        "twintails_girl": {
            "name_color": "#ff98c8",
            "accent_color": "#dd4d91",
            "dialogue_color": DIALOGUE_BODY_COLOR,
        },
    }

    def get_character_dialogue_theme(theme_id):
        """Returns a registered theme, falling back to the narrator palette."""
        return CHARACTER_DIALOGUE_THEMES.get(
            theme_id,
            CHARACTER_DIALOGUE_THEMES["narrator"],
        )

    def make_dialogue_character(name, theme_id, **kwargs):
        """Creates a Character wired to the shared dialogue displayables."""
        theme = get_character_dialogue_theme(theme_id)
        accent = theme["accent_color"]

        properties = {
            "who_color": theme["name_color"],
            "who_outlines": [(1, "#07152f", 0, 1)],
            "what_color": theme["dialogue_color"],
            "what_outlines": [(1, "#07152fcc", 0, 1)],
            "accent_background": Solid(accent),
            "namebox_background": Frame(
                "assets/ui/menu/buttons/main_button_idle.svg",
                24,
                24,
            ),
            "ctc": Text(
                "◆",
                font=gui.interface_text_font,
                size=18,
                color=accent,
                outlines=[(1, "#07152f", 0, 0)],
            ),
            "ctc_position": "nestled",
        }
        properties.update(kwargs)

        translated_name = _(name) if name is not None else None
        return Character(translated_name, **properties)

    if "accent" not in config.character_id_prefixes:
        config.character_id_prefixes.append("accent")

    if "namebox" not in config.character_id_prefixes:
        config.character_id_prefixes.append("namebox")
