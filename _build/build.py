"""Genera todas las páginas HTML del sitio a partir de _build/datos.py.

Uso:  python _build/build.py
(Si cambian las fotos, correr antes python _build/procesar_fotos.py)
"""
import json
from datetime import date
from html import escape
from pathlib import Path
from urllib.parse import quote

import datos as D

ROOT = Path(__file__).resolve().parents[1]
MEDIDAS = json.loads((ROOT / "_build" / "medidas.json").read_text(encoding="utf-8"))
V = "2"  # subir al cambiar css/js (cache inmutable en vercel.json)
HOY = date.today().isoformat()
ANIOS = date.today().year - D.FUNDACION


# ---------------------------------------------------------------- helpers

def wa(texto):
    return f"https://wa.me/{D.WHATSAPP}?text={quote(texto)}"


WA_GENERAL = wa("Hola! Quisiera coordinar una entrevista por un tema de ")


def img(nombre, alt, sizes="100vw", cls="", eager=False):
    w0, h0 = MEDIDAS[nombre]
    w960 = min(960, w0)
    src = [f"/assets/img/{nombre}-480.webp {min(480, w0)}w"]
    if w0 > 480:
        src.append(f"/assets/img/{nombre}-960.webp {w960}w")
    if w0 >= 1440:
        src.append(f"/assets/img/{nombre}-1440.webp 1440w")
    h960 = round(h0 * w960 / w0)
    carga = 'fetchpriority="high"' if eager else 'loading="lazy"'
    clase = f' class="{cls}"' if cls else ""
    return (f'<img{clase} src="/assets/img/{nombre}-960.webp" srcset="{", ".join(src)}" '
            f'sizes="{sizes}" width="{w960}" height="{h960}" alt="{escape(alt)}" {carga} decoding="async">')


def icono(nombre):
    trazos = {
        "wa": '<path d="M3.5 20.5l1.3-4.2A8.5 8.5 0 1 1 8 19.3z"/><path d="M9 8.6c0 3.3 3 6.3 6.3 6.4l1.2-1.4-2-1-1 .8a4.6 4.6 0 0 1-2.4-2.4l.8-1-1-2z"/>',
        "flecha": '<path d="M5 12h14M13 6l6 6-6 6"/>',
        "ig": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6"/>',
        "pin": '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
        "reloj": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
        "tel": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a1 1 0 0 1-1 1A16 16 0 0 1 4 5a1 1 0 0 1 1-1z"/>',
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "cerrar": '<path d="M6 6l12 12M18 6L6 18"/>',
        "estrella": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z" fill="currentColor" stroke="none"/>',
        "familia": '<circle cx="8" cy="7" r="2.5"/><circle cx="16" cy="7" r="2.5"/><circle cx="12" cy="13" r="2"/><path d="M3.5 20v-3a4 4 0 0 1 4-4h1M20.5 20v-3a4 4 0 0 0-4-4h-1M9 20v-1.5a3 3 0 0 1 6 0V20"/>',
        "laboral": '<rect x="3.5" y="7.5" width="17" height="12" rx="1.5"/><path d="M9 7.5V5.5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M3.5 12.5h17"/>',
        "civil-comercial": '<path d="M7 3.5h7l4 4v13H7z"/><path d="M14 3.5v4h4M9.5 12h6M9.5 15.5h6"/>',
        "escudo": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8-7.5 9.5-4.3-1.5-7.5-5-7.5-9.5V6z"/>',
    }[nombre]
    return (f'<svg class="ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{trazos}</svg>')


# balanza de la justicia: la marca del logo, redibujada
BALANZA = ('<svg class="balanza" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M24 6v34M15 42h18M10 13h28"/><circle cx="24" cy="8" r="1.6"/>'
           '<path d="M10 13l-5.5 12h11zM38 13l-5.5 12h11z"/>'
           '<path d="M4.5 25a5.5 3 0 0 0 11 0M32.5 25a5.5 3 0 0 0 11 0"/></svg>')

NAV = [
    ("/familia/", "Familia"),
    ("/laboral/", "Laboral"),
    ("/civil-comercial/", "Civil y comercial"),
    ("/el-estudio/", "El estudio"),
    ("/primera-consulta/", "Primera consulta"),
    ("/contacto/", "Contacto"),
]


def marca(extra=""):
    return f"""<a class="marca{extra}" href="/" aria-label="{D.NOMBRE}, inicio">
      {BALANZA}
      <span class="marca__txt"><small>Estudio Jurídico</small><b>Martínez</b><em>En Merlo desde {D.FUNDACION}</em></span>
    </a>"""


