import flet as ft

def create_adaptive_control(base_class):
    """
    Dynamically creates a class inheriting from the provided base_class
    with adaptive icon logic injected (iOS/Android).
    """
    class AdaptiveControl(base_class):
        def __init__(self, ios_icon, android_icon, ios_selected, android_selected, *args, **kwargs):
            # Store our custom attributes
            self._ios_icon = ios_icon
            self._android_icon = android_icon
            self._ios_selected = ios_selected
            self._android_selected = android_selected
            
            # Initialize the base Flet class
            super().__init__(*args, **kwargs)

        def build(self):
            # Check platform
            is_apple = self.page.platform in [ft.PagePlatform.IOS, ft.PagePlatform.MACOS]

            # Update icons
            self.icon = self._ios_icon if is_apple else self._android_icon
            
            target_selected = self._ios_selected if is_apple else self._android_selected
            self.icon_selected = target_selected
            
            # Helper for standard Flet controls that use 'selected_icon'
            if hasattr(self, "selected_icon"):
                self.selected_icon = target_selected
            
            # Call the original build if it exists
            if hasattr(super(), "build"):
                return super().build()

    return AdaptiveControl

AdaptiveNavigationBarDestination = create_adaptive_control(ft.NavigationBarDestination)
AdaptiveIconButton = create_adaptive_control(ft.IconButton)
AdaptiveFloatingActionButton = create_adaptive_control(ft.FloatingActionButton)
AdaptiveElevatedButton = create_adaptive_control(ft.ElevatedButton)

class TitleAppbar(ft.AppBar):
    def __init__(self, text:str, text_size:int):
        super().__init__()
        self.text=text
        self.text_size=text_size
        self.toolbar_height=100
        self.bgcolor=ft.Colors.SURFACE
        self.surface_tint_color=ft.Colors.TRANSPARENT
        self.center_title=True
        self.title=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    margin=ft.margin.only(top=10, bottom=5),
                    content=ft.Text(text, size=text_size),
                ),
                ft.Container(content=ft.Divider())
            ]
        )

class OptionButton(ft.Container):
    def __init__(self, text:ft.Text, icon:ft.Icon, margin_top:float=0, margin_bottom:float=10):
        super().__init__()
        self.width=350
        self.height=80
        self.margin=ft.margin.only(top=margin_top, bottom=margin_bottom)
        self.content=ft.FloatingActionButton(
            width=self.width,
            height=self.height,
            bgcolor=ft.Colors.SECONDARY_CONTAINER,
            content=ft.ResponsiveRow(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=self.width,
                        margin=ft.margin.only(left=25),
                        col={"xs": 9, "sm": 9},
                        content=text
                    ),
                    ft.Container(
                        width=self.width,
                        col={"xs": 3, "sm": 3},
                        content=icon
                    )
                ]    
            )
        )


class LittleHeader(ft.Container):
    def __init__(self, text:ft.Text):
        super().__init__()
        self.padding = ft.padding.only(left=15, top=20, bottom=5)
        self.content=ft.Text(
            value=text,
            color=ft.Colors.PRIMARY, # Matches the color in your image
            weight=ft.FontWeight.BOLD,
            size=14, 
        )