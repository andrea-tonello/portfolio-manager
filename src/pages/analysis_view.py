import flet as ft
from translator import Translator
from utils import toggle_icon
from create_controls import *
translator = Translator(language_code="it")

class AnalysisView(ft.Container):
    def __init__(self, page: ft.Page, account_options_dropdown, num_operations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.account_options = account_options_dropdown
        self.num_operations = num_operations
        
        account_selection = ft.Container(
            content=ft.Dropdown(
                width=310,
                text_size=19,
                filled=True,
                fill_color=ft.Colors.ON_INVERSE_SURFACE,
                border_color=ft.Colors.SECONDARY,
                focused_border_color=ft.Colors.INVERSE_PRIMARY,     # this does not apply for some fucking reason
                border_width=3,
                focused_border_width=8,                             # this does not apply for some fucking reason
                border_radius=ft.border_radius.all(15),
                trailing_icon=ft.Icons.KEYBOARD_ARROW_DOWN,
                selected_trailing_icon=ft.Icons.KEYBOARD_ARROW_UP,
                
                options=self.account_options, 
                value=translator.get("account_selection.select_prompt"),
            ),
            padding=10,
            margin=ft.margin.only(left=20, right=20, bottom=10)
        )

        cash_op = OptionButton(
            text = ft.Text(translator.get("operations.cash"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED)
        )
        etf_op = OptionButton(
            text = ft.Text(translator.get("operations.etfs"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_OUTLINED)
        )
        stock_op = OptionButton(
            text = ft.Text(translator.get("operations.stocks"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_OUTLINED)
        )
        bond_op = OptionButton(
            text = ft.Text(translator.get("operations.bonds"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_OUTLINED)
        )

        home_outer_container = ft.Container(
            #height=1000,
            #bgcolor=ft.Colors.TERTIARY,
            alignment=ft.alignment.center,
            content=ft.Column(
                #alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    account_selection,
                    cash_op,
                    etf_op,
                    stock_op,
                    bond_op
                ],
            )
        )    
        

        self.content = home_outer_container
    
        self.page.update()