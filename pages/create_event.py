from nicegui import ui
from components.navbar import show_navbar
import requests
from utils.api import base_url

_event_image = None

def _handle_image_upload(event):
    global _event_image
    _event_image = event.content

# function to create a post event
def _post_event(data, files):
    response = requests.post(url=f"{base_url}/events", data=data, files=files)
    if response.status_code == 200:
        ui.notify(
            message= "Events added successfully!",
            type="positive")
        return ui.navigate.to("/")
    elif response.status_code == 422:
        return ui.notify(message="Please ensure all inputs are filled!", type="postive")
    # print(response.status_code)
    json_data = response.json()
    # print(json_data)

@ui.page('/create_event')
def show_create_event_page():
    ui.query(".nicegui-content").classes('m-0 p-0 gap-0')
    # ui.query('.q-uploader__header').classes('bg-orange-500')
    show_navbar()
    # main container
    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Create Event").classes("font-bold text-2xl mb-4")
        with ui.card().classes("font-bold shadow-lg w-[40%] p-8"):
            ui.label("Event Title")
            event_title = ui.input(placeholder="Enter title").props("outlined").classes("w-full")
            ui.label("Event Venue")
            event_venue = ui.input(placeholder="Enter the venue").props("outlined").classes("w-full")

            with ui.row().classes("flex flex-row justify-between w-full"):
                event_start_time = ui.input(label='Start Time' ,placeholder="Start Time").props('type=time outlined').classes('cursor-pointer w-1/3')
                event_end_time = ui.input(label='End Time' ,placeholder="End Time").props('type=time outlined').classes('cursor-pointer w-1/3') 

                

            with ui.row().classes("flex flex-row justify-between w-full"):
                event_start_date = ui.input(label="Start Date").props('type=date outlined')
                event_end_date = ui.input(label="End Date").props('type=date outlined')

    with ui.element("div").classes("w-screen h-screen items-center justify-center flex flex-col bg-orange-50"):
        ui.label("Event Description").classes("font-bold text-2xl mb-4")
        with ui.card().classes("font-bold shadow-lg w-[40%] p-8 mb-8 flex flex-col justify-center items-center"):
            with ui.column().classes("w-full"):
                ui.label("Event Image")
                ui.upload(label="Select an image", auto_upload=True, on_upload=_handle_image_upload).classes('w-full').props('color=orange')
                ui.label("Event Description")
                event_description = ui.input(placeholder="Type here...").classes('w-full').props("type=text-area outlined")

            ui.button("Create Event", on_click=lambda: _post_event(
                data={
                    "title": event_title.value,
                    "venue": event_venue.value,
                    "start_time": event_start_time.value,
                    "end_time": event_end_time.value,
                    "start_date": event_start_date.value,
                    "end_date": event_end_date.value,
                    "description": event_description.value
                },
                files={"image": _event_image}
            )).props("flat dense no-caps").classes("w-1/2 bg-orange-600 p-2 text-white text-sm rounded-lg")
