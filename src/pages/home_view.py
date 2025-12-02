import flet as ft
from translator import Translator
from utils import toggle_icon
from create_controls import *
translator = Translator(language_code="it")

class HomeView(ft.Container):
    def __init__(self, page: ft.Page, account_options, num_operations, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.account_options = account_options
        self.num_operations = num_operations

        self.money_integer = ft.Container(
            height=80,
            content=ft.Text("14000", size=70)
        )
        self.money_float = ft.Container(
            height=80,   # same height as the large text
            margin=ft.margin.only(top=40),
            alignment=ft.alignment.bottom_left,
            content=ft.Text(".13€", size=30)# smaller & bottom aligned
        )
        self.money_total=ft.Container(
            border_radius=15,
            expand=True,
            height=80,
            margin=ft.margin.only(left=10, top=10, bottom=30, right=10),
            content=ft.Row(
                spacing=0,
                controls=[
                    self.money_integer,
                    self.money_float
                ]
            )
        )
        self.visibility_button = ft.FloatingActionButton(
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            icon=ft.Icons.VISIBILITY,
            data=ft.Icons.VISIBILITY_OFF,
            shape=ft.CircleBorder(),
            elevation=2,
            tooltip=translator.get("home.main_card.tooltip_hide_amount"),
            on_click=self._toggle_money_visibility
        )
        self.money_display = ft.Row(
            spacing=2,  # space between integer and fractional part
            controls=[
                self.money_total,
            ],
        )
        self.money_card = ft.Card(
            width=800,
            height=300,
            elevation=8,
            margin=ft.margin.only(top=20, bottom=60, left=10, right=10),
            content=ft.Container(
                padding=10,
                content=ft.ResponsiveRow(
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    #alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            # xs=12 means full width on mobile
                            # sm=8 means it takes 2/3rds space on larger screens
                            col={"xs": 12, "sm": 7},      
                            #bgcolor="blue",                
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    self.money_display,
                                    ft.Row(
                                        controls=[
                                            ft.Container(
                                                margin=ft.margin.only(left=10),
                                                content=self.visibility_button
                                            ),
                                            ft.Column(
                                                spacing=5,
                                                controls=[
                                                    ft.Text("   "+self.account_options[0], size=18, weight=ft.FontWeight.BOLD),
                                                    ft.Text("   "+str(self.num_operations)+" "+translator.get("home.main_card.operations_literal"), size=18),
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                        ),
                        ft.Container(
                            # xs=0 means HIDDEN on mobile
                            # sm=4 means VISIBLE (taking remaining 1/3rd) on larger screens
                            col={"xs": 0, "sm": 5}, 
                            bgcolor=ft.Colors.PRIMARY_CONTAINER,
                            clip_behavior=ft.ClipBehavior.HARD_EDGE,    # prevents contents (in this case Text) to spill
                            content=ft.Text("Some text", size=14, color="black"),
                            alignment=ft.alignment.center
                        )

                    ]
                )
            )
        )
        self.recent_transactions = OptionButton(
            text = ft.Text(translator.get("home.recent_transactions"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED)
        )
        self.glossary = OptionButton(
            text = ft.Text(translator.get("home.glossary"), size=20),
            icon = ft.Icon(ft.Icons.ARROW_FORWARD_IOS_OUTLINED)
        )

        self.home_outer_container = ft.Container(
            #height=1000,
            #bgcolor=ft.Colors.TERTIARY,
            alignment=ft.alignment.center,
            content=ft.Column(
                #alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.money_card,
                    self.recent_transactions,
                    self.glossary
                ],
            )
        )    
        

        self.content = self.home_outer_container
    

    def _toggle_money_visibility(self, e):
        toggle_icon(e)
        if e.control.icon == ft.Icons.VISIBILITY_OFF:
            self.money_total.bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST
            self.money_total.content=ft.Text(translator.get("home.main_card.hidden"), size=18, opacity=0.4)
            self.money_total.alignment=ft.alignment.center
        else:
            self.money_total.bgcolor=ft.Colors.TRANSPARENT
            self.money_total.content=ft.Row(
                spacing=0,
                controls=[
                    self.money_integer,
                    self.money_float
                ]
            )
        self.page.update()