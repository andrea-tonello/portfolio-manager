import flet as ft

def toggle_icon(e):
    current_icon = e.control.icon
    e.control.icon = e.control.data
    e.control.data = current_icon
    e.control.update()


def str_to_dropdown(str_list: list) -> list:
    str_list = [str(item) for item in str_list]
    if not str_list:
        return []
    
    dropdown_options = [
        ft.DropdownOption(
            key=item,
            content=ft.Text(
                item, 
                size=16,
                weight=ft.FontWeight.BOLD if index == 0 else ft.FontWeight.NORMAL
            )
        ) 
        for index, item in enumerate(str_list)
    ]
    
    return dropdown_options