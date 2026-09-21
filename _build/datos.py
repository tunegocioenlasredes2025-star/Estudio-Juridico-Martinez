"""Contenido del sitio. Todo lo que cambia a menudo está acá; el HTML lo arma build.py."""

NOMBRE = "Estudio Jurídico Martínez"
SITIO = "https://estudio-juridico-martinez.vercel.app"  # cambiar cuando tenga dominio propio
WHATSAPP = "5491132176540"
TEL_VISIBLE = "11 3217-6540"
INSTAGRAM = "https://www.instagram.com/estudio.juridico.martinez/"
DIRECCION = "Av. José de San Martín 3285"
LOCALIDAD = "Merlo"
CP = "B1722"
PROVINCIA = "Provincia de Buenos Aires"
MAPS = "https://www.google.com/maps/place/Estudio+Jur%C3%ADdico+Mart%C3%ADnez/@-34.688243,-58.7337533,17z/data=!4m6!3m5!1s0x95bcc1347b861acb:0xb00a913527b144bb!8m2!3d-34.688243!4d-58.7337533"
MAPS_EMBED = "https://www.google.com/maps?q=Estudio+Jur%C3%ADdico+Mart%C3%ADnez,+Av.+Jos%C3%A9+de+San+Mart%C3%ADn+3285,+Merlo&output=embed"
LAT, LNG = -34.688243, -58.7337533
FUNDACION = 1976
# El de la puerta del estudio (Maps dice otro: ver insumos/dudas.md)
HORARIOS = [
    ("Lunes a viernes", "13:30 a 19:30"),
    ("Sábados", "con cita previa"),
]
HORARIO_SCHEMA = [{"dias": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "abre": "13:30", "cierra": "19:30"}]

OPINIONES = [
    ("N. L.", "Excelente servicio. Súper profesional y amable. Lo recomiendo 100%."),
    ("Christian S.", "Excelente profesional. Muy recomendable."),
    ("Brenda", "Excelente profesional, recomiendo sin dudas."),
]
PUNTAJE = "5,0"

