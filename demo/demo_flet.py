import flet as ft

from shl.core.language_manager import LanguageManager
from shl.ui.components.SHLComponent import SHLComponent
from shl.adapters.flet_adapter import FletAdapter
from shl.middleman.manager import MiddlemanManager
from shl.middleman.user_middleman import UserMiddleman
from shl.core.form_engine import FormEngine


# -------------------------
# Example data model
# -------------------------
class User:
    def __init__(self, name):
        self.name = name


# -------------------------
# Flet demo app
# -------------------------
def main(page: ft.Page):
    page.title = "SHL Flet Demo"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    # SHL core components
    lang = LanguageManager("fi")
    adapter = FletAdapter(lang)

    middle = MiddlemanManager()
    middle.register(UserMiddleman())

    engine = FormEngine(adapter, lang, middle)

    # SHL components
    components = [
        SHLComponent("user_name"),
        SHLComponent("action_button")
    ]

    # Create UI widgets
    form = engine.create_form(components)

    # Add widgets to page
    for widget in form.values():
        page.add(widget)

    # Example data
    user = User(name="Tuomas")

    # Fill form with data
    engine.fill_form(user, components)

    # Language switch button
    def switch_language(e):
        lang.set_language("en")
        engine.refresh_language(components)
        page.update()

    page.add(ft.ElevatedButton("Switch Language", on_click=switch_language))

    def create_button(self, component, on_click=None):
        label = self.lang.get_text(component.text_keys.get("label"))
    return ft.ElevatedButton(text=label, on_click=on_click)


# Run Flet app
if __name__ == "__main__":
    ft.app(target=main)