def header(actual):
    links = "".join(
        f'<li><a href="{u}"{" aria-current=\"page\"" if u == actual else ""}>{t}</a></li>' for u, t in NAV)
    return f"""<a class="skip" href="#contenido">Saltar al contenido</a>
<header class="hdr" id="hdr">
  <div class="hdr__in wrap">
    {marca()}
    <nav class="nav" id="nav" aria-label="Principal">
      <ul>{links}</ul>
      <a class="btn btn--wa nav__cta" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Escribinos</a>
    </nav>
    <a class="btn btn--wa btn--sm hdr__cta" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}<span>WhatsApp</span></a>
    <button class="hdr__menu" id="menu" aria-expanded="false" aria-controls="nav" aria-label="Abrir menú">{icono("menu")}{icono("cerrar")}</button>
  </div>
</header>"""


def footer():
    areas = "".join(f'<li><a href="/{a["slug"]}/">{a["nombre"]}</a></li>' for a in D.AREAS)
    horarios = "".join(f"<li><span>{d}</span> {h}</li>" for d, h in D.HORARIOS)
    return f"""<footer class="pie">
  <div class="wrap pie__grid">
    <div class="pie__marca">
      {marca(" marca--claro")}
      <p>Estudio jurídico familiar. Acompañamos a las familias merlenses desde {D.FUNDACION}, creciendo con ellas y sus necesidades.</p>
    </div>
    <div>
      <h2 class="pie__tit">Áreas</h2>
      <ul class="pie__lista">{areas}<li><a href="/primera-consulta/">Primera consulta</a></li></ul>
    </div>
    <div>
      <h2 class="pie__tit">Visitanos</h2>
      <ul class="pie__lista">
        <li><a href="{D.MAPS}" target="_blank" rel="noopener">{D.DIRECCION}<br>{D.LOCALIDAD}, {D.PROVINCIA}</a></li>
        {horarios}
      </ul>
    </div>
    <div>
      <h2 class="pie__tit">Contacto</h2>
      <ul class="pie__lista">
        <li><a href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")} {D.TEL_VISIBLE}</a></li>
        <li><a href="{D.INSTAGRAM}" target="_blank" rel="noopener">{icono("ig")} @estudio.juridico.martinez</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap pie__legal">
    <p>© {date.today().year} {D.NOMBRE}. La información de este sitio es general y no reemplaza una consulta profesional.</p>
    <p>Sitio por <a href="https://www.tunegocioenlasredes.com.ar" target="_blank" rel="noopener">Tu Negocio En Las Redes</a></p>
  </div>
</footer>
<a class="wa-flot" href="{WA_GENERAL}" target="_blank" rel="noopener" aria-label="Escribinos por WhatsApp">{icono("wa")}</a>"""


def schema_estudio():
    return {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": D.SITIO + "/#estudio",
        "name": D.NOMBRE,
        "description": "Estudio jurídico familiar en Merlo desde 1976: derecho de familia, laboral y civil y comercial.",
        "url": D.SITIO + "/",
        "image": D.SITIO + "/og.jpg",
        "logo": D.SITIO + "/favicon/icon-512.png",
        "telephone": "+" + D.WHATSAPP,
        "foundingDate": str(D.FUNDACION),
        "founder": {"@type": "Person", "name": "Miguel Ángel Martínez", "jobTitle": "Abogado"},
        "address": {"@type": "PostalAddress", "streetAddress": D.DIRECCION, "addressLocality": D.LOCALIDAD,
                    "postalCode": D.CP, "addressRegion": D.PROVINCIA, "addressCountry": "AR"},
        "geo": {"@type": "GeoCoordinates", "latitude": D.LAT, "longitude": D.LNG},
        "hasMap": D.MAPS,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": h["dias"], "opens": h["abre"], "closes": h["cierra"]}
            for h in D.HORARIO_SCHEMA],
        "areaServed": ["Merlo", "San Antonio de Padua", "Libertad", "Pontevedra", "Ituzaingó", "Moreno"],
        "knowsAbout": ["Derecho de familia", "Divorcio", "Cuota alimentaria", "Sucesiones",
                       "Derecho laboral", "Despidos", "Accidentes de trabajo", "Derecho civil", "Contratos", "Alquileres"],
        "sameAs": [D.INSTAGRAM],
    }


def schema_faq(preguntas):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": p, "acceptedAnswer": {"@type": "Answer", "text": r}} for p, r in preguntas]}


