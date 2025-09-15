from nicegui import ui
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page('/not_found')
def show_not_found_page():
    ui.query('.nicegui-content').classes('m-0 p-0 gap-0')
    ui.add_head_html(
        '<script src="https://kit.fontawesome.com/ccba89e5d4.js" crossorigin="anonymous"></script>'
    )
    show_navbar()
    with ui.element("div").classes(
        "w-full h-screen flex flex-col justify-center items-center"
    ):
        ui.image("/assets/404page.png").classes("h-3/4 mb-4")
        # with ui.link("", "/"):
        ui.button("Back to Homepage", on_click=lambda: ui.navigate.to("/")).props("color=orange-7").classes("mb-4 px-8")

        ui.label("Follow us on").classes("mb-4")

        with ui.row().classes("text-black text-2xl "):
            ui.html('<i class="fa-brands fa-facebook"></i>').classes(
                "hover:text-orange-600 cursor-pointer"
            )
            ui.html('<i class="fa-brands fa-instagram"></i>').classes(
                "hover:text-orange-600 cursor-pointer"
            )
            ui.html('<i class="fa-brands fa-linkedin"></i>').classes(
                "hover:text-orange-600 cursor-pointer"
            )
    show_footer()