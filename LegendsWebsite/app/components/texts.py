import reflex as rx

from LegendsWebsite.Styles import color
from LegendsWebsite.app.components.navbar import PageState

        
def text() -> rx.Component:
    return rx.heading(PageState.cont_txt, size="3", color=color.pr_2.value, justify="start", align='left', style={"max-width": "50%",'white-space': 'pre-wrap'})