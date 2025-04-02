import reflex as rx

@rx.page(
    route='/'
)

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.text("Have questions? Join our community on Discord!", size="8", color="yellow"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )

