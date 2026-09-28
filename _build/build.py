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
V = "5"  # subir al cambiar css/js (cache inmutable en vercel.json)
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
        "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
        "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
        "cerrar": '<path d="M6 6l12 12M18 6L6 18"/>',
        "estrella": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z" fill="currentColor" stroke="none"/>',
        "familia": '<circle cx="8" cy="7" r="2.5"/><circle cx="16" cy="7" r="2.5"/><circle cx="12" cy="13" r="2"/><path d="M3.5 20v-3a4 4 0 0 1 4-4h1M20.5 20v-3a4 4 0 0 0-4-4h-1M9 20v-1.5a3 3 0 0 1 6 0V20"/>',
        "laboral": '<rect x="3.5" y="7.5" width="17" height="12" rx="1.5"/><path d="M9 7.5V5.5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2M3.5 12.5h17"/>',
        "civil": '<path d="M3.5 10.5L12 4l8.5 6.5"/><path d="M5.5 10v10h13V10M10 20v-5.5h4V20"/>',
        "sucesiones": '<path d="M6 3.5h9l3.5 3.5v13H6z"/><path d="M14.5 3.5v4h4M9 12h6M9 15.5h4"/>',
        "escudo": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8-7.5 9.5-4.3-1.5-7.5-5-7.5-9.5V6z"/><path d="M9.5 11.8l1.8 1.8 3.4-3.4"/>',
        "documento": '<path d="M7 3.5h7l4 4v13H7z"/><path d="M14 3.5v4h4M9.5 12h6M9.5 15.5h6"/>',
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
    ("/sucesiones/", "Sucesiones"),
    ("/civil/", "Civil"),
    ("/laboral/", "Laboral"),
    ("/el-estudio/", "El estudio"),
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
    familia = "".join(f'<li><a href="/familia/{t["slug"]}/">{t["nombre"]}</a></li>' for t in D.TEMAS_FAMILIA)
    otras = "".join(f'<li><a href="/{a["slug"]}/">{a["nombre"]}</a></li>' for a in D.AREAS_SEC)
    horarios = "".join(f"<li><span>{d}</span> {h}</li>" for d, h in D.HORARIOS)
    return f"""<footer class="pie">
  <div class="wrap pie__grid">
    <div class="pie__marca">
      {marca(" marca--claro")}
      <p>Estudio jurídico familiar. Acompañamos a las familias merlenses desde {D.FUNDACION}, creciendo con ellas y sus necesidades.</p>
    </div>
    <div>
      <h2 class="pie__tit">Familia</h2>
      <ul class="pie__lista">{familia}</ul>
    </div>
    <div>
      <h2 class="pie__tit">Otras áreas</h2>
      <ul class="pie__lista">{otras}<li><a href="/primera-consulta/">Primera consulta</a></li><li><a href="/el-estudio/">El estudio</a></li></ul>
    </div>
    <div>
      <h2 class="pie__tit">Dónde estamos</h2>
      <ul class="pie__lista">
        <li><a href="{D.MAPS}" target="_blank" rel="noopener">{D.DIRECCION}<br>{D.LOCALIDAD}, {D.PROVINCIA}</a></li>
        {horarios}
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
        "description": f"Estudio jurídico familiar en Merlo desde {D.FUNDACION}: derecho de familia, sucesiones, civil y laboral.",
        "url": D.SITIO + "/",
        "image": D.SITIO + "/og.jpg",
        "logo": D.SITIO + "/favicon/icon-512.png",
        "telephone": "+" + D.WHATSAPP,
        "foundingDate": str(D.FUNDACION),
        "founder": {"@type": "Person", "name": D.FUNDADOR, "jobTitle": "Abogado"},
        "employee": {"@type": "Person", "name": D.A_CARGO, "jobTitle": "Abogada"},
        "address": {"@type": "PostalAddress", "streetAddress": D.DIRECCION, "addressLocality": D.LOCALIDAD,
                    "postalCode": D.CP, "addressRegion": D.PROVINCIA, "addressCountry": "AR"},
        "geo": {"@type": "GeoCoordinates", "latitude": D.LAT, "longitude": D.LNG},
        "hasMap": D.MAPS,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification", "dayOfWeek": h["dias"], "opens": h["abre"], "closes": h["cierra"]}
            for h in D.HORARIO_SCHEMA],
        "areaServed": D.ZONA,
        "knowsAbout": ["Derecho de familia", "Divorcio", "Cuota alimentaria", "Tenencia de hijos",
                       "Régimen de comunicación", "Violencia familiar", "Uniones convivenciales",
                       "División de bienes", "Sucesiones", "Usucapión", "Daños y perjuicios", "Derecho laboral"],
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
    destino = ROOT / "404.html" if ruta == "/404" else (
        ROOT / "index.html" if ruta == "/" else ROOT / ruta.strip("/") / "index.html")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print("ok", ruta)


def parrafos(textos):
    return "".join(f"<p>{t}</p>" for t in textos)


def faq_html(preguntas, titulo="Preguntas frecuentes"):
    items = "".join(f"""<details class="faq__item"><summary>{escape(p)}</summary><p>{escape(r)}</p></details>"""
                    for p, r in preguntas)
    return f"""<section class="sec faq" aria-labelledby="faq-t">
  <div class="wrap faq__grid">
    <div><p class="eyebrow">Dudas comunes</p><h2 id="faq-t" class="h2">{titulo}</h2>
    <p class="muted">¿La tuya no está? <a class="link" href="{WA_GENERAL}" target="_blank" rel="noopener">Escribinos y la vemos</a>.</p></div>
    <div class="faq__lista">{items}</div>
  </div>
