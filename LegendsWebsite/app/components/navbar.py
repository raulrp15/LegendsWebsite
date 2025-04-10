import reflex as rx

from LegendsWebsite.Styles import color, size

content_list = ["Lake Urke Goddess", "Elbow oak", "Queen Donn Testimony"]

class PageState(rx.State):
    index: int = 0

    def next(self):
        if self.index < len(content_list) - 1:
            self.index += 1

    def prev(self):
        if self.index > 0:
            self.index -= 1

    @rx.var
    def content(self) -> str:
        return content_list[self.index]
    
    @rx.var
    def cont_txt(self) -> str:
        return open (f'assets/{self.index + 1}/{self.index + 1}.txt', 'r', encoding='utf-8').read()

def arrow_selector():
    return rx.hstack(
        rx.button(
            rx.icon("arrow-left", size=(int(size.md.value) * 10)),
            on_click=PageState.prev,
            is_disabled=PageState.index == 0,
            bg="transparent"
        ),

        rx.heading(
            PageState.content,
            size=size.lg.value,
            color=color.pr_1.value,
            justify="center",
            align="center",
            key="content-heading"
        ),

        rx.button(
            rx.icon("arrow-right", size=(int(size.md.value) * 10)),
            on_click=PageState.next,
            is_disabled=PageState.index == len(content_list) - 1,
            bg="transparent"
        ),

        spacing="2",
        align="center",
        justify="center",
        padding="2",
    )
