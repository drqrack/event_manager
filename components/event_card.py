from nicegui import ui

def show_event_card(event):
    with ui.card().on(
            type="click",
            handler=lambda: ui.navigate.to(f"/event?id={event["id"]}")
    ).classes("cursor-pointer"):
                        ui.label(text=event["title"])
                        ui.image(source=event["image"]).classes("rounded-lg transform transition-transform duration-500 hover:scale-105")
                        ui.label(text=event["description"]).classes("font-bold text-lg")
                        with ui.row():
                            ui.label(text=event["start_date"]).classes('text-blue-500 text-sm')
                            ui.label(text=event["start_time"]).classes('text-blue-500 text-sm')
                        ui.label(text=event["venue"]).classes('text-gray-700 text-sm')