import flet as ft

class MyColors:
    SURFACE_L = "#a1cbe4"
    SURFACE_D = "#0D1B44"

    PRIMARY_L = "#6fadd1"
    PRIMARY_D = "#192f5f"
    PRIMARY_CONTAINER_L = "#6fadd1"
    PRIMARY_CONTAINER_D = "#192f5f"




class LightTheme(ft.Theme):
    def __init__(self):
        super().__init__()
        self.navigation_bar_theme=ft.NavigationBarTheme(
            indicator_color=MyColors.SURFACE_L,
            bgcolor=MyColors.PRIMARY_L,
            label_text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
            ),
        )
        self.color_scheme = ft.ColorScheme(
            surface=MyColors.SURFACE_L,
            primary_container=MyColors.PRIMARY_CONTAINER_L,
            primary=MyColors.PRIMARY_L,
            on_primary=ft.Colors.WHITE,
            on_surface=ft.Colors.WHITE,
        )

class DarkTheme(ft.Theme):
    def __init__(self):
        super().__init__()
        self.navigation_bar_theme=ft.NavigationBarTheme(
            indicator_color=MyColors.SURFACE_D,
            bgcolor=MyColors.PRIMARY_D,
            label_text_style=ft.TextStyle(
                color=ft.Colors.WHITE,
            ),
        )
        self.color_scheme = ft.ColorScheme(
            surface=MyColors.SURFACE_D,
            primary_container=MyColors.PRIMARY_CONTAINER_D,
            primary=MyColors.PRIMARY_D,
            on_primary=ft.Colors.WHITE,
            on_surface=ft.Colors.WHITE,
        )