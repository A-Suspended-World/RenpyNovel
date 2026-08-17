#Resumen rapido: El protagonista llega su salon de clases luego de haber tenido su encuentro con una misteriosa mujer


label part_03:

scene bg aisle with dissolve

play music BGM_OPENING

"Me detuve frente al aula C3."

"dude antes de entrar."

"¿De verdad debería entrar ahora?"

"dude durante unos segundos, antes de llegar a una conclusion"

"Justo cuando estaba a punto de dar media vuelta..."

prof "Adelante, alumno."

"Desde el otro lado de la puerta, escuche una voz"

"La cual me invitaba a pasar"

"..."

"¿Acaso puede ver atravez de las paredes?"

"No me quedaba de otra...."

"Al acercarme un poco mas a la entrada"

"Esta se deslizo hacia un lado"

play sound SFX_DOOR

"..."

scene bg classroom with dissolve

"Una vez dentro"

"Habia una mujer para al lado de la pizarra"


$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_CERCANO,
    rebote,
    transition = dissolve
)

$ escena.hide("alice_formal_idle")

$ escena.show(
    "alice_formal_thinking",
    POS_CEN,
    PLANO_CERCANO
)

prof "Vuelve a llegar tarde, alumno."

$ escena.hide("alice_formal_thinking")

$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_CERCANO
)

"Era una mujer de cabello azul oscuro y con una mirada penetrante."

"Aterradora...."

y "No tengo excusa por haber llagado tarde....."

y "Disculpeme"

$ escena.show(
    "alice_formal_R",
    POS_CEN,
    PLANO_CERCANO
)

"La profesora desvió ligeramente la mirada hacia los asientos."

$ escena.hide("alice_formal_R")

$ escena.show(
    "alice_formal_idle",
    POS_CEN,
    PLANO_CERCANO
)

"No hacía falta decir nada más."

"Caminé tan rápido como mi cuerpo me lo permitió y tomé asiento."

$ escena.hide("alice_formal_idle",transition=dissolve)


"La clase continuó como si nada hubiera pasado."

"Mientras la profesora dictaba su clase, se me vino a la mente lo que habia pasado ante."

"Aun que intenté prestar atención..."

"Simplemente no podia quitarlo de mi cabeza."

"Esa mujer de la entrada...."

"¿Quién era?"

"Y lo que mas me desconcertaba"

"¿Por qué había reaccionado de esa manera?"

"Mientras trataba de llegar a una respuesta"

"Senti que algo tocaba mi espalda."

"incline mi cabeza hacia atras."

stop music

scene bg kuki_escena01 
with dissolve

"..."


"aquí vamos de nuevo..."

scene bg classroom

play music BGM_SHEN

