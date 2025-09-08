from nicegui import ui

def show_college_page():
    with ui.element("div").classes("w-full px-10 py-10"):
        with ui.element("div").classes("w-full h-[380px] bg-[url('/assets/college1.jpg')] bg-cover bg-center"):
        # ui.image("/assets/college2.jpg").classes("w-full h-full object-fill")
            ui.label("")
        ui.label("IIT Roorke")
        ui.label(
                "DesignHub organized a 3D Modeling Workshop using Blender on 16th February at 5 PM. The workshop taught participants the magic of creating stunning 3D models and animations using Blender. It was suitable for both beginners and experienced users. The event was followed by a blender-render competition, which added to the excitement."
            ).classes("text-sm mb-4")