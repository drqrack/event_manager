from nicegui import ui

def show_footer():
    ui.add_head_html(
        '<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>'
    )

    with ui.element("footer").classes(
        "w-full h-[300px] bg-orange-700 items-center justify-center px-10 py-5"
    ):
        with ui.row().classes("items-center justify-center text-4xl font-bold mb-4"):
            ui.label("Event").classes("text-white")
            ui.label("Hive").classes("text-orange-600")

        with ui.row().classes("items-center justify-center text-white mb-8 gap-0"):
            # ui.input(placeholder="Enter your mail").props("borderless dense flat").classes(
            #     "w-[240px] h-[40px] px-2 py-1 text-sm bg-white rounded-sm"
            # )
            # ui.button("Subscribe").props("flat dense no-caps").classes("px-8 py-2 text-sm font-normal text-white w-[120px] bg-orange-900")
            ui.input(placeholder="Enter your mail").props("outlined no-caps").classes("bg-white w-64")
            ui.button("Subscribe").props("flat dense no-caps").classes("px-20 py-4 bg-orange-400")
            

        ui.html("<hr>").classes("mt-16")

        with ui.element("div").classes(
            "flex flex-row justify-between text-white px-4 py-8 items-center text-center"
        ):
            with ui.row():
                ui.label("English")
                ui.label("French")
                ui.label("Twi")

            with ui.row().classes("text-white text-xl"):
                ui.html('<i class="fa-brands fa-facebook"></i>').classes("hover:text")
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-linkedin"></i>')

            with ui.row():
                ui.html("<p>Non Copyrighted &copy; 2025 Upload by nadia studio</p>")
