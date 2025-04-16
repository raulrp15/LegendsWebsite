import reflex as rx
from LegendsWebsite.Styles import color, size

# Lista de títulos para cada contenido.
content_list = [
    "Deives Urke",
    "Alkūninis ąžuolas",
    "Karalienės Donn pasakojimas",
    "Mystery of the Deep"
]

# Estado global de la página.
class PageState(rx.State):
    index: int = 0
    title: str = content_list[0]  # Valor inicial

    def set_index(self, new_index: int):
        self.index = new_index
        self.title = content_list[new_index]

    @staticmethod
    def get_page_title() -> str:
        # Devuelve el título actual; este método se usa en el render para obtener un string primitivo.
        return PageState.title

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
    return rx.grid(
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
        style={
            "gridTemplateColumns": "repeat(4, 1fr)",     # 4 botones en la misma fila
            "@media (max-width: 768px)": {
                "gridTemplateColumns": "repeat(2, 1fr)"  # 2 columnas cuando <=768px
            },
            "margin": "0 auto",  # Centra la grilla en horizontal
            "gap": "0.5rem"      # Ajusta el espacio entre celdas si quieres algo menor
        },
        # "spacing" y "padding" reducidos
        spacing="1",   # Espacio entre los children del grid
        align="center",
        justify="center",
        padding="0.5rem",
    )