def schema_migas(migas):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": D.SITIO + u} for i, (n, u) in enumerate(migas)]}


def pagina(ruta, titulo, descripcion, cuerpo, schemas=(), actual=None):
    url = D.SITIO + ruta
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schemas)
    return f"""<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add("js")</script>
<title>{escape(titulo)}</title>
<meta name="description" content="{escape(descripcion)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#16233f">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="{D.NOMBRE}">
<meta property="og:title" content="{escape(titulo)}">
<meta property="og:description" content="{escape(descripcion)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{D.SITIO}/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/favicon/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400&family=Jost:wght@400;500&display=swap">
<link rel="stylesheet" href="/css/estilos.css?v={V}">
{ld}
</head>
<body>
{header(actual)}
<main id="contenido">
{cuerpo}
</main>
{footer()}
<script src="/js/main.js?v={V}" defer></script>
</body>
</html>
"""


def escribir(ruta, html):
    destino = ROOT / ruta.strip("/") / "index.html" if ruta != "/404" else ROOT / "404.html"
    if ruta == "/":
        destino = ROOT / "index.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print("ok", ruta)


def faq_html(preguntas, titulo="Preguntas frecuentes"):
    items = "".join(f"""<details class="faq__item"><summary>{escape(p)}</summary><p>{escape(r)}</p></details>"""
                    for p, r in preguntas)
    return f"""<section class="sec faq" aria-labelledby="faq-t">
  <div class="wrap faq__grid">
    <div><p class="eyebrow">Dudas comunes</p><h2 id="faq-t" class="h2">{titulo}</h2>
    <p class="muted">¿La tuya no está? <a class="link" href="{WA_GENERAL}" target="_blank" rel="noopener">Preguntanos por WhatsApp</a>.</p></div>
    <div class="faq__lista">{items}</div>
  </div>
</section>"""


def cta_final(titulo="¿Querés que lo veamos juntos?", texto="Contanos tu situación por WhatsApp y coordinamos una entrevista, en el estudio o por videollamada."):
    horarios = " · ".join(f"{d} {h}" for d, h in D.HORARIOS)
    return f"""<section class="cta-final">
  <div class="wrap cta-final__in reveal">
    {BALANZA}
    <h2 class="h2">{titulo}</h2>
    <p>{texto}</p>
    <div class="acciones acciones--centro">
      <a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Escribinos al {D.TEL_VISIBLE}</a>
    </div>
    <p class="cta-final__dato">{icono("pin")} {D.DIRECCION}, {D.LOCALIDAD} &nbsp;·&nbsp; {icono("reloj")} {horarios}</p>
  </div>
</section>"""


def opiniones_html():
    tarjetas = "".join(f"""<figure class="opinion reveal">
      <div class="estrellas" aria-label="5 de 5 estrellas">{icono("estrella") * 5}</div>
      <blockquote>“{escape(t)}”</blockquote>
      <figcaption>{escape(n)} · opinión en Google</figcaption>
    </figure>""" for n, t in D.OPINIONES)
    return f"""<section class="sec opiniones" aria-labelledby="op-t">
  <div class="wrap">
    <div class="sec__cab">
      <p class="eyebrow">Lo que dicen de nosotros</p>
      <h2 id="op-t" class="h2">{D.PUNTAJE} estrellas en Google</h2>
    </div>
    <div class="opiniones__grid">{tarjetas}</div>
    <p class="centro"><a class="link" href="{D.MAPS}" target="_blank" rel="noopener">Ver la ficha en Google Maps {icono("flecha")}</a></p>
  </div>
</section>"""


# ---------------------------------------------------------------- páginas