</section>"""


def cta_final(titulo="¿Querés que lo veamos juntos?",
              texto="Contanos tu situación por WhatsApp y coordinamos una entrevista, en el estudio o por videollamada."):
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


def bloque_consulta(compacto=False):
    """Cómo es la primera consulta y qué conviene traer: es lo que baja la ansiedad de quien nunca consultó."""
    traer = "".join(f"<li>{icono('check')}<span><b>{t}</b>{x}</span></li>" for t, x in D.LLEVAR[:4 if compacto else 6])
    esperar = "".join(f"""<li class="esperar"><h3 class="h4">{t}</h3><p>{x}</p></li>""" for t, x in D.ESPERAR)
    return f"""<section class="sec consulta" id="primera-consulta">
  <div class="wrap consulta__grid">
    <div class="reveal">
      <p class="eyebrow">La primera consulta</p>
      <h2 class="h2">Qué pasa cuando venís por primera vez</h2>
      <p class="muted">Muchas personas llegan al estudio sin haber hablado nunca con un abogado. Esto es lo que podés esperar de la entrevista.</p>
      <ul class="esperar__lista">{esperar}</ul>
      <a class="link" href="/primera-consulta/">Ver la primera consulta en detalle {icono("flecha")}</a>
    </div>
    <div class="traer reveal">
      <h3 class="h3">Qué conviene traer</h3>
      <ul class="traer__lista">{traer}</ul>
      <p class="traer__nota">Si te falta algo, vení igual: en la entrevista vemos cómo conseguirlo.</p>
    </div>
  </div>
</section>"""


def opiniones_html():
    tarjetas = "".join(f"""<figure class="opinion reveal">
      <div class="estrellas" aria-label="5 de 5 estrellas">{icono("estrella") * 5}</div>
      <blockquote>“{escape(t)}”</blockquote>
      <figcaption>{escape(n)}</figcaption>
    </figure>""" for n, t in D.OPINIONES)
    return f"""<section class="sec opiniones" aria-labelledby="op-t">
  <div class="wrap">
    <div class="sec__cab">
      <p class="eyebrow">Opiniones publicadas en Google</p>
      <h2 id="op-t" class="h2">Lo que dejaron escrito quienes nos consultaron</h2>
    </div>
    <div class="opiniones__grid">{tarjetas}</div>
    <p class="centro"><a class="link" href="{D.MAPS}" target="_blank" rel="noopener">Ver la ficha en Google Maps {icono("flecha")}</a></p>
  </div>
