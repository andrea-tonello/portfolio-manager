import flet as ft
from translator import Translator
from utils import *
from create_controls import *
translator = Translator(language_code="it")

class SettingsView(ft.Container):
    def __init__(self, page: ft.Page, account_options, num_operations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.account_options = account_options
        self.num_operations = num_operations

        T_BLUE = translator.get("settings.palette.blue")
        T_TEAL = translator.get("settings.palette.teal")
        T_GREEN = translator.get("settings.palette.green")
        T_YELLOW = translator.get("settings.palette.yellow")
        T_ORANGE = translator.get("settings.palette.orange")
        T_RED = translator.get("settings.palette.red")
        T_VIOLET = translator.get("settings.palette.violet")
        T_PURPLE = translator.get("settings.palette.purple")


        # Updated helper to create clickable toggle rows
        def tile_with_switch(title, subtitle=None, default_value=True):
            # Create the switch as a separate object so we can reference it
            switch = ft.Switch(value=default_value, active_color=ft.Colors.PRIMARY)
            # Define the click handler that toggles the switch
            def on_tile_click(e):
                switch.value = not switch.value
                switch.update()
            return ft.ListTile(
                title=ft.Text(title),
                subtitle=ft.Text(subtitle) if subtitle else None,
                trailing=switch,
                content_padding=ft.padding.symmetric(horizontal=30),
                on_click=on_tile_click
            )

        def expansion_tile(title, subtitle=None, controls:list=None):
            subtitle_text = ft.Text(subtitle) if subtitle else None
            def toggle_subtitle(e):
                # Hide subtitle when expanded, show when collapsed
                if e.control.data == e.control.subtitle:  # e.data is True when expanded
                    e.control.subtitle = None
                else:
                    e.control.subtitle = e.control.data
                e.control.update()
            return ft.ExpansionTile(
                title=ft.Text(title),
                subtitle=subtitle_text,
                maintain_state=True,
                tile_padding=ft.padding.symmetric(horizontal=30),
                data=subtitle_text,  # Store original subtitle
                controls=controls if controls else [],
                on_change=toggle_subtitle
            )

        # Helper for tiles with buttons (non-toggle)
        def tile_with_button(title, subtitle=None, button_text=None, button_icon=ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=16), on_button_click=None):
            if button_text:     # Only create button if button_text is provided
                button = ft.FilledButton(
                    button_text, 
                    bgcolor=ft.Colors.PRIMARY, 
                    scale=1.1,
                    on_click=on_button_click
                )
            else: # Use an icon as trailing indicator
                button = button_icon    
            # For button tiles, clicking the tile triggers the button action
            def on_tile_click(e):
                if on_button_click:
                    on_button_click(e)
            return ft.ListTile(
                title=ft.Text(title),
                subtitle=ft.Text(subtitle) if subtitle else None,
                trailing=button,
                content_padding=ft.padding.symmetric(horizontal=30) if subtitle else ft.padding.only(top=4, bottom=4, left=30, right=30),
                on_click=on_tile_click
            )

        def on_theme_click(e):
            # e.control is the RadioGroup
            # e.control.value contains the value of the selected Radio
            selected_value = e.control.value
            color_map = {
                T_BLUE: ft.Colors.BLUE,
                T_TEAL: ft.Colors.TEAL,
                T_GREEN: ft.Colors.GREEN,
                T_YELLOW: ft.Colors.YELLOW,
                T_ORANGE: ft.Colors.ORANGE,
                T_RED: ft.Colors.RED,
                T_PURPLE: ft.Colors.PURPLE,
                T_VIOLET: ft.Colors.INDIGO,
            }
            selected_color = color_map.get(selected_value)
            if selected_color:
                page.theme = ft.Theme(color_scheme_seed=selected_color)
                page.update()

        palette_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(translator.get("settings.palette.name")),
            content=ft.RadioGroup(
                content=ft.Column(
                    controls=[
                        ft.Radio(value=T_BLUE, label=T_BLUE),
                        ft.Radio(value=T_TEAL, label=T_TEAL),
                        ft.Radio(value=T_GREEN, label=T_GREEN),
                        ft.Radio(value=T_YELLOW, label=T_YELLOW),
                        ft.Radio(value=T_ORANGE, label=T_ORANGE),
                        ft.Radio(value=T_RED, label=T_RED),
                        ft.Radio(value=T_PURPLE, label=T_PURPLE),
                        ft.Radio(value=T_VIOLET, label=T_VIOLET), 
                    ]
                ),
                on_change=on_theme_click
            ),
            actions=[
                ft.TextButton(translator.get("navigation.cancel"), on_click=lambda e: page.close(palette_dialog)),
                ft.TextButton(translator.get("navigation.proceed"), on_click=lambda e: page.close(palette_dialog)),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
            





        def on_language_click(e):
            print("Language button clicked")
            # Add your language change logic here


    # RESET OPTION ========================================================================================
        
        def open_and_close(e):
            page.close(first_reset_dialog)
            page.open(second_reset_dialog)
        def close_and_reset(e):
            page.close(second_reset_dialog)
            reset_app()
        def on_reset_confirm(e):
            if e.control.value == "RESET":
                second_reset_dialog.actions[1].disabled = False  
            else:
                second_reset_dialog.actions[1].disabled = True  
            second_reset_dialog.update()    

        first_reset_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(translator.get("settings.reset_app.name")),
            content=ft.Text(translator.get("settings.reset_app.first_attempt")),
            actions=[
                ft.TextButton(translator.get("navigation.cancel"), on_click=lambda e: page.close(first_reset_dialog)),
                ft.TextButton(translator.get("navigation.proceed"), on_click=open_and_close),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        second_reset_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(translator.get("settings.reset_app.name")),
            content=ft.TextField(
                text_size=12,
                border_radius=15,
                border_color=ft.Colors.TRANSPARENT,
                focused_border_color=ft.Colors.SECONDARY,
                filled=True,
                hint_text=translator.get("settings.reset_app.second_attempt"),
                on_change=on_reset_confirm
            ),
            actions=[
                ft.TextButton(translator.get("navigation.cancel"), on_click=lambda e: page.close(second_reset_dialog)),
                ft.TextButton(translator.get("navigation.confirm"), disabled=True, on_click=close_and_reset),
            ],
            actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )



    # CONTENT ===============================================================================================

        horizontal_divider = ft.Container(
            margin=ft.margin.only(left=25, right=25),
            content=ft.Divider()
        )
        account_management_tiles = [
                tile_with_button(
                    translator.get("settings.manage_accounts.add.name"),
                    on_button_click=on_language_click
                ),
                tile_with_button(
                    translator.get("settings.manage_accounts.remove.name"),
                    on_button_click=on_language_click
                ),
                tile_with_button(
                    translator.get("settings.manage_accounts.change.name"), 
                    on_button_click=on_language_click
                )
        ]
        
        scrollable_content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                LittleHeader(translator.get("settings.header_1")),
                
                tile_with_button(
                    translator.get("settings.theme.name"),
                    button_text=translator.get("settings.theme.system"),
                    on_button_click=on_theme_click
                ),
                tile_with_button(
                    translator.get("settings.palette.name"),
                    button_text=translator.get("settings.palette.blue"),
                    on_button_click=lambda e: page.open(palette_dialog)
                ),
                tile_with_button(
                    translator.get("settings.language.name"),
                    subtitle=translator.get("settings.language.it"),
                    on_button_click=on_language_click
                ),
                
                horizontal_divider,
                LittleHeader(translator.get("settings.header_2")),
                

                expansion_tile(
                    title=translator.get("settings.manage_accounts.name"),
                    subtitle=translator.get("settings.manage_accounts.description"),
                    controls=account_management_tiles
                ),

                tile_with_button(
                    translator.get("settings.reset_app.name"),
                    translator.get("settings.reset_app.description"),
                    button_icon=ft.Icon(ft.Icons.CACHED, size=20),
                    on_button_click=lambda e: page.open(first_reset_dialog)
                )
            ],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        
        self.content = scrollable_content
        self.page.update()



        """
                settings_tile(
                    translator.get("settings.add_account.name"), 
                    translator.get("settings.language.it")
                    trailing=circle_floating_button(ft.Icons.ASSIGNMENT_ADD)
                ),
                settings_tile(
                    translator.get("settings.language.name"), 
                    translator.get("settings.language.it")
                    trailing=circle_floating_button(ft.Icons.CACHED)
                ),
                settings_tile(
                    translator.get("settings.language.name"), 
                    translator.get("settings.language.it")
                    trailing=circle_floating_button(ft.Icons.CACHED)
                ),
            """