def home():
    chips = [
        ("Divorcio", "divorcio"), ("Cuota alimentaria", "cuota alimentaria"),
        ("Régimen de comunicación", "régimen de comunicación con mis hijos"),
        ("Sucesión", "una sucesión"), ("Despido", "un despido"), ("Accidente / ART", "un accidente de trabajo (ART)"),
        ("Alquiler", "un alquiler"), ("Choque", "un accidente de tránsito"), ("Otro tema", "otro tema"),
    ]
    chips_html = "".join(
        f'<a class="chip" href="{wa("Hola! Quisiera coordinar una entrevista por un tema de " + m + ".")}" target="_blank" rel="noopener">{t}</a>'
        for t, m in chips)

    areas_html = ""
    for i, a in enumerate(D.AREAS):
        temas = "".join(f'<li><a href="/{a["slug"]}/#{s}">{t}</a></li>' for s, t, *_ in a["temas"])
        areas_html += f"""<article class="area reveal" style="--d:{i * 90}ms">
      <a class="area__foto" href="/{a["slug"]}/" tabindex="-1" aria-hidden="true">{img(a["foto"], "", "(min-width: 960px) 30vw, 90vw")}</a>
      <div class="area__cuerpo">
        <p class="area__num">0{i + 1}</p>
        <h3 class="h3"><a href="/{a["slug"]}/">{a["nombre"]}</a></h3>
        <p>{a["resumen"]}</p>
        <ul class="area__temas">{temas}</ul>
        <a class="link" href="/{a["slug"]}/">Conocer el área {icono("flecha")}</a>
      </div>
    </article>"""

    pasos = "".join(f"""<li class="paso reveal" style="--d:{i * 80}ms"><span class="paso__n">{i + 1}</span>
      <h3 class="h4">{t}</h3><p>{x}</p></li>""" for i, (t, x) in enumerate(D.PASOS))

    cuerpo = f"""<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__txt">
      <p class="eyebrow">Estudio jurídico familiar · Merlo</p>
      <h1 class="h1">Acompañamos a las familias de Merlo desde <em>{D.FUNDACION}</em>.</h1>
      <p class="hero__sub">Derecho de familia, laboral y civil y comercial. Te explicamos tu situación con palabras claras y te acompañamos en cada paso, con la experiencia de {ANIOS} años en el barrio.</p>
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Coordinar una entrevista</a>
        <a class="btn btn--linea btn--lg" href="#areas">Ver áreas de práctica</a>
      </div>
      <ul class="hero__datos">
        <li><b>{D.FUNDACION}</b><span>año de fundación</span></li>
        <li><b>{D.PUNTAJE}<span class="est">{icono("estrella")}</span></b><span>en Google</span></li>
        <li><b>3</b><span>áreas de práctica</span></li>
      </ul>
    </div>
    <div class="hero__media">
      <div class="hero__arco">{img("estudio-oficina", "Una de las abogadas del estudio en la oficina de Av. San Martín, en Merlo", "(min-width: 960px) 40vw, 90vw", eager=True)}</div>
      <div class="hero__sello">
        {BALANZA}
        <p><b>50 años de matrícula</b>Dr. Miguel Ángel Martínez, fundador. Colegio de Abogados de Morón.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec areas" id="areas" aria-labelledby="areas-t">
  <div class="wrap">
    <div class="sec__cab">
      <p class="eyebrow">Áreas de práctica</p>
      <h2 id="areas-t" class="h2">En qué te podemos ayudar</h2>
      <p class="muted">Tres áreas, un mismo criterio: explicarte claro, contestarte rápido y no dejarte solo en el proceso.</p>
    </div>
    <div class="areas__grid">{areas_html}</div>
  </div>
</section>

<section class="sec guia">
  <div class="wrap guia__in reveal">
    <div>
      <p class="eyebrow eyebrow--claro">¿No sabés por dónde empezar?</p>
      <h2 class="h2">Elegí tu tema y escribinos.</h2>
      <p>No hace falta que sepas cómo se llama legalmente lo que te pasa. Tocá el tema más parecido y te llega el WhatsApp con el mensaje ya escrito.</p>
    </div>
    <div class="chips">{chips_html}</div>
  </div>
</section>

<section class="sec historia" aria-labelledby="hist-t">
  <div class="wrap historia__grid">
    <div class="historia__fotos reveal">
      <figure class="historia__diploma">{img("diploma-uba", "Diploma de abogado de la Universidad de Buenos Aires del Dr. Miguel Ángel Martínez", "(min-width: 960px) 34vw, 90vw")}
        <figcaption>El diploma de la UBA del fundador.</figcaption></figure>
      <figure class="historia__premio">{img("fundador-reconocimiento", "El Dr. Miguel Ángel Martínez recibe el reconocimiento por 50 años de matrícula", "(min-width: 960px) 20vw, 50vw")}
        <figcaption>Reconocimiento por 50 años de matrícula, 2026.</figcaption></figure>
    </div>
    <div class="historia__txt reveal">
      <p class="eyebrow">Nuestra historia</p>
      <p class="historia__num" aria-hidden="true">{ANIOS}</p>
      <h2 id="hist-t" class="h2">Años acompañando a las mismas familias.</h2>
      <p>El Dr. Miguel Ángel Martínez abrió el estudio en Merlo en {D.FUNDACION}. Desde entonces pasaron por la puerta de Av. San Martín abuelos, hijos y nietos de las mismas familias: muchos de los que hoy nos consultan llegan porque sus padres ya confiaban en nosotros.</p>
      <p>En 2026 el Colegio de Abogados de Morón le entregó un reconocimiento por sus 50 años de matrícula. Hoy el estudio sigue creciendo con una nueva generación de abogadas.</p>
      <a class="link" href="/el-estudio/">Conocer el estudio {icono("flecha")}</a>
    </div>
  </div>
</section>

<section class="sec pasos" aria-labelledby="pasos-t">
  <div class="wrap">
    <div class="sec__cab">
      <p class="eyebrow">Cómo trabajamos</p>
      <h2 id="pasos-t" class="h2">De tu primer mensaje a la solución</h2>
    </div>
    <ol class="pasos__lista">{pasos}</ol>
    <p class="centro"><a class="link" href="/primera-consulta/">Qué llevar a la primera consulta {icono("flecha")}</a></p>
  </div>
</section>

{opiniones_html()}
{faq_html(D.FAQ_GENERAL)}
{cta_final()}"""
    return pagina("/", f"Estudio Jurídico Martínez · Abogados en Merlo desde {D.FUNDACION}",
                  f"Estudio jurídico familiar en Merlo desde {D.FUNDACION}. Abogadas de familia, laboral y civil: divorcios, cuota alimentaria, sucesiones, despidos, ART y contratos. Consultas por WhatsApp.",
                  cuerpo, [schema_estudio(), schema_faq(D.FAQ_GENERAL)], "/")


