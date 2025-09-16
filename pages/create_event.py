from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/create_event')
def show_create_event_page():
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    show_navbar()
    # main container
    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Create Event").classes("font-bold text-2xl mb-4")
        with ui.card().classes("font-bold shadow-2xl w-[40%] p-8"):
            ui.label("Event Title")
            ui.input(placeholder="Enter title").props("outlined").classes("w-full")
            ui.label("Event Venue")
            ui.input(placeholder="Enter the venue").props("outlined").classes("w-full")

            with ui.row().classes("flex flex-row justify-around w-full"):
                ui.input(label='Start Time' ,placeholder="Start Time").props('type=time outlined').classes('cursor-pointer w-1/3')
                ui.input(label='End Time' ,placeholder="End Time").props('type=time outlined').classes('cursor-pointer w-1/3')

                

            with ui.row().classes("flex flex-row justify-around w-full"):
                ui.input(label="Start Date").props('type=date outlined')
                ui.input(label="End Date").props('type=date outlined')
            #     with ui.input('Start Date').props('outlined') as date:
            #         with date.add_slot('append'):
            #             ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
            #         with ui.menu() as menu:
            #             ui.date().bind_value(date)

            #     with ui.input('End Date').props('outlined') as date:
            #         with date.add_slot('append'):
            #             ui.icon('edit_calendar').on('click', lambda: menu.open()).classes('cursor-pointer')
            #         with ui.menu() as menu:
            #             ui.date().bind_value(date)

    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Event Description").classes("font-bold text-2xl mb-4")
        with ui.card().classes("font-bold shadow-2xl w-[40%] p-8 mb-8"):
            ui.label("Event Image")
            ui.upload(auto_upload=True, on_multi_upload=True).classes('w-full')
            ui.label("Event Description")
            ui.input(placeholder="Type here...").classes('w-full')

        ui.button("Create Event").props("flat dense no-caps").classes("w-1/3 bg-orange-600 p-2 text-white text-lg rounded-lg")
    show_footer()