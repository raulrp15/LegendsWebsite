import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.navbar import PageState
from LegendsWebsite.app.components.texts import text

class selected_state(rx.State):
    value:str ='Lithuanian'
    @rx.event
    def change_value(self, value:str):
        
        self.value = value

def content(video, audio) -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.audio(
                url=(audio + selected_state.value + '.mp3'),
                controls=True,
                volume=0.5,
                align="center",
                width="45dvh",
                height="5dvh",
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
        rx.flex(
            rx.box(
                rx.video(
                    url=video,
                    width="100%",
                    loop=True,
                    muted=False,
                    volume=0.01,
                    controls=False,
                    playing=True,
                    style={"border-radius": "15px", "overflow": "hidden"}
                ),
                flex="1",
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
    )


def card() -> rx.Component:
    return rx.card(
        content(f"/{PageState.index + 1}/{PageState.index + 1}.mp4", f"/{PageState.index + 1}/{PageState.index + 1}_"),
        size='1',
        bg=color.th.value,
        style={"width": "100%"},
    )