def pagina_area(a):
    ruta = f"/{a['slug']}/"
    indice = "".join(f'<li><a href="#{s}">{t}</a></li>' for s, t, *_ in a["temas"])
    temas = ""
    for i, (s, t, texto, puntos) in enumerate(a["temas"]):
        lista = "".join(f"<li>{icono('check')}{p}</li>" for p in puntos)
        msg = wa(f"Hola! Quisiera coordinar una entrevista por un tema de {t.lower()}.")
        temas += f"""<article class="tema reveal" id="{s}">
        <p class="tema__num">{i + 1:02d}</p>
        <div>
          <h2 class="h3">{t}</h2>
          <p>{texto}</p>
          <ul class="tema__lista">{lista}</ul>
          <a class="link" href="{msg}" target="_blank" rel="noopener">{icono("wa")} Consultar por {t.lower()}</a>
        </div>
      </article>"""
    otras = "".join(f"""<a class="otra reveal" href="/{o["slug"]}/">{icono(o["slug"])}
        <span><b>{o["nombre"]}</b>{o["resumen"]}</span>{icono("flecha")}</a>""" for o in D.AREAS if o is not a)
    wa_area = wa(f"Hola! Quisiera coordinar una entrevista por un tema de {a['nombre'].lower()}.")

    cuerpo = f"""<section class="phero">
  <div class="wrap phero__grid">
    <div>
      <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>{a["nombre"]}</nav>
      <p class="eyebrow">{icono(a["slug"])} Área {a["nombre"].lower()}</p>
      <h1 class="h1">{a["titulo"]}</h1>
      <p class="phero__lema">{a["lema"]}</p>
      <p>{a["intro"]}</p>
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{wa_area}" target="_blank" rel="noopener">{icono("wa")}Consultar por WhatsApp</a>
      </div>
    </div>
    <div class="phero__foto">{img(a["foto"], f"Abogada del área de {a['nombre'].lower()} del Estudio Jurídico Martínez", "(min-width: 960px) 32vw, 80vw", eager=True)}</div>
  </div>
</section>

<section class="sec temas">
  <div class="wrap temas__grid">
    <aside class="temas__indice">
      <p class="eyebrow">En esta página</p>
      <ul>{indice}</ul>
      <div class="temas__caja">
        <p><b>¿Tu caso es urgente?</b>Escribinos y te respondemos a la brevedad.</p>
        <a class="btn btn--wa" href="{wa_area}" target="_blank" rel="noopener">{icono("wa")}{D.TEL_VISIBLE}</a>
      </div>
    </aside>
    <div class="temas__lista">{temas}</div>
  </div>
</section>

{faq_html(a["faq"])}

<section class="sec otras">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Otras áreas</p><h2 class="h2">También te podemos ayudar con</h2></div>
    <div class="otras__grid">{otras}</div>
  </div>
</section>
{cta_final()}"""
    return pagina(ruta, f"{a['titulo']} · {a['nombre']} | Estudio Jurídico Martínez", a["meta"], cuerpo,
                  [schema_estudio(), schema_faq(a["faq"]), schema_migas([("Inicio", "/"), (a["nombre"], ruta)])], ruta)


