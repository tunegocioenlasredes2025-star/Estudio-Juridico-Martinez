"""Contenido del sitio. Todo lo que cambia a menudo está acá; el HTML lo arma build.py.

Tono: calmo, claro y humano. Sin promesas de resultado, sin honorarios como gancho
y sin comparaciones con otros estudios (lo pide la ética profesional del Colegio de Abogados).
"""

NOMBRE = "Estudio Jurídico Martínez"
SITIO = "https://estudio-juridico-martinez-merlo.vercel.app"  # cambiar cuando tenga dominio propio
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
FUNDADOR = "Miguel Ángel Martínez"
A_CARGO = "María José Martínez"
ZONA = ["Merlo", "San Antonio de Padua", "Libertad", "Pontevedra", "Ituzaingó", "Moreno"]
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

# ------------------------------------------------------------------ familia
# Cada tema de familia tiene página propia: son las búsquedas concretas de la gente.
TEMAS_FAMILIA = [
    {
        "slug": "divorcio",
        "nombre": "Divorcio",
        "titulo": "Divorcio en Merlo",
        "meta": "Divorcio en Merlo: cómo es el trámite, qué se resuelve sobre los hijos, la vivienda y los bienes. Estudio Jurídico Martínez, en Merlo desde 1976.",
        "resumen": "Lo puede pedir uno solo de los dos o los dos juntos, sin tener que explicar los motivos.",
        "intro": [
            "En Argentina el divorcio no necesita una causa ni el acuerdo de la otra persona. Lo puede pedir uno solo "
            "de los dos, o los dos juntos, y no hay que probar nada de lo que pasó en la pareja.",
            "Junto con el pedido se presenta una propuesta sobre los temas que quedan abiertos: cómo se organiza la vida "
            "de los hijos, qué pasa con la vivienda y cómo se reparten los bienes. Si están de acuerdo, se presenta un "
            "convenio firmado por los dos. Si no lo están, cada uno presenta su propuesta y esos puntos se discuten aparte, "
            "sin frenar el divorcio.",
            "En la primera entrevista te explicamos en qué situación estás, qué caminos hay y qué implica cada uno.",
        ],
        "puntos": ["Divorcio pedido por los dos o por uno solo", "Convenio regulador", "Uso de la vivienda familiar",
                   "Compensación económica", "Homologación de acuerdos", "Divorcios con bienes o comercios en común"],
        "faq": [
            ("¿Puedo divorciarme si la otra persona no quiere?",
             "Sí. El divorcio se puede pedir de forma unilateral y la otra parte no puede impedirlo. Lo que sí se puede "
             "discutir son los efectos: los hijos, la vivienda y los bienes."),
            ("¿Cuánto tarda?",
             "Depende de si hay acuerdo y de los tiempos del juzgado. Cuando las dos partes acuerdan, el trámite es "
             "bastante más corto. En la entrevista te damos una idea realista según tu caso."),
            ("¿Hace falta ir al juzgado?",
             "En general no tenés que estar presente en cada paso: el trámite lo lleva el estudio. Te avisamos si en "
             "algún momento se necesita tu presencia."),
        ],
    },
    {
        "slug": "tenencia-y-regimen-de-comunicacion",
        "nombre": "Tenencia y régimen de comunicación",
        "titulo": "Tenencia de hijos y régimen de comunicación en Merlo",
        "meta": "Tenencia (hoy cuidado personal) y régimen de comunicación en Merlo: con quién viven los chicos, cómo se organizan los días, viajes y vacaciones. Estudio Jurídico Martínez.",
        "resumen": "Con quién viven los chicos y cómo se organizan los días con cada progenitor.",
        "intro": [
            "Lo que mucha gente conoce como “tenencia” hoy se llama cuidado personal. Es la decisión sobre con quién "
            "viven los chicos en el día a día, y puede ser compartida entre los dos progenitores o quedar a cargo de uno, "
            "con un régimen de comunicación para el otro.",
            "El régimen de comunicación ordena lo concreto: qué días, cómo son las vacaciones y las fiestas, quién retira "
            "de la escuela, qué pasa si uno quiere viajar con los chicos. Tenerlo por escrito y homologado evita "
            "discusiones más adelante.",
            "Cuando hay acuerdo, se arma un plan de parentalidad y se presenta para que el juzgado lo homologue. Cuando no "
            "lo hay, se plantea ante el juzgado de familia.",
        ],
        "puntos": ["Cuidado personal compartido o a cargo de uno", "Régimen de comunicación", "Plan de parentalidad",
                   "Vacaciones, fiestas y viajes", "Autorizaciones para viajar", "Incumplimientos del régimen"],
        "faq": [
            ("¿“Tenencia” y “cuidado personal” son lo mismo?",
             "Sí. Es el mismo tema con el nombre que usa la ley desde 2015. Si buscás “tenencia”, estás buscando esto."),
            ("¿El cuidado compartido significa mitad y mitad?",
             "No necesariamente. Compartido quiere decir que los dos siguen decidiendo y ocupándose; cómo se reparten los "
             "días depende de cada familia, de las edades y de las rutinas."),
            ("¿Se puede cambiar un régimen que ya está?",
             "Sí. Si cambiaron las circunstancias (mudanzas, horarios, edades de los chicos), se puede pedir que se "
             "modifique."),
        ],
    },
    {
        "slug": "cuota-alimentaria",
        "nombre": "Cuota alimentaria",
        "titulo": "Cuota alimentaria en Merlo",
        "meta": "Cuota alimentaria en Merlo: cómo se fija, cómo se actualiza y qué hacer si no la pagan. Estudio Jurídico Martínez, en Merlo desde 1976.",
        "resumen": "Fijarla, actualizarla o reclamar la que no se paga, para hijos hasta los 21 años (o 25 si estudian).",
        "intro": [
            "Los alimentos cubren lo que hace falta para la vida de los chicos: comida, vivienda, ropa, salud, escuela y "
            "también su recreación. Corresponden hasta los 21 años, y hasta los 25 si el hijo estudia o se capacita y eso "
            "no le permite mantenerse solo.",
            "La cuota se puede acordar entre los progenitores y homologar, o pedirla ante el juzgado. También se puede "
            "pedir que se actualice cuando quedó vieja, o reclamar las cuotas que no se pagaron.",
            "Traé lo que tengas a mano sobre gastos e ingresos: con eso podemos plantear un pedido realista.",
        ],
        "puntos": ["Acuerdo de cuota y homologación", "Pedido de cuota ante el juzgado", "Aumento o reducción",
                   "Cobro de cuotas atrasadas", "Alimentos provisorios mientras dura el trámite",
                   "Alimentos durante el embarazo"],
        "faq": [
            ("¿Hasta qué edad se paga?",
             "Hasta los 21 años. Si el hijo estudia o se capacita y eso le impide mantenerse, puede extenderse hasta los 25."),
            ("El padre o la madre trabaja en negro, ¿igual se puede reclamar?",
             "Sí. Cuando no hay recibos, la cuota se plantea a partir de otros elementos: el nivel de vida, los gastos de "
             "los chicos y lo que se pueda acreditar. Contanos tu caso y lo vemos."),
            ("¿Qué pasa si no paga lo que se acordó?",
             "Se puede reclamar el cobro de lo adeudado. La ley prevé distintas medidas para los incumplimientos; en la "
             "entrevista te explicamos cuáles se aplican a tu situación."),
        ],
    },
    {
        "slug": "violencia-familiar",
        "nombre": "Violencia familiar",
        "titulo": "Violencia familiar en Merlo",
        "meta": "Violencia familiar en Merlo: medidas de protección, qué pasa después de la denuncia y cómo se ordenan los alimentos y el contacto con los hijos. Estudio Jurídico Martínez.",
        "resumen": "Medidas de protección y lo que viene después de la denuncia: alimentos, hijos, vivienda.",
        "intro": [
            "Si estás atravesando una situación de violencia, lo primero es tu seguridad. Se pueden pedir medidas de "
            "protección ante el juzgado de familia, como la exclusión del hogar, la prohibición de acercamiento o un "
            "botón antipánico.",
            "La denuncia no cierra el tema: después aparecen preguntas que también son urgentes. Con qué se sostiene la "
            "casa, qué pasa con los alimentos, cómo se organiza el contacto de los chicos con el otro progenitor, quién "
            "decide sobre la escuela o la salud.",
            "Te acompañamos en ese camino con reserva y sin apuro, al ritmo que puedas.",
        ],
        "aviso": "Si estás en peligro en este momento, llamá al 911. La línea 144 atiende las 24 horas, "
                 "todos los días y en todo el país, de forma gratuita y confidencial.",
        "puntos": ["Medidas de protección", "Exclusión del hogar y prohibición de acercamiento",
                   "Pedido de prórroga de las medidas", "Alimentos y cuidado de los hijos durante el proceso",
                   "Acompañamiento con total reserva"],
        "faq": [
            ("Ya hice la denuncia, ¿necesito un abogado?",
             "Podés hacer la denuncia sin abogado, pero para lo que sigue (que las medidas se cumplan y no venzan, "
             "alimentos, cuidado de los hijos) conviene tener asesoramiento."),
            ("¿Lo que cuento queda entre nosotros?",
             "Sí. El secreto profesional nos obliga a reservar todo lo que nos cuentes, contrates o no al estudio."),
        ],
    },
    {
        "slug": "uniones-convivenciales",
        "nombre": "Uniones convivenciales",
        "titulo": "Uniones convivenciales en Merlo",
        "meta": "Uniones convivenciales en Merlo: registro, pactos de convivencia, vivienda y qué pasa con los bienes cuando la pareja termina. Estudio Jurídico Martínez.",
        "resumen": "Parejas que conviven sin casarse: registro, pactos y qué pasa cuando la convivencia termina.",
        "intro": [
            "Convivir sin casarse también genera derechos y obligaciones. La ley reconoce la unión convivencial cuando la "
            "pareja convive de manera estable y pública, en general a partir de los dos años.",
            "Se puede registrar la unión y firmar un pacto de convivencia, que ordena por escrito cómo se manejan los "
            "gastos, la vivienda y los bienes mientras dura y si un día termina.",
            "Cuando la convivencia termina, aparecen los mismos temas que en una separación: la casa donde viven los "
            "chicos, los bienes que se compraron entre los dos y, en algunos casos, una compensación económica.",
        ],
        "puntos": ["Registro de la unión convivencial", "Pactos de convivencia", "Protección de la vivienda familiar",
                   "Bienes adquiridos durante la convivencia", "Compensación económica al terminar la unión"],
        "faq": [
            ("¿Cuánto tiempo hay que convivir para que la ley lo reconozca?",
             "Por lo general, dos años de convivencia estable y pública. Igual, cada situación se analiza con sus detalles."),
            ("Compramos cosas juntos y no está todo a mi nombre, ¿qué puedo hacer?",
             "Se puede reclamar sobre lo que se adquirió durante la convivencia. Traé lo que tengas (recibos, "
             "transferencias, mensajes) y lo revisamos."),
        ],
    },
    {
        "slug": "division-de-bienes",
        "nombre": "División de bienes",
        "titulo": "División de bienes en Merlo",
        "meta": "División de bienes después del divorcio en Merlo: bienes propios y gananciales, la casa, el auto y los comercios. Estudio Jurídico Martínez, desde 1976.",
        "resumen": "Qué le toca a cada uno después del divorcio: la casa, el auto, los ahorros, el comercio.",
        "intro": [
            "Con el divorcio termina el régimen de bienes del matrimonio y hay que liquidar lo que había en común. El "
            "primer paso es separar los bienes propios (los que cada uno traía o recibió por herencia o donación) de los "
            "gananciales (los que se adquirieron durante el matrimonio).",
            "Después se acuerda cómo se reparten: la vivienda, el auto, los ahorros, un comercio, las deudas. Si hay "
            "acuerdo, se firma un convenio y se homologa. Si no lo hay, la división se plantea ante el juzgado.",
            "También puede corresponder una compensación económica cuando el divorcio deja a uno de los dos en una "
            "situación claramente peor por el rol que ocupó durante el matrimonio.",
        ],
        "puntos": ["Bienes propios y gananciales", "Convenio de división y homologación", "Vivienda familiar",
                   "Vehículos, ahorros y comercios", "Deudas del matrimonio", "Compensación económica"],
        "faq": [
            ("La casa está solo a nombre de mi ex, ¿pierdo todo?",
             "No necesariamente. Si se compró durante el matrimonio, en general es ganancial más allá de a nombre de quién "
             "figure. Hay que ver cada caso con la documentación."),
            ("¿Se puede dividir sin juicio?",
             "Sí, si las dos partes acuerdan. Se firma un convenio y se presenta para su homologación."),
        ],
    },
]

