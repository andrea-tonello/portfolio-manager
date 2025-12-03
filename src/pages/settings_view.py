import flet as ft
from translator import Translator
from utils import toggle_icon
from create_controls import *
translator = Translator(language_code="it")

class SettingsView(ft.Container):
    def __init__(self, page: ft.Page, account_options, num_operations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.account_options = account_options
        self.num_operations = num_operations

    # Helper function to create the "Little Titles" (Section Headers)
        def settings_section_header(title):
            return ft.Container(
                content=ft.Text(
                    value=title,
                    color=ft.Colors.PRIMARY, # Matches the color in your image
                    weight=ft.FontWeight.BOLD,
                    size=14, 
                ),
                # Padding: Left to align, Top to separate sections, Bottom for small gap
                padding=ft.padding.only(left=15, top=20, bottom=5)
            )

        # Helper to create the toggle rows (for visual completeness)
        def settings_tile(icon_name, title, subtitle=None, trailing=None):
            return ft.ListTile(
                title=ft.Text(title),
                subtitle=ft.Text(subtitle) if subtitle else None,
                trailing=trailing,
                content_padding=ft.padding.symmetric(horizontal=15)
            )

        def filled_button(title):
            return ft.FilledButton(
                title, bgcolor=ft.Colors.PRIMARY, scale=1.1
            )

        switch = ft.Switch(value=True, active_color=ft.Colors.PRIMARY)
        
        settings_outer_container = ft.Container(
            #height=1000,
            #bgcolor=ft.Colors.TERTIARY,
            alignment=ft.alignment.center,
            content=ft.Column(
                #alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    settings_section_header(translator.get("settings.header_1")),
                    
                    settings_tile(
                        "palette", 
                        translator.get("settings.theme.name"), 
                        trailing=filled_button(translator.get("settings.theme.system"))
                    ),
                    settings_tile(
                        "format_paint", 
                        translator.get("settings.material.name"), 
                        translator.get("settings.material.description"),
                        trailing=switch
                    ),
                    settings_tile(
                        "language", 
                        translator.get("settings.language.name"), 
                        translator.get("settings.language.it")
                    ),
                    
                    ft.Container(
                        margin=ft.margin.only(left=30, right=30),
                        content=ft.Divider()
                    ),

                    # --- SECTION 2: ADVANCED ---
                    settings_section_header(translator.get("settings.header_2")),
                    
                    settings_tile(
                        "update", 
                        "Auto update patches", 
                        "Automatically update patches to the latest version",
                        trailing=switch
                    ),
                    settings_tile(
                        "visibility", 
                        "Show update dialog", 
                        "Show a dialog when a new update is available",
                        trailing=switch
                    ),
                ],
            )
        )    
        

        self.content = settings_outer_container
    
        self.page.update()