def el_estudio():
    valores = [
        ("Cercanía", "Somos un estudio de barrio. Te atendemos nosotros, no una recepción: sabés con quién hablás."),
        ("Claridad", "Te explicamos tu situación sin jerga. Vas a entender qué pasa, qué puede pasar y cuánto cuesta."),
        ("Reserva", "Lo que nos contás queda entre nosotros. En temas de familia, la discreción es parte del trabajo."),
        ("Experiencia", f"{ANIOS} años resolviendo los problemas de las familias de Merlo, en los tribunales de la zona."),
    ]
    val = "".join(f"""<li class="valor reveal" style="--d:{i * 70}ms"><h3 class="h4">{t}</h3><p>{x}</p></li>"""
                  for i, (t, x) in enumerate(valores))
    equipo = "".join(f"""<figure class="miembro reveal" style="--d:{i * 90}ms">
      <div class="miembro__foto">{img(a["foto"], f"Abogada del área {a['nombre'].lower()}", "(min-width: 960px) 28vw, 80vw")}</div>
      <figcaption><b>Área {a["nombre"].lower()}</b><span>{a["resumen"]}</span>
      <a class="link" href="/{a["slug"]}/">Ver el área {icono("flecha")}</a></figcaption>
    </figure>""" for i, a in enumerate(D.AREAS))
    linea = [
        (str(D.FUNDACION), "Nace el estudio",
         "El Dr. Miguel Ángel Martínez, abogado recibido en la Universidad de Buenos Aires, se matricula en el Colegio de Abogados de Morón y abre el estudio en Merlo."),
        ("Décadas", "Crecer con el barrio",
         "Sucesiones, divorcios, despidos, contratos: el estudio acompaña a varias generaciones de las mismas familias merlenses."),
        ("Hoy", "Una nueva generación",
         "Un equipo de abogadas atiende las áreas de familia, laboral y civil y comercial, con la misma forma de trabajar: cerca y claro."),
        ("2026", "50 años de matrícula",
         "El Colegio de Abogados de Morón reconoce al Dr. Martínez por sus 50 años de ejercicio profesional."),
    ]
    hitos = "".join(f"""<li class="hito reveal"><p class="hito__anio">{a}</p><div><h3 class="h4">{t}</h3><p>{x}</p></div></li>"""
                    for a, t, x in linea)

    cuerpo = f"""<section class="phero phero--centro">
  <div class="wrap">
    <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>El estudio</nav>
    <p class="eyebrow">El estudio</p>
    <h1 class="h1">Un estudio familiar, <em>para familias</em>.</h1>
    <p class="phero__lema">Desde {D.FUNDACION} en Merlo, creciendo con las familias del barrio y con sus necesidades.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap historia__grid">
    <div class="historia__fotos reveal">
      <figure class="historia__diploma">{img("diploma-uba", "Diploma de abogado de la Universidad de Buenos Aires del Dr. Miguel Ángel Martínez", "(min-width: 960px) 34vw, 90vw")}
        <figcaption>El diploma de la UBA del fundador.</figcaption></figure>
      <figure class="historia__premio">{img("fundador-reconocimiento", "El Dr. Miguel Ángel Martínez con el reconocimiento del Colegio de Abogados de Morón", "(min-width: 960px) 20vw, 50vw")}
        <figcaption>Colegio de Abogados de Morón, 2026.</figcaption></figure>
    </div>
    <div>
      <p class="eyebrow">Nuestra historia</p>
      <ol class="linea">{hitos}</ol>
    </div>
  </div>
</section>

<section class="sec valores">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow eyebrow--claro">Cómo trabajamos</p><h2 class="h2">Lo que no cambió en {ANIOS} años</h2></div>
    <ul class="valores__grid">{val}</ul>
  </div>
</section>

<section class="sec" aria-labelledby="eq-t">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">El equipo</p><h2 id="eq-t" class="h2">Una abogada para cada tema</h2>
    <p class="muted">Cada área está a cargo de una profesional que se dedica a eso todos los días.</p></div>
    <div class="equipo__grid">{equipo}</div>
  </div>
</section>

<section class="sec espacio">
  <div class="wrap espacio__grid">
    <figure class="reveal">{img("abogada-consulta", "Una de las abogadas del estudio, en su escritorio", "(min-width: 960px) 45vw, 90vw")}</figure>
    <div class="reveal">
      <p class="eyebrow">Nuestro espacio</p>
      <h2 class="h2">Te esperamos en Av. San Martín 3285</h2>
      <p>Un lugar tranquilo para hablar con reserva. Si no podés acercarte, hacemos la consulta por videollamada.</p>
      <a class="link" href="/contacto/">Cómo llegar {icono("flecha")}</a>
    </div>
  </div>
</section>
{opiniones_html()}
{cta_final()}"""
    return pagina("/el-estudio/", f"El estudio · Abogados en Merlo desde {D.FUNDACION} | Estudio Jurídico Martínez",
                  f"Fundado en {D.FUNDACION} por el Dr. Miguel Ángel Martínez, el Estudio Jurídico Martínez acompaña a las familias de Merlo hace {ANIOS} años. Conocé nuestra historia y nuestro equipo.",
                  cuerpo, [schema_estudio(), schema_migas([("Inicio", "/"), ("El estudio", "/el-estudio/")])], "/el-estudio/")


