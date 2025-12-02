import flet as ft

# Define your own callable custom controls

class GoogleButton(ft.ElevatedButton):
    def __init__(self, content, on_click):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_300
        self.color = ft.Colors.GREEN_800
        self.content = content
        # self.text = text in a str format
        self.width = 200
        self.height = 80
        self.on_click = on_click


class AppleButton(ft.CupertinoButton):
    def __init__(self, content, on_click):
        super().__init__()
        self.bgcolor = ft.Colors.ORANGE_600
        self.color = ft.Colors.GREEN_800
        self.content = content
        # self.text = text in a str format
        self.width = 200
        self.height = 80
        self.on_click = on_click 


def main_buttons(page: ft.Page):

    def ok_clicked(e):
        print("OK clicked") # in the terminal

    def cancel_clicked(e):
        print("Cancel clicked")

    ok = ft.Text("OK", size=20)
    cancel = ft.Text("Cancel", size=20)

    page.add(
        GoogleButton(content=ok, on_click=ok_clicked),
        AppleButton(content=cancel, on_click=cancel_clicked),
    )


    page.add()


# ============================================================================================

# Custom controls can also be composed: composite custom controls inherit from container controls 
# such as Column, Row, Stack or even View to combine multiple Flet controls. The example below 
# is a Task control that can be used in a To-Do app:

class Task(ft.Row):
    def __init__(self, text):
        super().__init__()
        self.text_view = ft.Text(text)
        self.text_edit = ft.TextField(text, visible=False)
        self.edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=self.edit)
        self.save_button = ft.IconButton(
            visible=False, icon=ft.Icons.SAVE, on_click=self.save
        )
        self.controls = [
            ft.Checkbox(),
            self.text_view,
            self.text_edit,
            self.edit_button,
            self.save_button,
        ]

    def edit(self, e):
        self.edit_button.visible = False
        self.save_button.visible = True
        self.text_view.visible = False
        self.text_edit.visible = True
        self.update()

    def save(self, e):
        self.edit_button.visible = True
        self.save_button.visible = False
        self.text_view.visible = True
        self.text_edit.visible = False
        self.text_view.value = self.text_edit.value
        self.update()

def main_todo(page: ft.Page):

    page.add(
        Task(text="Do laundry"),
        Task(text="Cook dinner"),
    )



ft.app(main_todo)