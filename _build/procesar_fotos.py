"""Recorta y optimiza las fotos originales (carpeta ../_raw, fuera del repo).

Uso:  python _build/procesar_fotos.py
Genera assets/img/<nombre>-480.webp / -960.webp (y -1440 si da el tamaño),
_build/medidas.json, los favicons y og.jpg.
"""
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT.parent / "_raw"
IG = RAW / "ig"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

NAVY = (22, 35, 63)
CREMA = (246, 241, 232)
BRONCE = (168, 132, 69)

# nombre: (archivo, recorte (x0, y0, x1, y1) o None, duotono)
FOTOS = {
    "equipo-civil": (IG / "DH_R2-Csx0Y.jpg", (322, 24, 640, 640), True),
    "equipo-laboral": (IG / "DH_R4Uzs5qV.jpg", (330, 40, 640, 640), True),
    "equipo-familia": (IG / "Da5r0Y5N5XN.jpg", (70, 96, 590, 640), True),
    "estudio-oficina": (IG / "DZDg7RAxvjN.jpg", (0, 96, 640, 640), False),
    "abogada-consulta": (IG / "Da5r0Y5N5XN.jpg", (0, 96, 640, 640), False),
    "fundador-reconocimiento": (IG / "DcmVWc4xJZL.jpg", None, False),
    "diploma-uba": (IG / "Dara_6iDAwG.jpg", None, False),
    "fachada": (RAW / "maps1.jpg", (452, 330, 872, 1210), False),
}


def duotono(im):
    """Blanco y negro teñido de navy a crema: unifica fotos con fondos de colores distintos."""
    g = ImageOps.autocontrast(im.convert("L"), cutoff=1)
    return ImageOps.colorize(g, black=NAVY, white=CREMA, mid=(128, 124, 128))


medidas = {}
for nombre, (archivo, caja, duo) in FOTOS.items():
    im = Image.open(archivo).convert("RGB")
    if caja:
        im = im.crop(caja)
    if duo:
        im = duotono(im)
    w0, h0 = im.size
    medidas[nombre] = [w0, h0]
    for ancho in (480, 960, 1440):
        if ancho == 1440 and w0 < 1440:
            continue
        a = min(ancho, w0)
        out = im.resize((a, round(h0 * a / w0)), Image.LANCZOS) if a != w0 else im
        out.save(OUT / f"{nombre}-{ancho}.webp", "WEBP", quality=80, method=6)
    print(nombre, w0, h0)

(ROOT / "_build" / "medidas.json").write_text(json.dumps(medidas, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- favicons y og
SERIF = str(RAW / "eb1.ttf")   # EB Garamond 500
SERIF_B = str(RAW / "eb2.ttf")  # EB Garamond 600
SANS = str(RAW / "f4.ttf")    # Jost 400


def icono(tam):
    im = Image.new("RGB", (tam, tam), NAVY)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(SERIF_B, int(tam * 0.78))
    d.text((tam / 2, tam * 0.47), "M", font=f, fill=CREMA, anchor="mm")
    y = int(tam * 0.8)
    d.line([(tam * 0.3, y), (tam * 0.7, y)], fill=BRONCE, width=max(1, tam // 32))
    return im


fav = ROOT / "favicon"
fav.mkdir(exist_ok=True)
icono(180).save(fav / "apple-touch-icon.png")
icono(512).save(fav / "icon-512.png")
icono(192).save(fav / "icon-192.png")
icono(48).save(ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

og = Image.new("RGB", (1200, 630), NAVY)
foto = Image.open(OUT / "abogada-consulta-960.webp").convert("RGB")
foto = ImageOps.fit(foto, (470, 630), centering=(0.5, 0.4))
og.paste(foto, (730, 0))
d = ImageDraw.Draw(og)
d.text((80, 150), "ESTUDIO JURÍDICO", font=ImageFont.truetype(SANS, 26), fill=BRONCE)
d.text((76, 190), "Martínez", font=ImageFont.truetype(SERIF_B, 118), fill=CREMA)
d.line([(82, 350), (170, 350)], fill=BRONCE, width=3)
d.text((80, 380), "Familia · Sucesiones · Civil · Laboral", font=ImageFont.truetype(SERIF, 38), fill=CREMA)
d.text((80, 432), "En Merlo desde 1976", font=ImageFont.truetype(SERIF, 40), fill=(200, 196, 188))
og.save(ROOT / "og.jpg", "JPEG", quality=86, optimize=True)
print("favicons y og listos")
