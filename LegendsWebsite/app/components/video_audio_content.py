import reflex as rx
from LegendsWebsite.Styles import color, size
from LegendsWebsite.app.components.texts import text
from LegendsWebsite.app.components.navbar import button_selector, PageState

# Lista de títulos para cada contenido.
content_list = [
    "Deives Urke",
    "Alkūninis ąžuolas",
    "Karalienės Donn pasakojamiento",
    "Mystery of the Deep"
]

# Si aún no lo has hecho, asegúrate de que PageState esté definido con get_page_title().
# Por ejemplo:
#
# class PageState(rx.State):
#     index: int = 0
#     title: str = content_list[0]
#     def set_index(self, new_index: int):
#         self.index = new_index
#         self.title = content_list[new_index]
#     @staticmethod
#     def get_page_title() -> str:
#         return PageState.title
#     ... (otras propiedades reactivas, etc.)

# Estado para selector de idioma (defínela solo una vez).
class selected_state(rx.State):
    value: str = 'Lietuvių'

    @rx.event
    def change_value(self, value: str):
        self.value = value

def content(video: str, audio: str) -> rx.Component:
    return rx.vstack(
        # Reproductor de audio y selector
        rx.flex(
            rx.audio(
                url=(audio + selected_state.value + '.mp3'),
                controls=True,
                volume=0.5,
                width="45dvh",
                height="4dvh",
                flex="1",
            ),
            rx.select(
                ['Lietuvių', 'English', 'Español'],
                value=selected_state.value,
                on_change=selected_state.change_value,
                flex="2",
            ),
            style={
                "flexDirection": "row",
                "padding": "1rem",
                "gap": "1.5rem",
                "marginBottom": "2rem",
                "borderRadius": "10px",
                "backgroundColor": "#f9f9f9"
            },
            wrap="wrap",
            align="center",
        ),

        # Video y texto lado a lado
        rx.flex(
            # Video
            rx.box(
                rx.video(
                    url=video,
                    id="legend-video",
                    width="100%",
                    height="100%",
                    loop=True,
                    muted=False,
                    volume=0.01,
                    controls=False,
                    playing=True,
                    on_click=rx.call_script("""
                        const el = document.getElementById('legend-video');
                        if (!document.fullscreenElement) {
                            el.requestFullscreen();
                        } else {
                            document.exitFullscreen();
                        }
                    """),
                    style={
                        "display": "block",
                        "width": "100%",
                        "height": "100%",
                        "object-fit": "cover",
                        "transition": "transform 0.5s ease-in-out",
                        "transform-origin": "center"
                    }
                ),
                style={
                    "maxWidth": "600px",
                    "border-radius": "15px",
                    "overflow": "hidden",
                    "display": "flex",
                    "alignItems": "center",
                    "justifyContent": "center",
                    "transition": "box-shadow 0.3s ease-in-out",
                    "marginBottom": "1rem",
                    ":hover": {
                        "box-shadow": "0 12px 24px rgba(0, 0, 0, 0.3)"
                    },
                    "selector": {
                        "video:hover": {
                            "transform": "scale(2)"
                        }
                    }
                },
                flex="1"
            ),

            # Texto
            rx.box(
                text(),
                style={
                    "maxWidth": "600px",
                    "whiteSpace": "pre-wrap",
                    "overflowWrap": "break-word",
                    "padding": "1rem",
                    "backgroundColor": "#ffffff",
                    "borderRadius": "10px",
                    "boxShadow": "0 2px 6px rgba(0, 0, 0, 0.05)",
                },
                flex="1"
            ),

            style={
                "flexDirection": "row",
                "gap": "2rem",
                "alignItems": "flex-start",
                "justifyContent": "center",
                "@media (max-width: 768px)": {
                    "flexDirection": "column",
                    "alignItems": "center"
                }
            }
        ),

        align="center",
        style={
            "width": "100%",
            "padding": "1rem",
            "gap": "1.5rem"
        }
    )


def card() -> rx.Component:
    return rx.card(
        rx.vstack(
            # Título dinámico con estilos responsivos.
            rx.heading(
                PageState.get_page_title(),
                size={"base": "5", "md": "7"},
                color="black",
                style={"marginBottom": {"base": "2rem", "md": "2rem"}}
            ),
            # Contenido multimedia y textual.
            content(
                f"/{PageState.index + 1}/{PageState.index + 1}.mp4",
                f"/{PageState.index + 1}/{PageState.index + 1}_"
            ),
            spacing="4",
            align="center",
        ),
        size="1",
        bg="rgba(40, 80, 60, 0.2)",
        style={
            "width": "100%",
            "maxWidth": "1200px",
            "flex": "1",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "flex-start",
            "alignItems": "center",
            "padding": "3em 2em",
            "box-sizing": "border-box",
            "overflowY": "auto",
            "gap": "2rem",
            "backdropFilter": "blur(4px)",
            "boxShadow": "0 8px 32px rgba(0, 0, 0, 0.1)"
        }
    )

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
        # Tarjeta principal.
        card(),
        style={
            "width": "100%",
            "justifyContent": "center",
            "alignItems": "center"
        },
        spacing="2"
    )
 