AREA_FAMILIA = {
    "slug": "familia",
    "nombre": "Familia",
    "icono": "familia",
    "foto": "equipo-familia",
    "titulo": "Abogados de familia en Merlo",
    "lema": "Cuando cambia la familia, ordenar lo que sigue.",
    "resumen": "Divorcios, tenencia y régimen de comunicación, cuota alimentaria, violencia familiar, uniones convivenciales y división de bienes.",
    "meta": "Abogada de familia en Merlo: divorcio, cuota alimentaria, tenencia y régimen de comunicación, violencia familiar, uniones convivenciales y división de bienes. Estudio Jurídico Martínez, desde 1976.",
    "intro": [
        "El derecho de familia es lo que más consultas nos trae, y también lo que más se parece a la vida de todos los "
        "días: una separación, los chicos, la casa, el dinero que hace falta cada mes.",
        "Casi siempre, quien llega al estudio está pasando un momento difícil y nunca antes había hablado con un abogado. "
        "Por eso empezamos por escuchar y explicar: qué dice la ley en tu situación, qué caminos hay y qué implica cada uno. "
        "Buscamos el acuerdo cuando es posible, porque suele ser lo que menos desgasta a la familia. Cuando no lo es, "
        "planteamos el tema ante el juzgado de familia.",
    ],
    "temas": TEMAS_FAMILIA,
    "faq": [
        ("Nunca fui a un abogado, ¿cómo empiezo?",
         "Escribinos por WhatsApp contando en dos líneas qué te pasa y coordinamos una entrevista. No hace falta que sepas "
         "cómo se llama tu tema ni que traigas todo resuelto."),
        ("¿Qué documentación conviene llevar?",
         "Tu DNI, las partidas o actas que tengas (matrimonio, nacimiento de los hijos), y los papeles relacionados con el "
         "tema: recibos, escrituras, denuncias, mensajes. Si te falta algo, igual podemos empezar."),
        ("¿Se puede resolver sin llegar a juicio?",
         "Muchos temas de familia se resuelven con un acuerdo homologado por el juzgado. Cuando el acuerdo no es posible, "
         "se plantea el reclamo judicial."),
        ("¿Atienden también fuera de Merlo?",
         "El estudio está en Merlo y atendemos a vecinos de Merlo, Padua, Libertad, Pontevedra, Ituzaingó y Moreno. "
         "Muchas consultas se pueden hacer por videollamada."),
    ],
}

