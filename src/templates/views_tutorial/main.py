import flet as ft
import pages

def main(page: ft.Page):
    page.title = "Fixed Navbar Example"
    page.padding = 0  # Remove padding so the navbar touches the edges

    # 1. Create the 'Body' container
    # This acts as a placeholder for our changing content.
    # We set expand=True so it takes up all available space above the navbar.
    body = ft.Container(expand=True, padding=20)

    # 2. Define the Routing Logic
    def route_change(e: ft.RouteChangeEvent):
        """
        When the URL changes, we update the body content
        and ensure the navbar highlights the correct icon.
        """
        route = e.route
        
        # Update Body Content
        if route == "/" or route == "":
            body.content = pages.get_home_content()
            nav_bar.selected_index = 0
        elif route == "/settings":
            body.content = pages.get_settings_content()
            nav_bar.selected_index = 1
        elif route == "/profile":
            body.content = pages.get_profile_content()
            nav_bar.selected_index = 2
        
        # We must explicitly call update() on the body to render the change
        body.update()
        nav_bar.update()

    # 3. Create the Navigation Bar
    # This is defined ONCE and never re-created.
    def on_nav_change(e):
        # We use page.go to change the URL, which triggers on_route_change
        index = e.control.selected_index
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/settings")
        elif index == 2:
            page.go("/profile")

    nav_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Settings"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Profile"),
        ]
    )

    # 4. Assemble the Layout
    # We use a Column to stack the Body (top) and Navbar (bottom).
    layout = ft.Column(
        controls=[
            body,
            nav_bar
        ],
        expand=True, # Expand the column to fill the page
        spacing=0    # No space between body and nav
    )

    # 5. Initialize
    page.on_route_change = route_change
    page.add(layout)
    
    # Trigger initial route
    page.go("/")

ft.app(target=main)
