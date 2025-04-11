import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.navbar import PageState
from LegendsWebsite.app.components.texts import text

class selected_state(rx.State):
    value: str = 'Lithuanian'

    @rx.event
    def change_value(self, value: str):
        self.value = value

def content(video, audio) -> rx.Component:
    return rx.vstack(
        # Primera sección: audio y selector de idioma
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
                ['Lithuanian', 'English', 'Spanish'],
                value=selected_state.value,
                on_change=selected_state.change_value,
                flex="2",
            ),
            wrap="wrap",
            align="center",
            spacing="4",
        ),
        # Segunda sección: vídeo y texto
        rx.flex(
            rx.box(
                rx.cond(
                    VideoState.loaded,
                    rx.video(
                        url=video,
                        width="100%",
                        loop=True,
                        muted=False,
                        volume=0.01,
                        controls=False,
                        playing=True,
                        style={
                            "border-radius": "15px",
                            "overflow": "hidden"
                        }
                    ),
                    rx.center(
                        rx.vstack(
                            rx.spinner(size="3", color=color.pr_1.value),  
                            rx.text("Cargando video...", color=color.pr_1.value)
                        ),
                        width="100%",
                        height="100%"
                    )
                ),
                flex="1"
            ),

            rx.box(
                text(),
                width="100%",
                flex="2",
            ),
            wrap="wrap",
            align="center",
            spacing="4",
        ),
        align="center",
        # Estilos para ocupar toda la pantalla y centrar el contenido
        style={
            "width": "100vw",
            "height": "100vh",
            "padding": "1rem",
            "box-sizing": "border-box",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "center",
            "alignItems": "center"
        }
    ) 

def card() -> rx.Component:
    return rx.card(
        content(
            f"/{PageState.index + 1}/{PageState.index + 1}.mp4",
            f"/{PageState.index + 1}/{PageState.index + 1}_"
        ),
        size='1',
        bg=color.th.value,
        style={
            "width": "100vw",
            "height": "100vh",
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "flex-start",
            "alignItems": "flex-start",  # Alineado a la izquierda si deseas eso
            "padding": "2em"             # Puedes ajustar el espacio interior
        }
    )


class VideoState(rx.State):
    loaded: bool = False

    def on_load(self):
        yield rx.timer(1.5)  # espera simulada de 1.5 segundos
        self.loaded = True
