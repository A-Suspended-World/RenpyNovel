################################################################################
## Characters
################################################################################

## The short variables below are the identifiers used by story dialogue, for
## example: k "Hola". Visual colors are registered separately in
## systems/dialogue/00_character_themes.rpy.

define narrator = make_dialogue_character(None, "narrator")

## Main cast.
define y = make_dialogue_character("Yuu", "yuu")
define k = make_dialogue_character("Kuki", "kuki")
define e = make_dialogue_character("Elen", "elen")
define z = make_dialogue_character("Zofi", "zofi")
define a = make_dialogue_character("Alice", "alice")
define prof = make_dialogue_character("Profesora", "professor")
define s = make_dialogue_character("Sis", "sis")
define m = make_dialogue_character("Max", "max")

## Supporting roles. Use unique identifiers so a supporting role never
## overwrites a main character definition.
define d = make_dialogue_character("Desconocido", "unknown")
define student = make_dialogue_character("Estudiante", "student")
define cm = make_dialogue_character("Chica misteriosa", "mysterious_girl")
define ccc = make_dialogue_character("Chica con coletas", "twintails_girl")
