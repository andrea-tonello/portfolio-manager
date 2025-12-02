import flet as ft

def get_home_content():
    return ft.Column(
        [
            ft.Text("Home Page", size=30, weight="bold"),
            ft.Container(
                content=ft.Text("This is the main dashboard."),
                padding=20,
                bgcolor=ft.Colors.SURFACE,
                border_radius=10,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def get_settings_content():
    return ft.Column(
        [
            ft.Text("Settings", size=30, weight="bold"),
            ft.Switch(label="Notifications", value=True),
            ft.Switch(label="Dark Mode", value=False),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

def get_profile_content():
    return ft.Column(
        [
            ft.Icon(ft.Icons.PERSON, size=80),
            ft.Text("User Profile", size=20),
            ft.ElevatedButton("Log Out")
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )