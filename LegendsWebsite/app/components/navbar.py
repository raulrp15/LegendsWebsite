import reflex as rx
from LegendsWebsite.Styles import color, size

# Asegúrate de tener 4 contenidos en la lista o de ajustarla según tus necesidades.
content_list = [
    "Deives Urke",
    "Elbow oak",
    "Queen Donn Testimony",
    "Mystery of the Deep"  # Contenido adicional para el botón 4.
]

class PageState(rx.State):
    index: int = 0

    def set_index(self, new_index: int):
        self.index = new_index

    @rx.var
    def content(self) -> str:
        return content_list[self.index]
    
    @rx.var
    def cont_txt(self) -> str:
        # Asegúrate de que la ruta y la estructura de archivos correspondan a tus contenidos.
        return open(f'assets/{self.index + 1}/{self.index + 1}.txt', 'r', encoding='utf-8').read()

    # Propiedades reactivas para el color de fondo de cada botón.
    @rx.var
    def button_bg_0(self) -> str:
        return "gray" if self.index == 0 else "transparent"
    
    @rx.var
    def button_bg_1(self) -> str:
        return "gray" if self.index == 1 else "transparent"
    
    @rx.var
    def button_bg_2(self) -> str:
        return "gray" if self.index == 2 else "transparent"
    
    @rx.var
    def button_bg_3(self) -> str:
        return "gray" if self.index == 3 else "transparent"

def button_selector():
    return rx.hstack(
        rx.button(
            content_list[0],
            on_click=lambda: PageState.set_index(0),
            bg=PageState.button_bg_0,
        ),
        rx.button(
            content_list[1],
            on_click=lambda: PageState.set_index(1),
            bg=PageState.button_bg_1,
        ),
        rx.button(
            content_list[2],
            on_click=lambda: PageState.set_index(2),
            bg=PageState.button_bg_2,
        ),
        rx.button(
            content_list[3],
            on_click=lambda: PageState.set_index(3),
            bg=PageState.button_bg_3,
        ),
        spacing="2",
        align="center",
        justify="center",
        padding="2",
    )