</section>"""


def historia_fotos():
    return f"""<div class="historia__fotos reveal">
      <figure class="historia__diploma">{img("diploma-uba", f"Diploma de abogado de la Universidad de Buenos Aires del Dr. {D.FUNDADOR}", "(min-width: 960px) 34vw, 90vw")}
        <figcaption>El diploma de la UBA del fundador.</figcaption></figure>
      <figure class="historia__premio">{img("fundador-reconocimiento", f"El Dr. {D.FUNDADOR} con el reconocimiento del Colegio de Abogados de Morón", "(min-width: 960px) 20vw, 50vw")}
        <figcaption>Reconocimiento por 50 años de matrícula, 2026.</figcaption></figure>
    </div>"""


# ---------------------------------------------------------------- páginas

def home():
    temas = "".join(f"""<a class="tf reveal" style="--d:{i * 60}ms" href="/familia/{t["slug"]}/">
        <h3 class="h4">{t["nombre"]}</h3>
        <p>{t["resumen"]}</p>
        <span class="tf__mas">Ver más {icono("flecha")}</span>
      </a>""" for i, t in enumerate(D.TEMAS_FAMILIA))

    otras = "".join(f"""<a class="otra reveal" style="--d:{i * 70}ms" href="/{a["slug"]}/">{icono(a["icono"])}
        <span><b>{a["nombre"]}</b>{a["resumen"]}</span>{icono("flecha")}</a>""" for i, a in enumerate(D.AREAS_SEC))

    cuerpo = f"""<section class="hero">
  <div class="wrap hero__grid">
    <div class="hero__txt">
      <p class="eyebrow">Derecho de familia · Merlo</p>
      <h1 class="h1">Abogados de familia en Merlo, <em>desde {D.FUNDACION}</em>.</h1>
      <p class="hero__sub">Divorcios, cuota alimentaria, tenencia y régimen de comunicación, violencia familiar, uniones convivenciales y división de bienes. También sucesiones, derecho civil y laboral. Te escuchamos, te explicamos tu situación en palabras claras y te acompañamos en lo que decidas.</p>
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Coordinar una entrevista</a>
        <a class="btn btn--linea btn--lg" href="#primera-consulta">Cómo es la primera consulta</a>
      </div>
      <ul class="hero__datos">
        <li><b>{D.FUNDACION}</b><span>año de fundación</span></li>
        <li><b>{ANIOS} años</b><span>acompañando a familias de Merlo</span></li>
        <li><b>Familia</b><span>nuestra área principal</span></li>
      </ul>
    </div>
    <div class="hero__media">
      <div class="hero__arco">{img("abogada-consulta", "Una de las abogadas del estudio, en la oficina de Av. San Martín, en Merlo", "(min-width: 960px) 40vw, 90vw", eager=True)}</div>
      <div class="hero__sello">
        {BALANZA}
        <p><b>Un estudio de familia</b>Fundado en {D.FUNDACION} por el Dr. {D.FUNDADOR}. Hoy a cargo de la Dra. {D.A_CARGO}.</p>
      </div>
    </div>
  </div>
</section>

<section class="sec familia-home" id="familia" aria-labelledby="fam-t">
  <div class="wrap">
    <div class="sec__cab">
      <p class="eyebrow">{icono("familia")} Nuestra área principal</p>
      <h2 id="fam-t" class="h2">Derecho de familia</h2>
      <p class="muted">Es el área por la que más nos consultan. Casi siempre hay una etapa difícil atrás: una separación, un desacuerdo por los chicos, una situación de violencia. Empezamos por escuchar y explicar; después vemos los caminos.</p>
    </div>
    <div class="tf__grid">{temas}</div>
    <div class="acciones">
      <a class="btn btn--navy btn--lg" href="/familia/">Ver el área de familia</a>
      <a class="btn btn--linea btn--lg" href="{wa("Hola! Quisiera coordinar una entrevista por un tema de familia.")}" target="_blank" rel="noopener">Consultar por WhatsApp</a>
    </div>
  </div>
</section>

{bloque_consulta()}

<section class="sec otras" aria-labelledby="otras-t">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Otras áreas</p><h2 id="otras-t" class="h2">También trabajamos en</h2></div>
    <div class="otras__grid">{otras}</div>
  </div>
</section>

<section class="sec historia" aria-labelledby="hist-t">
  <div class="wrap historia__grid">
    {historia_fotos()}
    <div class="historia__txt reveal">
      <p class="eyebrow">Nuestra historia</p>
      <p class="historia__num" aria-hidden="true">{ANIOS}</p>
      <h2 id="hist-t" class="h2">Años acompañando a las familias de Merlo.</h2>
      <p>El Dr. {D.FUNDADOR} abrió el estudio en Merlo en {D.FUNDACION}. Desde entonces pasaron por la puerta de Av. San Martín abuelos, hijos y nietos de las mismas familias: muchos de los que hoy nos consultan llegan porque sus padres ya se atendían acá.</p>
      <p>En 2026 el Colegio de Abogados de Morón le entregó un reconocimiento por sus 50 años de matrícula. Hoy el estudio está a cargo de la Dra. {D.A_CARGO}, con el foco puesto en el derecho de familia.</p>
      <a class="link" href="/el-estudio/">Conocer el estudio {icono("flecha")}</a>
    </div>
  </div>
</section>

{opiniones_html()}
{faq_html(D.FAQ_GENERAL)}
{cta_final()}"""
    return pagina("/", f"Abogados de familia en Merlo · Estudio Jurídico Martínez (desde {D.FUNDACION})",
                  f"Estudio de familia en Merlo desde {D.FUNDACION}: divorcio, cuota alimentaria, tenencia y régimen de comunicación, violencia familiar y división de bienes. También sucesiones, civil y laboral. Consultas por WhatsApp.",
                  cuerpo, [schema_estudio(), schema_faq(D.FAQ_GENERAL)], "/")


def pagina_familia():
    a = D.AREA_FAMILIA
    temas = "".join(f"""<a class="tf tf--grande reveal" style="--d:{i * 60}ms" href="/familia/{t["slug"]}/">
        <p class="tf__num">{i + 1:02d}</p>
        <h2 class="h3">{t["nombre"]}</h2>
        <p>{t["resumen"]}</p>
        <span class="tf__mas">Ver más {icono("flecha")}</span>
      </a>""" for i, t in enumerate(a["temas"]))
    wa_area = wa("Hola! Quisiera coordinar una entrevista por un tema de familia.")
    cuerpo = f"""<section class="phero">
  <div class="wrap phero__grid">
    <div>
      <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>Familia</nav>
      <p class="eyebrow">{icono("familia")} Área de familia</p>
      <h1 class="h1">{a["titulo"]}</h1>
      <p class="phero__lema">{a["lema"]}</p>
      {parrafos(a["intro"])}
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{wa_area}" target="_blank" rel="noopener">{icono("wa")}Coordinar una entrevista</a>
        <a class="btn btn--linea btn--lg" href="#primera-consulta">Cómo es la primera consulta</a>
      </div>
    </div>
    <div class="phero__foto">{img(a["foto"], "Abogada de familia del Estudio Jurídico Martínez, en Merlo", "(min-width: 960px) 32vw, 80vw", eager=True)}</div>
  </div>
</section>

<section class="sec familia-home" aria-labelledby="temas-t">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Temas</p><h2 id="temas-t" class="h2">En qué te podemos ayudar</h2>
    <p class="muted">Cada tema tiene su página, con lo que dice la ley explicado en palabras comunes.</p></div>
    <div class="tf__grid">{temas}</div>
  </div>
</section>

