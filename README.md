# 📊 roanny.github.io — CV / portfolio

Portfolio profesional de **Roanny Lamas López** (Data Engineer · Google Cloud), publicado con GitHub Pages en **https://roanny.github.io/**.

Construido con HTML, CSS y JavaScript puros en un único archivo — sin frameworks ni paso de build.

## Estructura

```
├── index.html       # Todo el sitio: contenido, estilos, i18n y lógica
├── favicon.svg      # Favicon (sol sobre olas) + favicon-32.png de respaldo
├── og-image.png     # Social card 1200×630 (previews en LinkedIn/WhatsApp/X)
├── robots.txt       # Permite indexación y enlaza el sitemap
├── sitemap.xml      # Mapa del sitio (actualiza lastmod al hacer cambios)
└── .nojekyll        # GitHub Pages sirve el sitio tal cual, sin Jekyll
```

## Cómo editar los textos

Todo vive en `index.html`. Los textos bilingües están en el objeto **`i18n`** del `<script>` final, en dos diccionarios (`en` y `es`) con las mismas claves; cada elemento traducible lleva `data-i18n="clave"`. Edita el valor en ambos idiomas y, si el cambio es grande, actualiza también el texto por defecto (inglés) en el HTML para mantenerlos alineados.

## Idioma y tema

- **Idioma**: se detecta del navegador (EN por defecto), se fuerza con `?lang=en|es` y se cambia con el botón **EN/ES**; la elección se recuerda.
- **Tema**: arranca según la apariencia del sistema (oscuro por defecto), se fuerza con `?theme=light|dark` y se cambia con el botón **🌙/☀️**; la elección se recuerda. El tema claro es la variante "caribe de día".

## Sistema de diseño

El sitio comparte identidad con [Coabana](https://coabana.github.io/): misma paleta caribeño-tech, tipografías, chips, botones y motion. La referencia canónica de tokens y componentes es el **[DESIGN.md del repo de Coabana](https://github.com/Coabana/coabana.github.io/blob/main/DESIGN.md)** — si cambias un token allí, replícalo en el `<style>` de `index.html`.

## SEO

`index.html` incluye canonical, hreflang (`en`/`es`/`x-default` vía `?lang=`), Open Graph y Twitter cards con `og-image.png`, y JSON-LD de tipo `Person` (con la afiliación a Coabana). Tras cambios de contenido, actualiza `lastmod` en `sitemap.xml`.

## Probar en local

```bash
python3 -m http.server 8000
# abre http://localhost:8000
```

## Publicación

GitHub Pages sirve la rama `main` (raíz) automáticamente — al hacer merge, el sitio se despliega solo en 1–2 minutos.
