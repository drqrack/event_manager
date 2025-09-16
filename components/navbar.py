from nicegui import ui

def show_navbar():
    ui.query(".nicegui-content").classes("m-o p-0 gap-0")
    with ui.element().classes(
        "w-full bg-transparent flex flex-row justify-between items-center px-10 py-5"
    ):
        with ui.row().classes("font-bold text-3xl space-x-2 gap-0"):
            ui.label("Event").classes("")
            ui.label("Hive").classes("text-orange-600")

        with ui.row().classes("flex items-center gap-0"):
            ui.button("Login", on_click=lambda: ui.navigate.to('/signin')).props("no-caps flat dense").classes("text-black bg-transparent px-4 py-2 text-lg")
            ui.button("Signup", on_click=lambda: ui.navigate.to('/signup')).props("no-caps flat dense").classes("bg-orange-600 text-white px-4 py-2 text-lg")
