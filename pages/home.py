from nicegui import ui

def show_home_page():
    ui.label("Welcome to the Home Page")
    with ui.row():
        ui.link("Signup", "/signup")
        ui.link("Signin", "/signin")
        with ui.link("", "/not_found"):
            ui.button("Don't Click")