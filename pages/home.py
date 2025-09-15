from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    show_navbar()
    with ui.element("div").classes("bg-[url('/assets/home.jpg')] bg-cover bg-center w-full h-screen flex flex-col justify-center items-center text-center"):
        with ui.column().classes("text-white text-7xl font-bold items-center"):
            ui.label("MADE FOR THOSE")
            ui.label("WHO DO")

        with ui.row():
                ui.link("Signup", "/signup")
                ui.link("Signin", "/signin")
                # with ui.link("", "/not_found"):
                ui.button("404 page ", on_click=lambda: ui.navigate.to('/not_found')).props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
                # with ui.link("", "/create_event"):
                ui.button("create Event ", on_click=lambda: ui.navigate.to('/create_event')).props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
                # with ui.link("", "/event"):
                ui.button("event", on_click=lambda: ui.navigate.to('/event')).props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
                # with ui.link("", "/not_found"):
                ui.button("404 page ", on_click=lambda: ui.navigate.to('/not_found')).props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
                # with ui.link("", "/college"):
                ui.button("College", on_click=lambda: ui.navigate.to('/college')).props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
    show_footer()