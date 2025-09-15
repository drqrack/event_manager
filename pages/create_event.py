from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/create_event')
def show_create_event_page():
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    show_navbar()
    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Create Event").classes("font-bold text-3xl mb-4")
        with ui.card().classes("font-bold shadow-2xl"):
            ui.label("Event Title")
            ui.input(placeholder="Enter title").props("outlined").classes("w-full")
            ui.label("Event Venue")
            ui.input(placeholder="Enter the venue").props("outlined").classes("w-full")
            with ui.row():
                ui.label("Start Time")
                ui.label("End Time")
            with ui.row():
                ui.input(placeholder="Enter your starting time").props("outlined")
                ui.input(placeholder="Enter your ending time").props("outlined")
            with ui.row():
                ui.label("Start Date")
                ui.label("End Date")
            with ui.row():
                ui.input(placeholder="Enter your starting date").props("outlined")
                ui.input(placeholder="Enter your ending date").props("outlined")

    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Event Description").classes("font-bold text-3xl mb-4")
        with ui.card().classes("font-bold shadow-2xl mb-8"):
            ui.label("Event Image")
            
            ui.label("Event Description")
            ui.input(placeholder="Type here...")

        ui.button("Create Event").props("color=orange-7").classes("w-1/4")
    show_footer()