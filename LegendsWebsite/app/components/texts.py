import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.navbar import PageState

def text() -> rx.Component:
    return rx.heading(
        PageState.cont_txt,
        size="3",
        color=color.pr_2.value,
        style={
            "max-width": "90%",
            "margin": "0 auto",
            "column-count": "1",       # Valor por defecto (móviles)
            "column-gap": "2rem",
            "white-space": "pre-wrap",
            "text-align": "justify",
            "padding": "1rem",
            "@media (min-width: 768px)": {  # A partir de 768px de ancho
                "column-count": "2"    # Se aplican 2 columnas en pantallas grandes
            }
        }
    )

