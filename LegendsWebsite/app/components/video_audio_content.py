import reflex as rx

class selected_state(rx.State):
    value:str ='Lithuanian'

    @rx.event
    def change_value(self, value:str):
        self.value = value


def content() -> rx.Component:
    return rx.hstack(
        rx.video(
            url="videos/Lithuania.mp4",
            width="auto",
            height="auto",
            loop=True,
            muted=False,
        ),
        rx.select(
            ['Lithuanian', 'English', 'Spanish'],
            value=selected_state.value,
            on_change=selected_state.change_value
        ),
        rx.audio(
            url="https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
            width="400px",
            height="32px",    
        ),
        rx.badge(
            selected_state.value,
            color="red"
        )
    )