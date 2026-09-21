# Estudio Jurídico Martínez — sitio web

Sitio estático multipágina (HTML/CSS/JS vanilla) del Estudio Jurídico Martínez, Merlo (desde 1976).
Se publica en Vercel tal cual (sin build): la raíz del repo es la raíz del sitio.

## Cómo se edita

Las páginas se **generan** con Python; no editar los `index.html` a mano.

```
python _build/procesar_fotos.py   # solo si cambian las fotos (originales en ../_raw, fuera del repo)
python _build/build.py            # regenera todas las páginas, sitemap, robots y manifest
```

- Textos, áreas, temas, horarios, teléfono y preguntas frecuentes: `_build/datos.py`.
- Estructura HTML: `_build/build.py`. Estilos: `css/estilos.css`. Comportamiento: `js/main.js`.
- Al cambiar CSS o JS, subir `V` en `build.py` (el cache de `/css` y `/js` es inmutable).
- Cuando haya dominio propio, cambiar `SITIO` en `datos.py` y regenerar.

## Páginas

`/` · `/familia/` · `/laboral/` · `/civil-comercial/` · `/el-estudio/` · `/primera-consulta/` · `/contacto/` · `404.html`

## Pendientes

Ver `insumos/dudas.md` (horario, teléfono de la puerta, dominio, nombres del equipo). Análisis de referencias en `insumos/ANALISIS.md`.