{bloque_consulta()}
{faq_html(a["faq"])}
{cta_final("¿Empezamos por una entrevista?", "Contanos en dos líneas qué te pasa y coordinamos día y horario. En el estudio, en Merlo, o por videollamada.")}"""
    return pagina("/familia/", f"{a['titulo']} · Divorcio, alimentos y tenencia | Estudio Jurídico Martínez",
                  a["meta"], cuerpo,
                  [schema_estudio(), schema_faq(a["faq"]), schema_migas([("Inicio", "/"), ("Familia", "/familia/")])],
                  "/familia/")


def pagina_tema_familia(t, i):
    ruta = f"/familia/{t['slug']}/"
    puntos = "".join(f"<li>{icono('check')}{p}</li>" for p in t["puntos"])
    otros = "".join(f'<a class="chip chip--claro" href="/familia/{o["slug"]}/">{o["nombre"]}</a>'
                    for o in D.TEMAS_FAMILIA if o is not t)
    traer = "".join(f"<li>{icono('check')}<span><b>{x}</b>{y}</span></li>" for x, y in D.LLEVAR[:4])
    msg = wa(f"Hola! Quisiera coordinar una entrevista por un tema de {t['nombre'].lower()}.")
    aviso = (f'<p class="aviso">{icono("escudo")}<span>{t["aviso"]}</span></p>' if t.get("aviso") else "")
    cuerpo = f"""<section class="phero phero--tema">
  <div class="wrap">
    <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span><a href="/familia/">Familia</a><span>/</span>{t["nombre"]}</nav>
    <p class="eyebrow">{icono("familia")} Familia</p>
    <h1 class="h1">{t["titulo"]}</h1>
    <p class="phero__lema">{t["resumen"]}</p>
  </div>
</section>

<section class="sec tema-pag">
  <div class="wrap tema-pag__grid">
    <div class="tema-pag__txt reveal">
      {parrafos(t["intro"])}
      {aviso}
      <h2 class="h3">Con qué te podemos ayudar</h2>
      <ul class="tema__lista">{puntos}</ul>
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{msg}" target="_blank" rel="noopener">{icono("wa")}Consultar por {t["nombre"].lower()}</a>
      </div>
    </div>
    <aside class="tema-pag__lado reveal">
      <div class="lado__caja">
        <h2 class="h4">Qué conviene traer</h2>
        <ul class="traer__lista traer__lista--chica">{traer}</ul>
        <a class="link" href="/primera-consulta/">Ver la lista completa {icono("flecha")}</a>
      </div>
      <div class="lado__caja lado__caja--navy">
        <p><b>Hablemos de tu caso</b>Coordinamos una entrevista en el estudio, en Merlo, o por videollamada.</p>
        <a class="btn btn--wa" href="{msg}" target="_blank" rel="noopener">{icono("wa")}{D.TEL_VISIBLE}</a>
      </div>
    </aside>
  </div>
</section>

{faq_html(t["faq"], "Preguntas frecuentes sobre " + t["nombre"].lower())}

<section class="sec otros-temas">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Otros temas de familia</p><h2 class="h2">También trabajamos</h2></div>
    <div class="chips chips--fila">{otros}</div>
  </div>
