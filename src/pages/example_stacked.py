import flet as ft
from translator import Translator

translator = Translator(language_code="it")

class TransactionDetailView(ft.Container):
    """
    Esempio di view di dettaglio che può essere "stackata" sopra la home
    """
    def __init__(self, page: ft.Page, transaction_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.page = page
        self.transaction_id = transaction_id

        # Back button che usa page.views.pop()
        def go_back(e):
            # Questo trigghera l'evento view_pop
            if len(self.page.views) > 1:
                self.page.views.pop()
                top_view = self.page.views[-1]
                self.page.go(top_view.route)

        back_button = ft.Container(
            margin=ft.margin.only(left=20, top=20, bottom=10),
            content=ft.TextButton(
                content=ft.Row([
                    ft.Icon(ft.Icons.ARROW_BACK),
                    ft.Text("Indietro", size=16)
                ]),
                on_click=go_back
            )
        )

        # Content della pagina di dettaglio
        detail_content = ft.Container(
            alignment=ft.alignment.center,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Card(
                        width=800,
                        elevation=8,
                        margin=ft.margin.only(top=20, bottom=20, left=10, right=10),
                        content=ft.Container(
                            padding=30,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.Text("Dettaglio Transazione", size=28, weight=ft.FontWeight.BOLD),
                                    ft.Divider(),
                                    ft.Text(f"ID: {transaction_id}", size=18),
                                    ft.Text("Data: 15-10-2025", size=16),
                                    ft.Text("Importo: €1000.00", size=16),
                                    ft.Text("Tipo: Acquisto", size=16),
                                    ft.Text("Asset: POET Technologies Inc.", size=16),
                                ]
                            )
                        )
                    ),
                    ft.ElevatedButton(
                        "Modifica Transazione",
                        icon=ft.Icons.EDIT,
                        width=200
                    )
                ]
            )
        )

        self.content = ft.Column(
            controls=[
                back_button,
                detail_content
            ],
            expand=True
        )


# Modifica nella home_view.py per navigare alla detail view:
# Nel metodo __init__ di HomeView, modifica recent_transactions così:
"""
def on_transaction_click(e):
    # Questo "stacka" una nuova view sulla corrente
    page.go("/transaction/detail/123")
"""
# E nel main.py, aggiungi questo case nel route_change:
"""
elif route.startswith("/transaction/detail/"):
    transaction_id = route.split("/")[-1]
    detail_appbar = ft.AppBar(
        toolbar_height=70,
        center_title=True,
        title=ft.Text("Dettaglio Transazione", size=25),
    )
    page.views.append(
        ft.View(
            route=route,
            appbar=detail_appbar,
            controls=[
                ft.SafeArea(
                    TransactionDetailView(page, transaction_id)
                ),
                nav_bar  # Navbar rimane visibile anche nella detail view
            ],
            padding=0,
        )
    )
"""