# ------------------------------------------------------------------ otras áreas
AREAS_SEC = [
    {
        "slug": "sucesiones",
        "nombre": "Sucesiones",
        "icono": "sucesiones",
        "foto": "diploma-uba",
        "titulo": "Sucesiones en Merlo",
        "lema": "Poner los bienes de la familia a nombre de quienes corresponde.",
        "resumen": "Declaratoria de herederos, sucesiones con testamento, inscripción de la casa y el auto, y partición entre herederos.",
        "meta": "Sucesiones en Merlo: declaratoria de herederos, sucesión con testamento, inscripción de inmuebles y automotores. Estudio Jurídico Martínez, desde 1976.",
        "intro": [
            "Cuando fallece un familiar, los bienes no pasan solos a nombre de los herederos: hace falta iniciar la "
            "sucesión. Recién con ella se puede vender o transferir la casa, el auto o disponer de las cuentas.",
            "Nos ocupamos del trámite completo, desde la apertura hasta la inscripción de los bienes, y te vamos "
            "contando en qué etapa está.",
        ],
        "temas": [
            ("declaratoria", "Declaratoria de herederos",
             "Es el trámite habitual cuando no hay testamento: el juzgado reconoce quiénes son los herederos.",
             ["Apertura de la sucesión", "Acreditación del vínculo", "Herederos en el exterior o que no se presentan"]),
            ("testamento", "Sucesión con testamento",
             "Cuando la persona dejó testamento, hay que presentarlo y cumplir sus pasos formales.",
             ["Presentación y validez del testamento", "Legítima de los herederos forzosos"]),
            ("inscripcion", "Inscripción de los bienes",
             "El paso final: que la casa, el terreno o el auto queden a nombre de los herederos.",
             ["Inscripción de inmuebles", "Inscripción de automotores", "Cuentas y bienes registrables"]),
            ("particion", "Partición entre herederos",
             "Cómo se reparte lo que quedó, por acuerdo entre los herederos o ante el juzgado si no lo hay.",
             ["Acuerdos de partición", "Venta de bienes de la sucesión", "Diferencias entre herederos"]),
        ],
        "faq": [
            ("¿Cuánto tarda una sucesión?",
             "Depende del juzgado, de la cantidad de herederos y de si están todos de acuerdo. En la entrevista te damos "
             "una idea según cómo esté tu caso."),
            ("Somos varios hermanos y no todos quieren iniciarla, ¿se puede igual?",
             "Sí. La sucesión la puede iniciar cualquiera de los herederos; después se cita al resto."),
        ],
    },
    {
        "slug": "civil",
        "nombre": "Civil",
        "icono": "civil",
        "foto": "equipo-civil",
        "titulo": "Abogados de derecho civil en Merlo",
        "lema": "Daños, propiedad y contratos: lo que ordena el patrimonio.",
        "resumen": "Daños y perjuicios, accidentes de tránsito, usucapión, contratos, alquileres y cobro de deudas.",
        "meta": "Derecho civil en Merlo: daños y perjuicios, accidentes de tránsito, usucapión, contratos, alquileres y cobro de deudas. Estudio Jurídico Martínez, desde 1976.",
        "intro": [
            "Reclamos por daños, temas de propiedad y contratos: los asuntos que tocan el patrimonio de una familia o de "
            "un comercio.",
            "Revisamos la documentación, te explicamos qué se puede reclamar y en qué plazos, y llevamos el reclamo "
            "adelante.",
        ],
        "temas": [
            ("danos", "Daños y perjuicios",
             "Si sufriste un daño, en tu persona o en tus cosas, se puede reclamar su reparación a quien lo causó y a su "
             "aseguradora.",
             ["Accidentes de tránsito", "Reclamos a aseguradoras", "Daños en la vivienda", "Responsabilidad civil"]),
            ("usucapion", "Usucapión",
             "Es el trámite para escriturar a nombre de quien vive y cuida un inmueble desde hace muchos años sin tener "
             "los papeles. En general se requieren veinte años de posesión pública y continua.",
             ["Prescripción adquisitiva de inmuebles", "Casas de familia sin escritura",
              "Prueba de la posesión (impuestos, servicios, testigos)"]),
            ("contratos", "Contratos",
             "Un contrato claro evita la mayoría de los conflictos. Redactamos y revisamos antes de firmar, y actuamos "
             "cuando la otra parte no cumple.",
             ["Boletos de compraventa", "Contratos de servicios y préstamos", "Revisión antes de firmar",
              "Incumplimientos"]),
            ("alquileres", "Alquileres",
             "Para propietarios e inquilinos: el contrato, las garantías, la devolución del depósito y los desalojos.",
             ["Contratos de locación", "Cobro de alquileres adeudados", "Desalojos", "Devolución del depósito"]),
            ("deudas", "Cobro de deudas",
             "Cheques, pagarés, facturas y préstamos impagos: intimación, negociación y, si hace falta, ejecución.",
             ["Cheques y pagarés", "Cartas documento", "Juicios ejecutivos"]),
            ("sociedades", "Sociedades y comercios",
             "Constitución de sociedades, acuerdos entre socios y los conflictos que aparecen con el tiempo.",
             ["Constitución de SRL y SAS", "Acuerdos entre socios", "Cesiones y modificaciones"]),
        ],
        "faq": [
            ("Tuve un choque, ¿qué hago primero?",
             "Sacá fotos, guardá los datos del otro conductor y de su seguro y hacé la denuncia en tu aseguradora dentro "
             "de los tres días. Después podemos ver el reclamo contra el seguro del responsable."),
            ("Vivo hace más de veinte años en una casa sin escritura, ¿puedo ponerla a mi nombre?",
             "Es el caso típico de usucapión. Hay que revisar la antigüedad y la prueba de la posesión: impuestos, "
             "servicios, mejoras, testigos."),
        ],
    },
    {
        "slug": "laboral",
        "nombre": "Laboral",
        "icono": "laboral",
        "foto": "equipo-laboral",
        "titulo": "Abogados laborales en Merlo",
        "lema": "Si te despidieron o te accidentaste trabajando, hay plazos que corren.",
        "resumen": "Despidos, liquidación final, accidentes de trabajo y ART, trabajo no registrado y asesoramiento a empresas.",
        "meta": "Abogado laboral en Merlo: despidos, indemnización, liquidación final, accidentes de trabajo y ART, trabajo no registrado. Estudio Jurídico Martínez, desde 1976.",
        "intro": [
            "Revisamos tu situación y te explicamos qué corresponde según la ley y qué plazos tenés. Algunos pasos, como "
            "responder un telegrama, se cuentan en días.",
            "También asesoramos a comercios y pymes de la zona para que la relación laboral esté en regla y los conflictos "
            "se puedan evitar.",
        ],
        "temas": [
            ("despidos", "Despidos e indemnizaciones",
             "Ante un despido sin causa corresponden la indemnización por antigüedad, el preaviso y la integración del mes. "
             "Controlamos los cálculos y reclamamos las diferencias.",
             ["Despido sin causa o con causa discutida", "Despido indirecto", "Intercambio de telegramas",
              "Diferencias en la indemnización"]),
            ("liquidacion", "Liquidación final",
             "Antes de firmar, conviene revisarla: vacaciones no gozadas, aguinaldo proporcional, horas extra y categoría.",
             ["Control de la liquidación", "Vacaciones y aguinaldo", "Horas extra", "Certificado de trabajo"]),
            ("art", "Accidentes de trabajo y ART",
             "Si te lesionaste trabajando o yendo al trabajo, la ART debe cubrir la atención y, si queda una secuela, la "
             "indemnización que corresponda.",
             ["Accidentes de trabajo e in itinere", "Enfermedades profesionales", "Comisiones médicas",
              "Rechazos de la ART"]),
            ("no-registrado", "Trabajo no registrado",
             "Trabajar en negro, con una fecha de ingreso que no es la real o con parte del sueldo fuera del recibo da "
             "derecho a reclamar.",
             ["Trabajo en negro total o parcial", "Fecha de ingreso mal registrada", "Aportes no depositados"]),
            ("violencia-laboral", "Violencia laboral",
             "El maltrato, el acoso o la persecución en el trabajo no son parte del empleo. Te explicamos cómo "
             "documentarlo y qué caminos hay.",
             ["Acoso y hostigamiento", "Acoso sexual en el trabajo", "Discriminación"]),
            ("empresas", "Asesoramiento a empresas",
             "Para comercios y pymes: registración, sanciones, desvinculaciones y respuesta a reclamos.",
             ["Contratación y registración", "Apercibimientos y sanciones", "Desvinculaciones",
              "Respuesta a telegramas"]),
        ],
        "faq": [
            ("¿Cuánto tiempo tengo para reclamar?",
             "El plazo general para los reclamos laborales es de dos años, pero algunos pasos previos se cuentan en días. "
             "Por eso conviene consultar apenas ocurre."),
            ("¿Tengo que firmar la liquidación final?",
             "Podés firmar como constancia de que la recibiste, sin que eso implique renunciar a reclamar diferencias. Si "
             "tenés dudas, mandanos una foto antes de firmar."),
            ("Me accidenté yendo al trabajo, ¿me cubre la ART?",
             "El accidente en el trayecto entre tu casa y el trabajo está cubierto. Conviene denunciarlo cuanto antes."),
        ],
    },
]