</section>
{cta_final()}"""
    return pagina(ruta, f"{t['titulo']} | Estudio Jurídico Martínez", t["meta"], cuerpo,
                  [schema_estudio(), schema_faq(t["faq"]),
                   schema_migas([("Inicio", "/"), ("Familia", "/familia/"), (t["nombre"], ruta)])], "/familia/")


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
    otras = f"""<a class="otra reveal" href="/familia/">{icono("familia")}
        <span><b>Familia</b>{D.AREA_FAMILIA["resumen"]}</span>{icono("flecha")}</a>"""
    otras += "".join(f"""<a class="otra reveal" href="/{o["slug"]}/">{icono(o["icono"])}
        <span><b>{o["nombre"]}</b>{o["resumen"]}</span>{icono("flecha")}</a>""" for o in D.AREAS_SEC if o is not a)
    wa_area = wa(f"Hola! Quisiera coordinar una entrevista por un tema de {a['nombre'].lower()}.")

    cuerpo = f"""<section class="phero">
  <div class="wrap phero__grid">
    <div>
      <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>{a["nombre"]}</nav>
      <p class="eyebrow">{icono(a["icono"])} Área {a["nombre"].lower()}</p>
      <h1 class="h1">{a["titulo"]}</h1>
      <p class="phero__lema">{a["lema"]}</p>
      {parrafos(a["intro"])}
      <div class="acciones">
        <a class="btn btn--wa btn--lg" href="{wa_area}" target="_blank" rel="noopener">{icono("wa")}Consultar por WhatsApp</a>
      </div>
    </div>
    <div class="phero__foto">{img(a["foto"], f"Estudio Jurídico Martínez, área {a['nombre'].lower()}, en Merlo", "(min-width: 960px) 32vw, 80vw", eager=True)}</div>
  </div>
</section>

<section class="sec temas">
  <div class="wrap temas__grid">
    <aside class="temas__indice">
      <p class="eyebrow">En esta página</p>
      <ul>{indice}</ul>
      <div class="temas__caja">
        <p><b>¿Tenés dudas?</b>Escribinos contando tu situación y coordinamos una entrevista.</p>
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
    return pagina(ruta, f"{a['titulo']} | Estudio Jurídico Martínez", a["meta"], cuerpo,
                  [schema_estudio(), schema_faq(a["faq"]), schema_migas([("Inicio", "/"), (a["nombre"], ruta)])], ruta)


