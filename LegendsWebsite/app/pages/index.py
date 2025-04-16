import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.texts import text
from LegendsWebsite.app.components.navbar import button_selector, PageState
from LegendsWebsite.app.components.video_audio_content import card

@rx.page(route='/')
def index() -> rx.Component:
    return rx.vstack(
        # Encabezado: título fijo y selector de botones.
        rx.vstack(
            rx.heading(
                "Inturkės legendos",
                size="9",
                color=color.pr_1.value,
                align="center",
                justify="center",
                style={
                    "text-shadow": "2px 2px 4px rgba(0,0,0,0.3)",
                    "margin-bottom": {"base": "2rem", "md": "1rem"}
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
                "margin-top": "2rem"
            },
            align="center"
        ),

        # Tarjeta principal
        card(),
        style={
            "width": "100%",
            "minHeight": "100vh",
            "justifyContent": "center",
            "alignItems": "center",
            "backgroundImage": "url('/fondo.png')",
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "backgroundRepeat": "no-repeat"
        },
        spacing="2"
    )