AREAS = [AREA_FAMILIA] + AREAS_SEC
AREA = {a["slug"]: a for a in AREAS}

# ------------------------------------------------------------------ primera consulta
PASOS = [
    ("Escribinos", "Por WhatsApp, contanos en dos líneas qué te pasa. No hace falta que sepas cómo se llama tu tema."),
    ("Coordinamos la entrevista", "En el estudio de Av. San Martín 3285, o por videollamada si te queda más cómodo."),
    ("Hablamos de tu situación", "Escuchamos, hacemos preguntas y te explicamos qué dice la ley en tu caso y qué caminos hay."),
    ("Vos decidís", "Si querés avanzar, te acompañamos y te vamos contando cómo sigue el expediente. Si no, te quedás con la información."),
]

LLEVAR = [
    ("Tu DNI", "Y el de las personas involucradas, si lo tenés a mano (por ejemplo, el de tus hijos)."),
    ("Partidas y actas", "Acta de matrimonio, partidas de nacimiento de los hijos, certificado de defunción en una sucesión."),
    ("Los papeles del tema", "Recibos de sueldo, contratos, escrituras, telegramas, denuncias, presupuestos. Aunque te parezcan de más."),
    ("Las fechas en orden", "Cuándo empezó, qué pasó después. Anotarlas antes ayuda mucho en la entrevista."),
    ("Mensajes y comprobantes", "Si hay conversaciones o transferencias que importan, guardalas. No las borres."),
    ("Tus preguntas anotadas", "En la entrevista es fácil olvidarse. Traelas escritas y las vamos viendo una por una."),
]

