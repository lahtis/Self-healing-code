import flet as ft
from shl.core.language_manager import LanguageManager
from shl.ui.components.SHLComponent import SHLComponent
from shl.adapters.flet_adapter import FletAdapter
from shl.middleman.manager import MiddlemanManager
from shl.middleman.user_middleman import UserMiddleman
from shl.core.form_engine import FormEngine

class User:
    def __init__(self, name):
        self.name = name

def main(page: ft.Page):
    page.title = "SHL Flet Demo"
    page.padding = 20

    lang = LanguageManager("fi")
    adapter = FletAdapter(lang)

    middle = MiddlemanManager()
    middle.register(UserMiddleman())

    engine = FormEngine(adapter, lang, middle)

    components = [
        SHLComponent("user_name"),
        SHLComponent("action_button")
    ]

    form = engine.create_form(components)

    for widget in form.values():
        page.add(widget)

    user = User(name="Tuomas")
    engine.fill_form(user, components)

    def switch_language(e):
        lang.set_language("en")
        engine.refresh_language(components)
        page.update()

    page.add(ft.ElevatedButton("Switch Language", on_click=switch_language))

if __name__ == "__main__":
    ft.app(target=main)
