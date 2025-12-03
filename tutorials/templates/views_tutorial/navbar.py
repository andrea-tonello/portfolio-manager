import flet as ft

def create_navbar(page: ft.Page, selected_index: int):
    """
    Creates a NavigationBar with specific routing logic.
    The selected_index helps highlight the correct tab.
    """

    def navigate(e):
        # Map indices to routes
        index = e.control.selected_index
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/settings")
        elif index == 2:
            page.go("/profile")

    return ft.NavigationBar(
        selected_index=selected_index,
        on_change=navigate,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ]
    )
