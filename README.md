# Hackea tu escuela: sensores, datos y energía con hardware libre

Presentación en Quarto (revealjs) para estudiantes de preparatoria.

## Contenido

| Archivo | Qué es |
| --- | --- |
| `index.qmd` | Las diapositivas (incluye notas del orador y las gráficas en Python) |
| `custom.scss` | Estilo de la presentación |
| `img/` | Figuras del artículo (CC BY) y croquis del SITE |
| `data/site_temperatura.csv` | Temperaturas del SITE, promedios de 5 min, 6 sensores |
| `scripts/prepara_datos.py` | Genera el CSV a partir del parquet crudo del repo `site_temperatura` |
| `smartWatch.pdf`, `smartWatch.txt` | Artículo de HardwareX (2025) y su texto plano |

## Uso

```bash
uv sync                          # instala jupyter, pandas, matplotlib
uv run quarto preview            # ver la presentación mientras se edita
uv run quarto render             # genera index.html
uv run quarto publish gh-pages   # publica en GitHub Pages
```

Las gráficas se ejecutan con Python; `_freeze/` guarda los resultados para que
publicar no requiera volver a ejecutarlas si el código no cambió.

Tecla `S` en la presentación: vista del orador con las notas.