ESPERAR = [
    ("Te escuchamos primero", "La entrevista empieza por tu relato. No hace falta que uses términos legales ni que tengas todo ordenado."),
    ("Te explicamos sin jerga", "Qué dice la ley en tu situación, qué caminos existen y qué implica cada uno, en palabras comunes."),
    ("Hablamos de tiempos y costos", "Con qué plazos se maneja un trámite así y cómo se trabajan los honorarios, antes de que decidas nada."),
    ("Queda entre nosotros", "El secreto profesional cubre todo lo que nos cuentes, contrates al estudio o no."),
]

FAQ_GENERAL = [
    ("¿Cómo pido una entrevista?",
     "Escribinos por WhatsApp al " + TEL_VISIBLE + " contando brevemente qué necesitás, y coordinamos día y horario."),
    ("Nunca consulté a un abogado, ¿qué tengo que saber?",
     "Nada en particular. Alcanza con que cuentes lo que te pasa; nosotros hacemos las preguntas que hagan falta. "
     "En la página de la primera consulta está el detalle de qué conviene traer."),
    ("¿Atienden solo en Merlo?",
     "El estudio está en Merlo y atendemos a vecinos de Merlo, Padua, Libertad, Pontevedra, Ituzaingó, Moreno y "
     "alrededores. Muchas consultas se pueden hacer por videollamada."),
    ("¿Lo que cuento es confidencial?",
     "Sí. El secreto profesional nos obliga a reservar todo lo que nos cuentes, hayas contratado al estudio o no."),
]