# ------------------------------------------------------------------ áreas
AREAS = [
    {
        "slug": "familia",
        "nombre": "Familia",
        "foto": "equipo-familia",
        "titulo": "Abogada de familia en Merlo",
        "lema": "Cuando cambia la familia, que no se desordene todo lo demás.",
        "resumen": "Divorcios, cuota alimentaria, régimen de comunicación, plan de parentalidad, uniones convivenciales, violencia familiar y sucesiones.",
        "intro": ("Una separación, un reclamo de alimentos o la organización de la vida de los chicos no son "
                  "solo trámites: son momentos difíciles. Te explicamos qué opciones tenés, en palabras "
                  "claras, y buscamos el acuerdo siempre que sea posible. Cuando no lo es, lo llevamos "
                  "adelante en los tribunales de familia."),
        "meta": "Abogada de familia en Merlo: divorcios, cuota alimentaria, régimen de comunicación, plan de parentalidad, violencia familiar y sucesiones. Estudio Jurídico Martínez, desde 1976.",
        "temas": [
            ("divorcio", "Divorcio",
             "En Argentina el divorcio no necesita causa ni el acuerdo del otro: puede pedirlo uno solo o los dos juntos. "
             "Lo que sí hay que presentar es una propuesta sobre cómo quedan los hijos, la vivienda y los bienes.",
             ["Divorcio de común acuerdo o pedido por uno solo", "Propuesta de convenio regulador",
              "División de bienes de la sociedad conyugal", "Atribución de la vivienda familiar",
              "Compensación económica"]),
            ("alimentos", "Cuota alimentaria",
             "Los hijos tienen derecho a alimentos hasta los 21 años, y hasta los 25 si estudian y eso les impide mantenerse. "
             "Pedimos que se fije la cuota, que se actualice o que se cobre la que se debe.",
             ["Fijación de la cuota", "Aumento o reducción", "Ejecución de cuotas atrasadas",
              "Alimentos provisorios mientras dura el juicio", "Alimentos durante el embarazo"]),
            ("cuidado-personal", "Cuidado personal y régimen de comunicación",
             "Con quién viven los chicos, cómo y cuándo ven al otro progenitor, qué pasa en vacaciones y fiestas. "
             "Lo ideal es acordarlo por escrito para evitar discusiones después.",
             ["Cuidado personal compartido o unilateral", "Régimen de comunicación",
              "Plan de parentalidad", "Permisos de viaje y cambios de domicilio",
              "Incumplimientos del régimen"]),
            ("convivencia", "Uniones convivenciales",
             "Las parejas que conviven sin casarse también tienen derechos. Te asesoramos para registrar la unión, "
             "firmar un pacto de convivencia o resolver qué pasa con la casa y los bienes cuando la pareja termina.",
             ["Pactos de convivencia", "Protección de la vivienda familiar",
              "Compensación económica al terminar la unión", "Reconocimiento de la unión"]),
            ("violencia-familiar", "Violencia familiar",
             "La denuncia es el primer paso, no el último. Después aparecen preguntas urgentes: alimentos, contacto con los hijos, "
             "quién decide sobre la escuela o la salud. Te acompañamos con cuidado y reserva en todo el proceso.",
             ["Medidas de protección (exclusión del hogar, prohibición de acercamiento)",
              "Alimentos y cuidado de los hijos mientras dura la medida",
              "Seguimiento y pedido de prórroga de las medidas", "Acompañamiento con total reserva"]),
            ("sucesiones", "Sucesiones",
             "Cuando fallece un familiar hay que iniciar la sucesión para que los herederos puedan disponer de los bienes: "
             "la casa, el auto, las cuentas. Nos ocupamos de todo el trámite, de principio a fin.",
             ["Declaratoria de herederos", "Sucesiones con testamento",
              "Inscripción de inmuebles y automotores a nombre de los herederos",
              "Partición de bienes entre herederos"]),
        ],
        "faq": [
            ("¿Me puedo divorciar si mi pareja no quiere?",
             "Sí. Desde 2015 el divorcio se puede pedir de forma unilateral, sin explicar la causa y sin esperar plazos. "
             "El otro no puede impedirlo: solo puede discutir cómo se resuelven los efectos (hijos, bienes, vivienda)."),
            ("¿Hasta qué edad se pagan alimentos?",
             "Hasta los 21 años. Si el hijo estudia o se capacita y eso no le permite mantenerse, puede extenderse hasta los 25."),
            ("¿Qué es un plan de parentalidad?",
             "Es un acuerdo escrito que organiza la vida de los chicos después de la separación: dónde viven, cómo se reparten "
             "los días, las vacaciones, la escuela y la salud. Se puede homologar para que tenga fuerza de sentencia."),
            ("Hice la denuncia por violencia, ¿y ahora qué?",
             "Hay que ordenar lo urgente: que las medidas de protección se cumplan y no venzan, y resolver alimentos y "
             "cuidado de los hijos. Escribinos y lo vemos con prioridad y total reserva."),
        ],
    },
    {
        "slug": "laboral",
        "nombre": "Laboral",
        "foto": "equipo-laboral",
        "titulo": "Abogada laboral en Merlo",
        "lema": "Si te despidieron o te accidentaste trabajando, tenés derechos y tenés plazos.",
        "resumen": "Despidos, liquidaciones finales, accidentes de trabajo y ART, trabajo no registrado, violencia laboral y asesoramiento a empresas.",
        "intro": ("Revisamos tu liquidación y te decimos si está bien calculada. Si no lo está, reclamamos lo que "
                  "te corresponde: primero con un telegrama y una negociación, y si hace falta, en juicio. "
                  "También asesoramos a comercios y pymes de la zona para que cumplan y eviten conflictos."),
        "meta": "Abogada laboral en Merlo: despidos, indemnizaciones, liquidación final, accidentes de trabajo y ART, trabajo en negro y violencia laboral. Estudio Jurídico Martínez.",
        "temas": [
            ("despidos", "Despidos e indemnizaciones",
             "Si te despidieron sin causa, te corresponde una indemnización por antigüedad, el preaviso y la integración del mes. "
             "Controlamos las cuentas y reclamamos las diferencias.",
             ["Despido sin causa o con causa discutible", "Despido indirecto (cuando el empleador incumple)",
              "Intercambio de telegramas y cartas documento", "Reclamos por diferencias"]),
            ("liquidaciones", "Liquidación final",
             "Antes de firmar, traé la liquidación. Revisamos vacaciones no gozadas, aguinaldo proporcional, "
             "horas extra y todo lo que tiene que figurar.",
             ["Control de la liquidación final", "Vacaciones y aguinaldo proporcionales",
              "Horas extra y categoría mal liquidada", "Certificado de trabajo"]),
            ("art", "Accidentes de trabajo y ART",
             "Si te lesionaste trabajando o en el trayecto, la ART tiene que cubrirte la atención y, si queda una "
             "secuela, pagarte una indemnización. Te acompañamos en la comisión médica y en el reclamo.",
             ["Accidentes de trabajo e in itinere", "Enfermedades profesionales",
              "Comisiones médicas", "Rechazos de la ART"]),
            ("trabajo-no-registrado", "Trabajo no registrado",
             "Trabajar en negro o con un sueldo menor al que figura en el recibo te da derecho a reclamar. "
             "Te explicamos cómo probarlo y cómo hacerlo.",
             ["Trabajo en negro total o parcial", "Fecha de ingreso mal registrada",
              "Aportes no depositados"]),
            ("violencia-laboral", "Violencia laboral",
             "El maltrato, el acoso o la persecución en el trabajo no son parte del empleo. Te asesoramos sobre "
             "cómo documentarlo y qué caminos tenés.",
             ["Acoso y hostigamiento", "Acoso sexual en el trabajo", "Discriminación"]),
            ("empresas", "Asesoramiento a empresas",
             "Para comercios y pymes: contratos, registración, sanciones, despidos bien hechos y respuesta a reclamos. "
             "Prevenir sale mucho más barato que un juicio.",
             ["Contratación y registración", "Apercibimientos y sanciones",
              "Desvinculaciones", "Respuesta a telegramas y reclamos"]),
        ],
        "faq": [
            ("¿Cuánto tiempo tengo para reclamar?",
             "En general, dos años desde que se generó el derecho. Pero algunos pasos, como responder un telegrama, "
             "tienen plazos de días. Por eso conviene consultar apenas pasa."),
            ("¿Tengo que firmar la liquidación final?",
             "Podés firmar como constancia de que la recibiste, sin renunciar a reclamar diferencias. Si tenés dudas, "
             "mandanos una foto antes de firmar."),
            ("Me accidenté yendo al trabajo, ¿me cubre la ART?",
             "Sí, el accidente en el trayecto entre tu casa y el trabajo está cubierto. Hay que denunciarlo cuanto antes."),
        ],
    },
    {
        "slug": "civil-comercial",
        "nombre": "Civil y comercial",
        "foto": "equipo-civil",
        "titulo": "Abogada civil y comercial en Merlo",
        "lema": "Contratos claros, alquileres en regla y daños que se reparan.",
        "resumen": "Contratos, alquileres, sociedades, daños y perjuicios, accidentes de tránsito y cobro de deudas.",
        "intro": ("Redactamos y revisamos contratos antes de que los firmes, resolvemos conflictos de alquiler "
                  "y reclamamos por los daños que te causaron. Para comercios y emprendimientos, armamos y "
                  "acompañamos la sociedad desde el primer día."),
        "meta": "Abogada civil y comercial en Merlo: contratos, alquileres, desalojos, sociedades, daños y perjuicios y accidentes de tránsito. Estudio Jurídico Martínez, desde 1976.",
        "temas": [
            ("contratos", "Contratos",
             "Un contrato bien escrito evita la mayoría de los conflictos. Redactamos y revisamos contratos de "
             "compraventa, boletos, préstamos y servicios.",
             ["Boletos de compraventa", "Contratos de servicios y préstamos",
              "Revisión antes de firmar", "Incumplimientos"]),
            ("alquileres", "Alquileres",
             "Para propietarios e inquilinos: contratos, garantías, actualizaciones, devolución del depósito y desalojos.",
             ["Contratos de locación", "Desalojos", "Cobro de alquileres adeudados",
              "Devolución del depósito"]),
            ("sociedades", "Sociedades",
             "Constitución de sociedades, estatutos, acuerdos entre socios y conflictos societarios.",
             ["Constitución de SRL y SAS", "Acuerdos entre socios", "Modificaciones y cesiones",
              "Conflictos entre socios"]),
            ("danos", "Daños y perjuicios",
             "Si te causaron un daño, en tu persona o en tus bienes, tenés derecho a que te lo reparen. "
             "Reclamamos a quien corresponda y a su aseguradora.",
             ["Accidentes de tránsito", "Reclamos a aseguradoras", "Daños en la vivienda",
              "Mala praxis y responsabilidad"]),
            ("deudas", "Cobro de deudas",
             "Cheques, pagarés, facturas y préstamos impagos: intimamos, negociamos y, si hace falta, ejecutamos.",
             ["Cheques y pagarés", "Cartas documento", "Juicios ejecutivos"]),
        ],
        "faq": [
            ("Tuve un choque, ¿qué hago primero?",
             "Sacá fotos, anotá los datos del otro conductor y de su seguro, y hacé la denuncia a tu aseguradora dentro "
             "de los tres días. Después escribinos: el reclamo contra el seguro del otro se puede iniciar enseguida."),
            ("El inquilino no paga, ¿cómo lo desalojo?",
             "Primero se lo intima formalmente a pagar. Si no paga, se inicia el juicio de desalojo. Cuanto antes se "
             "empiece, menos deuda se acumula."),
        ],
    },
]

