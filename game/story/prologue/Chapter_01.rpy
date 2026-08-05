label chapter_01:
# Aula C3

scene bg aisle with dissolve

play music BGM_OPENING

"Me detuve frente al aula C3."

"dude antes de entrar."

"¿De verdad debería entrar ahora?"

"dude durante unos segundos, antes de llegar a una conclusion"

"Justo cuando estaba a punto de dar media vuelta..."

prof "Adelante, alumno."

"Desde el otro lado de la puerta, alguien me invito a pasar"

"¿Acaso puede ver atravez de las paredes?"

"Al acercarme a la entrada, esta se abrio de inmediato"

scene bg classroom with dissolve

play sound "door_open.ogg"

$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)


"Suspiré para mis adentros y abrí la puerta."

$ escena.hide("alice_formal_idle")

$ escena.show(
    "alice_formal_thinking",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

prof "Llegas tarde... otra vez, alumno."

$ escena.hide("alice_formal_thinking")

$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

"Una mujer de cabello azul y lentes permanecía frente a la pizarra."

"Su mirada era tan fría que sentí un escalofrío recorrerme la espalda."


y "..."

"No tenía ninguna excusa que pudiera sonar convincente."

$ escena.show(
    "alice_formal_R",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

"La profesora desvió ligeramente la mirada hacia los asientos."

$ escena.hide("alice_formal_R")

$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

"No hacía falta decir nada más."

"Caminé tan rápido como mi cuerpo me lo permitió y tomé asiento."

$ escena.hide("alice_formal_idle",transition=dissolve)


"La clase continuó como si nada hubiera pasado."

"La profesora comenzó a hablar sobre historia."

"Intenté prestar atención..."

"No pude."

"La mujer que había visto en la entrada seguía dando vueltas en mi cabeza."

"¿Quién era?"

"¿Y por qué había reaccionado de esa manera?"

"Algo rozó mi espalda."

"Giré apenas la cabeza."

"Una chica sonriente estaba sentaba justa atras de mi."

stop music

play sound BGM_SHEN

$ escena.show(
    "kuki_smile_eyes_closed",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

k "¿Pasó algo interesante de camino hasta aquí?"

$ escena.show(
    "kuki_idle",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

"Le respondí con un simple ceño fruncido antes de volver la vista al frente."

$ escena.show(
    "kuki_smile",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

k "¿Así que no me lo vas a contar?"

play sound "tap.ogg"

"Intenté reconstruir lo ocurrido en la entrada."

play sound "tap.ogg"

"Otro golpecito en la espalda."

play sound "tap.ogg"

"Y otro."

play sound "tap.ogg"

"Cada vez eran más insistentes."

$ escena.show(
    "kuki_idle",
    POS_CEN,
    PLANO_MEDIO
)

k "¿Todavía no vas a hablar?"

k "Mmm... veamos..."

"Decidí ignorarla."

"Tarde o temprano acabaría perdiendo el interés."

"Después de todo..."

"Nadie iba a creerme."

"Nadie creería que había visto..."

"Una imagen cruzó de repente por mi mente."

"La escena de la entrada empezó a encajar."

"Sentí un nudo en el estómago."

"Un sabor amargo me invadió la boca."

"Mi cabeza se quedó completamente en blanco."

$ escena.show(
    "kuki",
    POS_DER,
    PLANO_MEDIO,
    respirar,
    expresion="preocupada"
)

k "¿Eh?"

k "¿Te pasa algo...?"

play sound "desk_hit.ogg"

$ escena.show(
    "yuu",
    POS_IZQ,
    PLANO_MEDIO,
    temblar,
    expresion="asustado"
)

y "¡¡PARAAAA!!"

stop sound

"Cuando recuperé el sentido..."

"Estaba de pie."

"Y todo el salón me estaba mirando."

return