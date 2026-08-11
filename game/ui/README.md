# UI architecture

This directory owns the custom interface layer. Story and engine files should
not define menu screens or menu-specific styles.

## Responsibilities

- `core/`: shared assets, reusable components, and transforms.
- `menu/`: the main menu, in-game menu shell, and navigation.
- `screens/`: feature screens opened from the menu.

Ren'Py discovers every `.rpy` file under `game/` automatically. Special screen
names such as `main_menu`, `game_menu`, `save`, and `preferences` must have a
single active definition. The generated versions retained in `screens.rpy` are
prefixed with `legacy_` and serve only as a migration reference.

## Extension rules

1. Put reusable layout in `core/components.rpy`.
2. Put reusable motion in `core/transforms.rpy`.
3. Keep feature-specific screens in their own file under `screens/`.
4. Put UI artwork under `assets/ui/`, fonts under `assets/fonts/`, and UI sound
   under `assets/audio/ui/`.
5. Prefer `xalign`, `yalign`, and bounded containers over absolute positions so
   layouts remain adaptable.
6. Add external code to `game/libs/` only when native Ren'Py features are not
   sufficient, and document its license and version.

## Current visual prototype

The main menu currently uses a supplied concept image as temporary background
art. Interactive buttons, typography, colors, sounds, and layout remain
separate from that image so production artwork can replace it later.

Cinzel is used for the primary menu labels. The font is distributed under the
SIL Open Font License; its license is stored next to the font file.