AREA = {a["slug"]: a for a in AREAS}

# ------------------------------------------------------------------ primera consulta
PASOS = [
    ("Escribinos", "Por WhatsApp, contanos en dos líneas qué te pasa. No hace falta que sepas cómo se llama tu tema."),
    ("Coordinamos la entrevista", "En el estudio de Av. San Martín 3285, o por videollamada si te queda más cómodo."),
    ("Te explicamos las opciones", "Qué se puede hacer, cuánto puede tardar y cuánto cuesta. Sin letra chica."),
    ("Te acompañamos", "Si decidís avanzar, te mantenemos al tanto de cada paso del expediente."),
]

LLEVAR = [
    ("Tu DNI", "Y el de las personas involucradas, si lo tenés (por ejemplo, de tus hijos)."),
    ("Los papeles que tengas", "Actas, recibos de sueldo, contratos, telegramas, denuncias, fotos. Aunque te parezcan de más."),
    ("Una línea de tiempo", "Las fechas importantes anotadas en orden: cuándo empezó, qué pasó después."),
    ("Tus preguntas por escrito", "En la consulta es fácil olvidarse. Anotalas antes."),
    ("Qué querés lograr", "Pensar el resultado que buscás nos ayuda a proponerte el mejor camino."),
    ("Mensajes o audios", "Si hay conversaciones importantes, guardalas. No las borres."),
]

FAQ_GENERAL = [
    ("¿Atienden solo en Merlo?",
     "El estudio está en Merlo y atendemos a vecinos de Merlo, Padua, Libertad, Pontevedra, Ituzaingó, Moreno y "
     "alrededores. Muchas consultas se pueden hacer por videollamada."),
    ("¿Lo que cuento es confidencial?",
     "Siempre. El secreto profesional nos obliga a reservar todo lo que nos cuentes, hayas contratado o no."),
    ("¿Cómo pido una consulta?",
     "Escribinos por WhatsApp al " + TEL_VISIBLE + " y coordinamos día y horario."),
]