def el_estudio():
    valores = [
        ("Escuchar primero", "Antes de hablar de leyes, escuchamos qué te pasa. La mayoría llega en un momento difícil."),
        ("Explicar sin jerga", "Vas a entender qué dice la ley en tu caso, qué caminos hay y qué implica cada uno."),
        ("Reserva", "Lo que nos contás queda entre nosotros. En temas de familia, la discreción es parte del trabajo."),
        ("Continuidad", f"{ANIOS} años en el mismo lugar, atendiendo a varias generaciones de las mismas familias."),
    ]
    val = "".join(f"""<li class="valor reveal" style="--d:{i * 70}ms"><h3 class="h4">{t}</h3><p>{x}</p></li>"""
                  for i, (t, x) in enumerate(valores))
    equipo = "".join(f"""<figure class="miembro reveal" style="--d:{i * 90}ms">
      <div class="miembro__foto">{img(a["foto"], f"Abogada del área de {a['nombre'].lower()} del estudio", "(min-width: 960px) 28vw, 80vw")}</div>
      <figcaption><b>Área {a["nombre"].lower()}</b><span>{a["resumen"]}</span>
      <a class="link" href="/{a["slug"]}/">Ver el área {icono("flecha")}</a></figcaption>
    </figure>""" for i, a in enumerate([D.AREA_FAMILIA, D.AREA["laboral"], D.AREA["civil"]]))
    linea = [
        (str(D.FUNDACION), "Nace el estudio",
         f"El Dr. {D.FUNDADOR}, abogado recibido en la Universidad de Buenos Aires, se matricula en el Colegio de "
         "Abogados de Morón y abre el estudio en Merlo."),
        ("Décadas", "Crecer con el barrio",
         "Sucesiones, divorcios, despidos, contratos: el estudio acompaña a varias generaciones de las mismas familias merlenses."),
        ("Hoy", f"A cargo de la Dra. {D.A_CARGO}",
         "El estudio trabaja sobre todo en derecho de familia, y también en sucesiones, civil y laboral."),
        ("2026", "50 años de matrícula",
         f"El Colegio de Abogados de Morón reconoce al Dr. {D.FUNDADOR} por sus 50 años de ejercicio profesional."),
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
    {historia_fotos()}
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
    <div class="sec__cab"><p class="eyebrow">El equipo</p><h2 id="eq-t" class="h2">Quiénes te van a atender</h2>
    <p class="muted">El estudio está a cargo de la Dra. {D.A_CARGO}, que lleva el área de familia. Cada área tiene una abogada que se dedica a eso.</p></div>
    <div class="equipo__grid">{equipo}</div>
  </div>
</section>

<section class="sec espacio">
  <div class="wrap espacio__grid">
    <figure class="reveal">{img("estudio-oficina", "La oficina del estudio en Av. San Martín, Merlo", "(min-width: 960px) 45vw, 90vw")}</figure>
    <div class="reveal">
      <p class="eyebrow">Nuestro espacio</p>
      <h2 class="h2">Te esperamos en Av. San Martín 3285</h2>
      <p>Un lugar tranquilo para hablar con reserva. Si no podés acercarte, la entrevista se puede hacer por videollamada.</p>
      <a class="link" href="/contacto/">Cómo llegar {icono("flecha")}</a>
    </div>
  </div>
</section>
{opiniones_html()}
{cta_final()}"""
    return pagina("/el-estudio/", f"El estudio · Abogados en Merlo desde {D.FUNDACION} | Estudio Jurídico Martínez",
                  f"Fundado en {D.FUNDACION} por el Dr. {D.FUNDADOR} y hoy a cargo de la Dra. {D.A_CARGO}, el Estudio Jurídico Martínez acompaña a las familias de Merlo hace {ANIOS} años.",
                  cuerpo, [schema_estudio(), schema_migas([("Inicio", "/"), ("El estudio", "/el-estudio/")])],
                  "/el-estudio/")


def primera_consulta():
    pasos = "".join(f"""<li class="paso reveal" style="--d:{i * 80}ms"><span class="paso__n">{i + 1}</span>
      <h3 class="h4">{t}</h3><p>{x}</p></li>""" for i, (t, x) in enumerate(D.PASOS))
    llevar = "".join(f"""<li class="llevar reveal" style="--d:{i * 60}ms"><span class="llevar__n">{i + 1:02d}</span>
      <div><h3 class="h4">{t}</h3><p>{x}</p></div></li>""" for i, (t, x) in enumerate(D.LLEVAR))
    esperar = "".join(f"""<li class="esperar reveal"><h3 class="h4">{t}</h3><p>{x}</p></li>""" for t, x in D.ESPERAR)
    cuerpo = f"""<section class="phero">
  <div class="wrap phero__grid">
    <div>
      <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>Primera consulta</nav>
      <p class="eyebrow">Primera consulta</p>
      <h1 class="h1">Cómo es la primera entrevista</h1>
      <p class="phero__lema">Ir a un abogado por primera vez pone nerviosa a cualquiera. Te contamos cómo es, qué conviene traer y qué podés esperar.</p>
      <div class="acciones"><a class="btn btn--wa btn--lg" href="{WA_GENERAL}" target="_blank" rel="noopener">{icono("wa")}Coordinar una entrevista</a></div>
    </div>
    <div class="phero__foto">{img("estudio-oficina", "La oficina del estudio en Merlo", "(min-width: 960px) 32vw, 80vw", eager=True)}</div>
  </div>
</section>

<section class="sec pasos">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Paso a paso</p><h2 class="h2">De tu primer mensaje a la entrevista</h2></div>
    <ol class="pasos__lista">{pasos}</ol>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Qué esperar</p><h2 class="h2">Cómo trabajamos en la entrevista</h2></div>
    <ul class="esperar__lista esperar__lista--grid">{esperar}</ul>
  </div>
</section>

<section class="sec llevar-sec">
  <div class="wrap">
    <div class="sec__cab"><p class="eyebrow">Checklist</p><h2 class="h2">Qué conviene traer</h2>
    <p class="muted">No es excluyente: si te falta algo, vení igual y vemos cómo conseguirlo.</p></div>
    <ol class="llevar__grid">{llevar}</ol>
  </div>
</section>
{faq_html(D.FAQ_GENERAL)}
{cta_final("¿Coordinamos?", "Escribinos contando brevemente qué necesitás y vemos día y horario. Presencial en Merlo o por videollamada.")}"""
    return pagina("/primera-consulta/", "Primera consulta con un abogado: cómo es y qué llevar | Estudio Jurídico Martínez",
                  "Cómo es la primera entrevista en el Estudio Jurídico Martínez de Merlo, qué documentación conviene traer y qué podés esperar. Presencial o por videollamada.",
                  cuerpo, [schema_estudio(), schema_faq(D.FAQ_GENERAL),
                           schema_migas([("Inicio", "/"), ("Primera consulta", "/primera-consulta/")])],
                  "/primera-consulta/")


def contacto():
    opciones = "".join(f'<option value="{t["nombre"]}">Familia · {t["nombre"]}</option>' for t in D.TEMAS_FAMILIA)
    opciones += "".join(f'<option value="{a["nombre"]}">{a["nombre"]}</option>' for a in D.AREAS_SEC)
    horarios = "".join(f"<li><span>{d}</span><b>{h}</b></li>" for d, h in D.HORARIOS)
    cuerpo = f"""<section class="phero phero--centro">
  <div class="wrap">
    <nav class="migas" aria-label="Estás en"><a href="/">Inicio</a><span>/</span>Contacto</nav>
    <p class="eyebrow">Contacto</p>
    <h1 class="h1">Hablemos de tu situación</h1>
    <p class="phero__lema">Escribinos por WhatsApp o acercate al estudio. Todo lo que nos cuentes es confidencial.</p>
  </div>
</section>

<section class="sec contacto">
  <div class="wrap contacto__grid">
    <form class="form reveal" id="form-wa" data-wa="{D.WHATSAPP}" novalidate>
      <h2 class="h3">Armá tu mensaje</h2>
      <p class="muted">Completá estos datos y se abre WhatsApp con el mensaje listo. No se guarda nada en ningún servidor.</p>
      <label>Tu nombre<input name="nombre" autocomplete="name" required></label>
      <label>Tema
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
      <figure class="contacto__fachada">{img("fachada", f"Fachada del Estudio Jurídico Martínez en {D.DIRECCION}, {D.LOCALIDAD}", "(min-width: 960px) 20vw, 45vw")}
        <figcaption>Buscá la puerta con el cartel del estudio, en Av. San Martín 3285.</figcaption></figure>
    </div>
  </div>
  <div class="wrap mapa reveal">
    <iframe title="Mapa: {D.NOMBRE}, {D.DIRECCION}, {D.LOCALIDAD}" src="{D.MAPS_EMBED}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>
</section>"""
    return pagina("/contacto/", "Contacto · Abogados en Merlo | Estudio Jurídico Martínez",
                  f"Contactá al Estudio Jurídico Martínez: WhatsApp {D.TEL_VISIBLE}, {D.DIRECCION}, {D.LOCALIDAD}. Entrevistas presenciales o por videollamada.",
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
    rutas = [("/", "1.0"), ("/familia/", "0.9")]
    rutas += [(f"/familia/{t['slug']}/", "0.8") for t in D.TEMAS_FAMILIA]
    rutas += [(f"/{a['slug']}/", "0.7") for a in D.AREAS_SEC]
    rutas += [("/primera-consulta/", "0.7"), ("/el-estudio/", "0.6"), ("/contacto/", "0.6")]
    urls = "".join(f"<url><loc>{D.SITIO}{r}</loc><lastmod>{HOY}</lastmod><priority>{p}</priority></url>" for r, p in rutas)
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
    escribir("/familia/", pagina_familia())
    for i, t in enumerate(D.TEMAS_FAMILIA):
        escribir(f"/familia/{t['slug']}/", pagina_tema_familia(t, i))
    for a in D.AREAS_SEC:
        escribir(f"/{a['slug']}/", pagina_area(a))
    escribir("/el-estudio/", el_estudio())
    escribir("/primera-consulta/", primera_consulta())
    escribir("/contacto/", contacto())
    escribir("/404", no_encontrada())
    soporte()
