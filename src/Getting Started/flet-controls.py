import flet as ft
import time


def main_hw(page: ft.Page):
    hello = ft.Text(value="Hello, world!", color="green")
    page.controls.append(hello)
    page.update()

    steps = ft.Text()
    page.add(steps) # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(3):
        steps.value = f"Step {i}"
        page.update()
        time.sleep(0.5)

    # ROWS
    text_field_str = "Your name"
    text_field_fancy = ft.Text(value="Your name (fancy!)", color="orange", italic=True)
    page.add(
        ft.Row(controls=[
            ft.TextField(label=text_field_str),
            ft.TextField(label=text_field_fancy),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    # page.update() is smart enough to send only the changes made since its last call, 
    # so you can add a couple of new controls to the page, remove some of them, 
    # change other controls' properties and then call page.update() to do a batched update, e.g:
    for i in range(7):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)    # if i > 4, start to remove controls (FIFO order)
        page.update()
        time.sleep(0.3)

    def button_clicked(e):  # WHY IS THERE A NOT USED "e"?
        clicked_text = ft.Text("Clicked!")
        page.add(clicked_text)

        if page.controls[-1] == clicked_text:
            page.controls.pop(-1)

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

    # Every control has "visible" property which is true by default - control is rendered on the page. 
    # Setting "visible" to false completely prevents control (and all its children if any) from rendering. 
    page.add(ft.Text(value="Here is an invisible element (button) ==>"))
    page.add(ft.ElevatedButton(text="Click me", visible=False, on_click=button_clicked))

    # Every control has "disabled" property which is false by default - control and all its children are enabled. 
    # "disabled" is mostly used with data entry controls like TextField, Dropdown, Checkbox, buttons. 
    # "disabled" could be set to a parent control, and its value will be propagated down to all children.
    page.add(ft.Text(value="vvv Here are two disabled elements (textfields) vvv"))
    first_name = ft.TextField(label="XX not accessible XX")
    last_name = ft.TextField(label="XX not accessible XX")
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)



def main_todo(page: ft.Page):
    def add_clicked(e):
        page.add(ft.Checkbox(label=new_task.value))
        new_task.value = ""
        new_task.focus()
        new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))




def main_textbox(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your name")

    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=btn_click))




def main_checkbox(page: ft.Page):
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski :  {todo_check.value}."
        )
        page.update()

    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)




def main_dropdown(page: ft.Page):
    def button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(width=200, height=100, text="Submit", on_click=button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)




def main_counter1(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )

def main_counter2(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main_dropdown)