$ escena.show(
    "kuki_smile_eyes_closed",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

ccc "¿Asi que, te paso algo interesante de camino?"

$ escena.hide("kuki_smile_eyes_closed")

$ escena.show(
    "kuki_idle",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)


"Uhg... tenia que ser ella"


"Le respondí con un simple ceño fruncido, antes de regresar la mirada al frente."



$ escena.show(
    "kuki_boring",
    POS_CEN,
    PLANO_CERCANO
)

$ escena.hide("kuki_idle"
)



ccc "¿Así que no me lo vas a contar?"



ccc "Aburrido"

$ escena.hide("kuki_boring",
transition=dissolve)

"Era mejor igorarla, sino...."

"Nada bueno podia pasar..."

"Donde me quede....Ah, estaba tratando de...."

"Senti nuevamente algo tocandome la espalda."

"Volví a mirar hacia atrás."

$ escena.show(
    "kuki_smile",
    POS_CEN,
    PLANO_CERCANO,
    negar
)

ccc "PUM PUM"


"..."

$ escena.hide("kuki_smile")

$ escena.show(
    "kuki_smile",
    POS_CEN,
    PLANO_CERCANO,
    negar
)

"Y otro."


"Cada vez eran más insistentes."

$ escena.hide("kuki_smile")

$ escena.show(
    "kuki_smile_eyes_closed",
    POS_CEN,
    PLANO_CERCANO
)

ccc "¿Todavía no vas a hablar?"

$ escena.hide("kuki_smile_eyes_closed", transition=dissolve)

"Decidí nuevamente usar: ignorar por el resto de la clase."

"Tarde o temprano acabaría perdiendo el interés."

"Después de todo..."

"Nadie me creeria si les dijera que......"

camera at sacudida

"¡¡¡¡AHHHHHH!!!!"

"Deje escapar un fuerte grito"

"El dolor hizo que me levantara del asiento"

"Rapidamente voltie hacia los asientos de atras"

"Tu..."

$ escena.show(
    "kuki_grin_looking_right",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)
ccc "Ah... jejeje."
$ escena.show(
    "kuki_smile",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)
$ escena.hide("kuki_grin_looking_right"
)

ccc "Se me paso la mano."



$ escena.hide("kuki_smile"
)



$ escena.hide("kuki_grin_looking_right", transition = dissolve
)

"Si seras......"

"Espera....."



"Todos el salon giraba a verme."

"Eso significa que...."

$ escena.show(
    "alice_formal_thinking",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

prof "¿Pasa algo...?"

$ escena.hide("alice_formal_thinking", transition = dissolve
)

"Esto era lo peor que podia pasarme"

"Tenia que explicarle lo que habia ocurrido"

"Y rapido"

"No.. yo solo estaba sentado y ella....."

"Pero no podia dejar de tartamudear"

"Mire en la direccion del problema"

$ escena.show(
    "kuki_looking_open_mouth",
    POS_CEN,
    PLANO_CERCANO
)
"¡AHHHHH!."

"¡¡fingiendo prestar atencion a la clase!!."
$ escena.hide("kuki_looking_open_mouth"
)

$ escena.show(
    "kuki_fake_smile",
    POS_CEN,
    PLANO_CERCANO,
    temblor_leve
)

"Despues de todo lo que hiciste..."

$ escena.hide("kuki_fake_smile"
)



"¡¡Para de finjir!!"

$ escena.show(
    "alice_formal_serious ",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)

prof "Silencio"

"...."

$ escena.hide("alice_formal_serious"
)

$ escena.show("alice_formal_thinking ",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

"¿Podria hacerme el favor de no interrumpir la clase?"

"...Si, No lo volvere a hacer"

#agregar aqui a alice forma parpadeando

$ escena.hide("alice_formal_thinking"
)

$ escena.show(
    "alice_formal_R ",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

prof "Perfecto"

"Entonces, donde nos habiamos quedado...."

$ escena.hide("alice_formal_R",transition = dissolve)

"La profesora volvio a dictar sus clases, mientras yo no podia quitarme este amargo sabor de boca"

"Habia llegado tarde, y ahora habia sido regañado en frente de todos"

"Tierra tragame...."

"Pero estaba vez, no habia sido culpa mia..."

"Cuando mire de reojo hacia atras"

$ escena.show(
    "kuki_boring_R",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

"...."

$ escena.show(
    "kuki_boring",
    POS_CEN,
    PLANO_CERCANO
)
$ escena.hide("kuki_boring_R"
)

"...."

$ escena.hide("kuki_boring_R",transition = dissolve)

$ escena.show(
    "kuki_smile_eyes_closed",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)

$ escena.hide("kuki_boring"
)

"Estaba riendose la muy desgraciada...."

$ escena.hide("kuki_smile_eyes_closed",transition = dissolve)

"Esto no se podia quedar asi..."

"Luego de pensarlo por un momento..."

"Lo tenia, el plan perfecto"

"Mientras la profesora seguia dictando sus clases, susurre lo suficientemente bajo como para que se me eschara"

"Sabes..., realmente vi algo antes de llegar"


$ escena.show(
    "kuki_boring_R",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

$ escena.show(
    "kuki_boring",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

ccc "..."

$ escena.hide("kuki_boring_R", transition = dissolve)
$ escena.hide("kuki_boring", transition = dissolve)

"Parece que capte su atencion."

"Perfecto..."

"Continue susurrando"

"Ah...realmente no puedo dejar de pensar en eso, sabes"

"Es algo que no se ve todos los dias"

$ escena.show(
    "kuki_embarrassed",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

ccc "..."

$ escena.hide("kuki_embarrassed", transition = dissolve)


"Aun que mis palabras despertaron su curiosidad, a su vez, ella parecia dudar de mi historia"

"Tenia que actuar rapido"

"Me recline un poco hacia atrás y la llame con un ligero gesto"

$ escena.show(
    "kuki_boring",
    POS_CEN,
    PLANO_MEDIO,
    transition=dissolve
)

$ escena.show(
    "kuki_idle_HB",
    POS_CEN,
    PLANO_CERCANO,
    transition=dissolve
)

$ escena.hide("kuki_boring", transition = dissolve)
$ escena.hide("kuki_idle_HB", transition = dissolve)


"Ella lo entendio de inmediato"

"cuando su cara estaba cerca empecé a susúrrarle algo al oído"

"En la entrada vi una....."

$ escena.show(
    "kuki_surprised",
    POS_CEN,
    PLANO_CERCANO,
    brinco
)

"—¿¿CHICA DESNUDA??"

$ escena.hide("kuki_surprised", transition = dissolve)

"Ella grito aun mas fuerte que yo habia pensando."

"Ahora todos tenian su atencion en una sola persona"

"varios chicos miraban hacia todas direcciones con caras que decían ¿Donde, donde?."

"Ella de inmediatamente tapo su boca"

"pero ya era demasiado tarde."

$ escena.show(
    "alice_formal_serious",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve
)

$ escena.show(
    "kuki_embarrassed_looking_right",
    POS_DER,
    PLANO_CERCANO,
    transition = dissolve
)

prof "Alunma kuki, ¿que acaba de decir?"

k "Ah....."

$ escena.hide ("kuki_embarrassed_looking_right")

$ escena.show(
    "kuki_embarrassed_open_mouth",
    POS_DER,
    PLANO_CERCANO,
    transition = dissolve
)

k "bueno, vera...."

$ escena.hide ("alice_formal_serious")

$ escena.show(
    "alice_formal_thinking",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve
)

"No hace falta que lo digas"

"De seguro otra vez no estubistes prestando atencion"

$ escena.hide("kuki_embarrassed_open_mouth")

$ escena.show(
    "kuki_embarrassed_looking_right",
    POS_DER,
    PLANO_CERCANO,
    transition = dissolve
)

ccc "Je je je"

$ escena.hide ("kuki_embarrassed_looking_right")

"Así fue como me recline en mi asiento, mientras esperaba ver el desenlace."

"Sin traicionar a mis expectativas, la maestra hizo que Kuki se levantara de su asiento"

"Te lo ganaste"

"Eso queria decir"

"pero la profesora seguia escuchando"

$ escena.hide("alice_formal_thinking")

$ escena.show(
    "alice_formal_serious",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve
)

prof "Entiendo"

$ escena.hide("alice_formal_serious")

$ escena.show(
    "alice_formal_thinking",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve
)

prof "si tenias tiempo para pensar en esas cosas"

prof "No tendraas problemas para mencionar algo de lo que vimos en clase"

ccc"..."

$ escena.hide("kuki_embarrassed_open_mouth")

$ escena.show(
    "kuki_boring",
    POS_DER,
    PLANO_CERCANO
)
ccc "Entiendo...."

$ escena.hide("alice_formal_thinking", transition = dissolve)

$ escena.hide("kuki_boring", transition = dissolve)






# "Hace aproximadamente tres mil años, una pequeña nación declaró la guerra al resto del mundo."

# "A simple vista no parecía una amenaza. Su territorio era reducido, su población escasa. "

# "Sin embargo, poseían algo desafiaba todo lo que la humanidad conocía."

# "Rodeando su país se alzaba una inmensa barrera de energía. Ninguna arma conocida podía atravesarla."

# "Balas, misiles, proyectiles e incluso los armamentos más avanzados eran repelidos y devueltos a sus atacantes."

# "Era un domo impenetrable."

# "Con semejante poder en sus manos, aquella nación lanzó un ultimátum al mundo."

# "Todos debían someterse a su autoridad."

# "Quienes se negaran serían eliminados."

# "Las guerras que siguieron dejaron cicatrices imborrables."

# "Millones de vidas se perdieron en intentos desesperados por derribar una defensa imposible de vulnerar."

# "Con el paso de los meses, una dolorosa verdad se hizo evidente: la humanidad no podía ganar."

# "La derrota parecía inevitable."

# "Entonces apareció una esperanza."

# "Un grupo de científicos"

# "liderado por una brillante investigadora cuyas contribuciones ya habían transformado innumerables campos de estudio"

# "logró descubrir una posible debilidad en la barrera. Era una oportunidad única. Quizá la última."

# "Pero el tiempo se estaba agotando."

# "Cada día que pasaba acercaba al mundo a la extinción."

# "Comprendiendo la gravedad de la situación, el equipo tomó una decisión de la que no habría regreso. Si querían salvar a la humanidad, tendrían que actuar de inmediato."

# "Partieron hacia el territorio enemigo llevando consigo la única herramienta capaz de poner fin a la amenaza."

# "Contra todo pronóstico, lograron atravesar la barrera."

# "Pero fueron detectados."

# "Antes de que pudieran alcanzar su objetivo"

# "las defensas enemigas desplegaron un gigantesco campo de fuerza alrededor de su aeronave. "

# "Desde el otro lado, los gobernantes de aquella nación anunciaron que ellos serían los primeros testigos del destino reservado para quienes se opusieran a su dominio."

# "Atrapados."

# "Sin posibilidad de escapar."

# "Sin tiempo para intentar otra estrategia."

# "Los científicos tomaron la decisión más difícil."

# "su ultima carta"

# "Activaron una bomba que train con ellos."

# "La explosión fue tan colosal que muchos creyeron que borraría del mapa una parte del planeta."

# "Sin embargo, la barrera contuvo toda la energía liberada."

# "Cuando la luz finalmente se desvaneció, solo quedó un inmenso vacío esférico en el lugar donde antes existía aquella nación."

# "No quedaron ciudades."

# "No quedaron edificios."

# "No quedó absolutamente nada."

# "Así fue como aquel grupo de científicos entregó sus vidas para salvar al mundo."

# "Miles de años después, sus nombres siguen siendo recordados como los de los mayores héroes de la historia."

# "Fueron los salvadores de la humanidad, los pioneros de la civilización moderna y el símbolo de que incluso frente a una derrota segura"

# "En honor a su legado"

# "la humanidad dedicó los siglos siguientes a aquello por lo que ellos lucharon: la búsqueda incansable del conocimiento."

# "Y hasta el día de hoy, seguimos avanzando, desarrollando nuevas tecnologías y explorando los límites de lo posible"

# "guiados por el mismo espíritu que permitió a nuestros salvadores cambiar el destino del mundo."

$ escena.hide("kuki_boring")

"Pasaron unos minutos"

$ escena.show(
    "alice_formal_idle",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve)


$ escena.show(
    "kuki_idle",
    POS_DER,
    PLANO_CERCANO,
    transition = dissolve)
    
k"Este seria el resumen de la clase."

"...."

"Su resumen habia sido impecable...."



$ escena.hide("alice_formal_thinking")



$ escena.show(
    "alice_formal_idle",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve)

"la maestra se mostraba levemente conmovida por aquellas palabras"

prof "Todos de pie"

$ escena.hide("alice_formal_idle")

$ escena.show(
    "alice_formal_thinking",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve)

$ escena.hide("kuki_idle")

$ escena.show(
    "kuki_idle_eyes_closed",
    POS_DER,
    PLANO_CERCANO,
    transition = dissolve)

prof"denle un aplauso a su compañera, por su magnifico dominio de nuestra historia"



$ escena.hide("alice_formal_thinking",
transition = dissolve)

$ escena.hide("kuki_idle_eyes_closed",
transition = dissolve)

"¿Pero como....?"

"Ahora tenia que felicitarla...."

"Obiviamente no quería hacerlo"

"era como admitir que había perdido."

"De inmediato todos se pararon y dieron un único aplauso que resonó por todo el aula"

"Eso me incluyo"

"Antes de que volvería a tomar asiento, la maestra hablo"

$ escena.show(
    "alice_formal_thinking",
    POS_IZQ,
    PLANO_CERCANO,
    transition = dissolve)



prof "Alumno Yuu"

y "!...¡"

prof"No pude evitar ver que estubo distraido durante toda la explicacion"

"Se habia dado cuenta..."

"Me habia sido imposible manterme concentrado"

"Despues de todo"

"Nunca antes habia visto a kuki de esa manera"

prof "Veamos..."

prof "como el día de hoy también llego tarde"

prof "debería de asignarle un castigo."

"Castigo...?"

"Mi rostro se volvió pálido."

prof "Al final de la clase, deberá entregarme un informe sobre lo que su compañera expuso"

prof "Me interesa saber su oponion"

$ escena.hide("alice_formal_thinking")

"Em..."

"Claro...."

"Antes de que Kuki volviera a su pupitre, me dio una ultima mirada"


$ escena.show(
    "kuki_idle",
    POS_CEN,
    PLANO_CERCANO,
    transition = dissolve)

$ escena.hide("kuki_idle")

$ escena.show(
    "kuki_teasing",
    POS_CEN,
    PLANO_CERCANO,
    brinco)

ccc "..."

"Gane esta vez" 

"Aun que no lo dijo"

"Eso es lo que se veia en su mirada"

$ escena.hide("kuki_teasing", transition = dissolve)


camera at sacudida

"Golpie mi cara contra el pupitre"

"Completamente derrotado"

"mientras la clase continuba con naturalidad"

stop music

jump part_04
