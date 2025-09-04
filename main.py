from nicegui import ui
from pages.home import show_home_page
from pages.signin import show_signin_page
from pages.signup import show_signup_page
from pages.event import show_event_page
from pages.college import show_college_page
from pages.create_event import show_create_event_page
from pages.not_found import show_not_found_page
from components.navbar import show_navbar
from components.footer import show_footer

@ui.page("/")
def home_page():
    show_navbar()
    show_home_page()
    show_footer()


@ui.page("/signin")
def signin_page():
    show_signin_page()


@ui.page("/signup")
def signup_page():
    show_signup_page()


@ui.page("/event")
def event_page():
    show_navbar()
    show_event_page()
    show_footer()


@ui.page("/college")
def college_page():
    show_navbar()
    show_college_page()
    show_footer()


@ui.page("/create_event")
def create_event_page():
    show_navbar()
    show_create_event_page()


@ui.page("/not_found")
def not_found_page():
    show_navbar()
    show_not_found_page()
    show_footer()


ui.run()
