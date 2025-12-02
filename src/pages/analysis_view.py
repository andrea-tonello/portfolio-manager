import flet as ft
from translator import Translator
from utils import toggle_icon
from create_controls import *
translator = Translator(language_code="it")

class AnalysisView(ft.Container):
    def __init__(self, page: ft.Page, account_options, num_operations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.account_options = account_options
        self.num_operations = num_operations

        horizontal_divider = ft.Container(
            margin=ft.margin.only(left=20, right=20, bottom=50),
            content=ft.Divider()
        )
        recent_transactions = OptionButton(
            text = ft.Text(translator.get("home.recent_transactions"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED)
        )
        glossary = OptionButton(
            text = ft.Text(translator.get("home.glossary"), size=20),
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
                    horizontal_divider,
                    recent_transactions,
                    glossary
                ],
            )
        )    
        

        self.content = home_outer_container
    
        self.page.update()