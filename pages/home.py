from nicegui import ui

def show_home_page():
    with ui.element("div").classes("bg-[url('/assets/home.jpg')] bg-cover bg-center w-full h-screen flex flex-col justify-center items-center text-center"):
        with ui.column().classes("text-white text-7xl font-bold items-center"):
            ui.label("MADE FOR THOSE")
            ui.label("WHO DO")

        with ui.row():
                ui.link("Signup", "/signup")
                ui.link("Signin", "/signin")
                with ui.link("", "/not_found"):
                    ui.button("404 page ")
                with ui.link("", "/create_event"):
                    ui.button("create Event ")
                with ui.link("", "/event"):
                    ui.button("event")
                with ui.link("", "/not_found"):
                    ui.button("404 page ")
                with ui.link("", "/college"):
                    ui.button("College")
