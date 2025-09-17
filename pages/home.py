from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer
from components.event_card import show_event_card
import requests
from utils.api import base_url



@ui.page('/')
def show_home_page():
    ui.query(".nicegui-content").classes("m-0 p-0 gap-0")
    show_navbar()
    with ui.element('main').classes("w-full h-screen px-10"):
        with ui.element("div").classes("bg-[url('/assets/home.jpg')] bg-cover bg-center w-full h-[80%] flex flex-col justify-center items-center text-center rounded-3xl"):
            with ui.column().classes("text-white text-7xl font-bold items-center bg-black/60 w-full h-full flex flex-col justify-center"):
                ui.label("MADE FOR THOSE")
                ui.label("WHO DO")

                with ui.row():
                    ui.link("Signup", "/signup")
                    ui.link("Signin", "/signin")
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


        with ui.element("section").classes("w-full flex flex-col justify-center items-center"):
            with ui.row().classes("w-full bg-transparent flex flex-row justify-around items-center text-center px-5 py-5"):
                with ui.row().classes("font-bold gap-0 space-x-2 text-center flex flex-row justify-center items-center"):
                    ui.label('Upcoming').classes('text-3xl font-bold text-gray-800')
                    ui.label('Events').classes('text-3xl font-bold text-orange-600')
                with ui.row().classes('flex flex-row justify-center items-center'):
                    weekdays = ['Weekdays', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                    ui.select(label="", value='Weekdays', options=weekdays).classes('w-48')
                    event_type = ['Event', 'Indoor', 'Outdoor']
                    ui.select(label="", value='Event', options=event_type)
                    category = ['Category', 'All', 'Some', 'Any', 'Nothing', 'Something']
                    ui.select(label="", value='Category', options=category)

            with ui.grid(columns=3).classes("w-[80%] h-full rounded-lg p-4 justify-center items-center"):
                response = requests.get(url=f"{base_url}/events?limit=0")
                # print(response.status_code, response.content)
                json_data = response.json()
                for event in json_data["data"]:
                    show_event_card(event)

                ui.button("Load More").props('flat dense no-caps').classes('bg-orange-600 text-white')

            with ui.row().classes('bg-orange-400 flex flex-row justify-around w-full h-full'):
                with ui.element("div").classes('w-1/3 relative'):
                    ui.image("/assets/sit.png").classes('')
                with ui.element("div").classes('w-1/3 text-white'):
                    ui.label('Make your own Event')
                    ui.label('There are so many events in Ghana. Lets go and have fun')
                    ui.button('Create Events', on_click=lambda: ui.navigate.to("/create_event"))

    # show_footer()