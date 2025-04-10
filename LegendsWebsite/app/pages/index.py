import reflex as rx

from LegendsWebsite.Styles import *
from LegendsWebsite.app.components.texts import *
from LegendsWebsite.app.components.navbar import *
from LegendsWebsite.app.components.video_audio_content import *

@rx.page(
    route='/'
)

def index() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.heading("Legends of Lithuania", size='9', color=color.pr_1.value, align="center", justify="center",),
            arrow_selector(),
            bg=color.pr_2.value,
            style={"height": "auto", "width": "100%", "border-bottom-left-radius": "5px", "border-bottom-right-radius": "5px"},
            align="center",
            padding='2dvh',
        ),
        card(),
        align="center",
        justify="between"
    )