def primera_consulta():
    pasos = "".join(f"""<li class="paso reveal" style="--d:{i * 80}ms"><span class="paso__n">{i + 1}</span>
      <h3 class="h4">{t}</h3><p>{x}</p></li>""" for i, (t, x) in enumerate(D.PASOS))
    llevar = "".join(f"""<li class="llevar reveal" style="--d:{i * 60}ms"><span class="llevar__n">{i + 1:02d}</span>
      <div><h3 class="h4">{t}</h3><p>{x}</p></div></li>""" for i, (t, x) in enumerate(D.LLEVAR))
    cuerpo = f"""<section class="phero">
  <div class="wrap phero__grid">
    <div>
      <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>Primera consulta</nav>
      <p class="eyebrow">Primera consulta</p>
      <h1 class="h1">Tu primera consulta, <em>sin nervios</em>.</h1>
      <p class="phero__lema">Ir a un abogado por primera vez da un poco de miedo. Te contamos cómo es y qué traer para aprovecharla al máximo.</p>
      <div class="acciones"><a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Pedir una entrevista</a></div>
    </div>
    <div class="phero__foto">{img("estudio-oficina", "La oficina del estudio en Merlo", "(min-width: 960px) 32vw, 80vw", eager=True)}</div>
  </div>
</section>

<section class="sec pasos">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Paso a paso</p><h2 class="h2">Cómo es</h2></div>
    <ol class="pasos__lista">{pasos}</ol>
  </div>
</section>

<section class="sec llevar-sec">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Checklist</p><h2 class="h2">6 cosas que te ayudan a aprovechar la consulta</h2></div>
    <ol class="llevar__grid">{llevar}</ol>
  </div>
</section>
{faq_html(D.FAQ_GENERAL)}
{cta_final("¿Lista la lista?", "Escribinos y coordinamos día y horario. Presencial en Merlo o por videollamada.")}"""
    return pagina("/primera-consulta/", "Primera consulta con una abogada: qué llevar | Estudio Jurídico Martínez",
                  "Cómo es la primera consulta en el Estudio Jurídico Martínez de Merlo y 6 cosas para llevar: documentos, fechas y preguntas. Presencial o por videollamada.",
                  cuerpo, [schema_estudio(), schema_faq(D.FAQ_GENERAL),
                           schema_migas([("Inicio", "/"), ("Primera consulta", "/primera-consulta/")])], "/primera-consulta/")


