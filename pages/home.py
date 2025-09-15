from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/')
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    show_navbar()
    with ui.element('main').classes("w-full h-screen px-5"):
        with ui.element("div").classes("bg-[url('/assets/home.jpg')] bg-cover bg-center w-full h-[70%] flex flex-col justify-center items-center text-center rounded-3xl"):
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

            # with ui.row().classes("absolute -bottom-10"):
            #     ui.select([1, 2, 3])
            #     ui.select([1, 2, 3])
            #     ui.select([1, 2, 3])



        with ui.element("section").classes("w-full h-screen"):
            with ui.row().classes("w-full bg-transparent flex flex-row justify-between items-center text-center px-10 py-10"):
                with ui.row().classes("font-bold gap-0 space-x-2 text-center"):
                    ui.label('Upcoming').classes('text-3xl font-bold text-gray-800 mb-8')
                    ui.label('Events').classes('text-3xl font-bold text-orange-600 mb-8')
                with ui.row():
                    weekdays = ['Weekdays', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                    ui.select(label="", value='Weekdays', options=weekdays)
                    weekdays = ['Event Type', 'Indoor', 'Outdoor']
                    ui.select(label="", value='Event Type', options=weekdays)
                    ui.select([1,2,3])
            with ui.grid(columns=3):
                for i in range(6):
                    with ui.card():
                        ui.label("Event Title")

    show_footer()