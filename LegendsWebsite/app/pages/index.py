import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.texts import text
from LegendsWebsite.app.components.navbar import button_selector, PageState
from LegendsWebsite.app.components.video_audio_content import card

@rx.page(route='/')
def index() -> rx.Component:
    return rx.vstack(
        # Encabezado con título y selector de botones
        rx.vstack(
            rx.heading(
                "Legends of Lithuania",
                size='9',
                color=color.pr_1.value,
                align="center",
                justify="center",
                style={
                    "text-shadow": "2px 2px 4px rgba(0,0,0,0.3)",
                    "margin-bottom": "1rem"
                }
            ),
            button_selector(),
            bg=color.pr_2.value,
            style={
                    "width": "100%",
                    "padding": "3dvh 2dvw",
                    "border-bottom-left-radius": "10px",
                    "border-bottom-right-radius": "10px",
                    "box-shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                    **{"margin-top": "2rem"}  # 👈 Aquí se agrega el margen superior
                },
            align="center",
        ),
        # Componente principal (tarjeta) que agrupa el contenido multimedia y texto.
        card(),
        align="center",
        justify="start",
        style={
            "width": "100vw",
            "min-height": "100vh",
            "background": color.bg.value if hasattr(color, "bg") else "#f5f5f5",
            "padding": "1rem",
            "box-sizing": "border-box",
            "margin-top": "-3rem"  # Valor negativo para subir el card
        }
    )