def contacto():
    opciones = "".join(f'<option value="{a["nombre"]}">{a["nombre"]}</option>' for a in D.AREAS)
    horarios = "".join(f"<li><span>{d}</span><b>{h}</b></li>" for d, h in D.HORARIOS)
    cuerpo = f"""<section class="phero phero--centro">
  <div class="wrap">
    <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>Contacto</nav>
    <p class="eyebrow">Contacto</p>
    <h1 class="h1">Hablemos de tu caso</h1>
    <p class="phero__lema">Escribinos por WhatsApp o acercate al estudio. Todo lo que nos cuentes es confidencial.</p>
  </div>
</section>

<section class="sec contacto">
  <div class="wrap contacto__grid">
    <form class="form reveal" id="form-wa" data-wa="{D.WHATSAPP}" novalidate>
      <h2 class="h3">Armá tu mensaje</h2>
      <p class="muted">Completá estos datos y se abre WhatsApp con el mensaje listo. No guardamos nada en ningún servidor.</p>
      <label>Tu nombre<input name="nombre" autocomplete="name" required></label>
      <label>Área
        <select name="area"><option value="">No sé / otro tema</option>{opciones}</select>
      </label>
      <label>Contanos brevemente qué pasa<textarea name="detalle" rows="4" placeholder="Por ejemplo: me separé y quiero acordar la cuota de mis hijos."></textarea></label>
      <fieldset><legend>Preferís la entrevista</legend>
        <label class="radio"><input type="radio" name="modo" value="en el estudio" checked> En el estudio</label>
        <label class="radio"><input type="radio" name="modo" value="por videollamada"> Por videollamada</label>
      </fieldset>
      <p class="form__error" id="form-error" role="alert" hidden>Escribí tu nombre para que sepamos cómo llamarte.</p>
      <button class="btn btn--wa btn--lg" type="submit">{icono("wa")}Enviar por WhatsApp</button>
    </form>

    <div class="contacto__datos reveal">
      <ul class="datos">
        <li>{icono("wa")}<div><span>WhatsApp</span><a href="{WA_GENERAL}" target="_blank" rel="noopener">{D.TEL_VISIBLE}</a></div></li>
        <li>{icono("pin")}<div><span>Dirección</span><a href="{D.MAPS}" target="_blank" rel="noopener">{D.DIRECCION}, {D.LOCALIDAD}</a></div></li>
        <li>{icono("ig")}<div><span>Instagram</span><a href="{D.INSTAGRAM}" target="_blank" rel="noopener">@estudio.juridico.martinez</a></div></li>
      </ul>
      <div class="horario"><h2 class="h4">{icono("reloj")} Horario de atención</h2><ul>{horarios}</ul></div>
      <figure class="contacto__fachada">{img("fachada", "Fachada del Estudio Jurídico Martínez en Av. José de San Martín 3285, Merlo", "(min-width: 960px) 20vw, 45vw")}
        <figcaption>Buscá la puerta con el cartel del estudio, en Av. San Martín 3285.</figcaption></figure>
    </div>
  </div>
  <div class="wrap mapa reveal">
    <iframe title="Mapa: {D.NOMBRE}, {D.DIRECCION}, {D.LOCALIDAD}" src="{D.MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>"""
    return pagina("/contacto/", "Contacto · Abogados en Merlo | Estudio Jurídico Martínez",
                  f"Contactá al Estudio Jurídico Martínez: WhatsApp {D.TEL_VISIBLE}, {D.DIRECCION}, {D.LOCALIDAD}. Consultas presenciales o por videollamada.",
                  cuerpo, [schema_estudio(), schema_migas([("Inicio", "/"), ("Contacto", "/contacto/")])], "/contacto/")


def no_encontrada():
    cuerpo = f"""<section class="phero phero--centro nf">
  <div class="wrap">
    <p class="eyebrow">Error 404</p>
    <h1 class="h1">Esta página no existe</h1>
    <p class="phero__lema">Puede que el enlace esté mal escrito o que la hayamos movido.</p>
    <div class="acciones acciones--centro">
      <a class="btn btn--navy btn--lg" href="/">Volver al inicio</a>
      <a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Escribinos</a>
    </div>
  </div>
</section>"""
    html = pagina("/404", "Página no encontrada | Estudio Jurídico Martínez", "La página que buscás no existe.", cuerpo)
    return html.replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"')


# ---------------------------------------------------------------- archivos de soporte

def soporte():
    rutas = ["/", "/familia/", "/laboral/", "/civil-comercial/", "/el-estudio/", "/primera-consulta/", "/contacto/"]
    urls = "".join(f"<url><loc>{D.SITIO}{r}</loc><lastmod>{HOY}</lastmod></url>" for r in rutas)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {D.SITIO}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({
        "name": D.NOMBRE, "short_name": "Martínez", "start_url": "/", "display": "standalone",
        "background_color": "#f7f3ec", "theme_color": "#16233f",
        "icons": [{"src": "/favicon/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/favicon/icon-512.png", "sizes": "512x512", "type": "image/png"}]},
        ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "favicon" / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#16233f"/>'
        + BALANZA.replace('<svg class="balanza" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" '
                          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">',
                          '<g fill="none" stroke="#e9d7ae" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" transform="translate(4.8 4.8) scale(.8)">')
        .replace("</svg>", "</g></svg>"), encoding="utf-8")


if __name__ == "__main__":
    escribir("/", home())
    for a in D.AREAS:
        escribir(f"/{a['slug']}/", pagina_area(a))
    escribir("/el-estudio/", el_estudio())
    escribir("/primera-consulta/", primera_consulta())
    escribir("/contacto/", contacto())
    escribir("/404", no_encontrada())
    soporte()
