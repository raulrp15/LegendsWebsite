import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.navbar import PageState

def text() -> rx.Component:
    return rx.heading(
        PageState.cont_txt,
        size="3",
        color=color.pr_2.value,
        style={
            "max-width": "90%",           # Para aprovechar casi todo el ancho disponible
            "margin": "0 auto",           # Centra el componente horizontalmente
            "column-count": "2",          # Divide el texto en 2 columnas
            "column-gap": "2rem",          # Espacio entre columnas
            "white-space": "pre-wrap",    # Conserva saltos de línea y evita desbordes de texto
            "text-align": "justify",       # Justifica el contenido para un acabado profesional
            "padding": "1rem"             # Espaciado interno para mejorar la legibilidad
        }
    )
