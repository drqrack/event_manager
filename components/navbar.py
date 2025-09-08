from nicegui import ui


def show_navbar():
    with ui.element().classes(
        "w-full bg-transparent flex flex-row justify-between items-center px-10 py-4"
    ):
        with ui.row().classes("font-bold text-2xl"):
            ui.label("Event").classes("")
            ui.label("Hive").classes("text-orange-600")

        with ui.row().classes("text-sm"):
            with ui.link("", "/signin"):
                ui.button("Login").props("color=white").classes("text-black")
            with ui.link("", "/signup"):
                ui.button("Signup").props("color=orange-7").classes("")
