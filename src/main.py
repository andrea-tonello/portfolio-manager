import flet as ft
import os
import configparser

from translator import Translator
from utils import str_to_dropdown
from create_controls import *
from pages.home_view import HomeView
from pages.operations_view import OperationsView
from pages.analysis_view import AnalysisView
from pages.settings_view import SettingsView

LANG = {1: ("en", "English"), 2: ("it", "Italiano")}
REP_DEF = "Report "
config_folder = os.path.join(os.getcwd(), "config")
config_res_folder = os.path.join(config_folder, "resources")
os.makedirs(config_res_folder, exist_ok=True)

config_path = os.path.join(config_folder, "config.ini")
config = configparser.ConfigParser()

default_lang = LANG[1][0]    # default - en
translator = Translator(language_code=default_lang)
lang_code = None
if os.path.exists(config_path):
    config.read(config_path)
    if 'Language' in config and 'Code' in config['Language']:
        lang_code = config['Language']['Code']
"""if lang_code is None:
    lang_code = mop.select_language(translator, config_folder, LANG)
translator.load_language(lang_code)"""

translator = Translator(language_code="it")
brokers = {}
# Try to load brokers from config

if os.path.exists(config_path) and 'Brokers' in config:
    try:
        # Convert keys to int (configparser reads keys as strings)
        brokers = {int(k): v for k, v in config.items('Brokers')}
    except ValueError:
        pass
# If no brokers found (first boot or empty section), initialize
"""if not brokers:
    print(translator.get("main_menu.first_boot"))
    brokers = mop.initialize_brokers(translator, config_folder)
    os.system("cls" if os.name == "nt" else "clear")    
for broker_name in list(brokers.values()):
    create_defaults(config_res_folder, broker_name)"""

account_options = [translator.get("account_selection.total_portfolio")]
account_options.extend(list(brokers.values()))
num_operations = 76
account_options_dropdown = str_to_dropdown(account_options)




def main(page: ft.Page):
    #page.views.clear()
    #page.views.append(View("/"))
    page.title = "Portfolio Manager"
    page.padding = 0  # Remove padding so the navbar touches the edges
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    page.adaptive=True
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.window_width = 400
    #page.window_height = 600
    #page.window_resizable = False




    body = ft.Container()#expand=True 





# APP BARS =========================================================================
    home_app_bar = ft.AppBar(
        toolbar_height=70,
        center_title=True,
        title=ft.Container(
            content=ft.Dropdown(
                width=365,
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
                
                options=account_options_dropdown, 
                value=translator.get("account_selection.total_portfolio"),
            ),
            padding=10,
            margin=ft.margin.only(top=15, left=20, right=20)
        ),
    )
    operations_app_bar = ft.AppBar(
        toolbar_height=70,
        center_title=True,
        title=ft.Container(
            content=ft.Text(translator.get("navigation.operations_title"), size=25),
            padding=10,
            margin=ft.margin.only(top=10, left=20, right=20)
        ),
    )
    analysis_app_bar = ft.AppBar(
        toolbar_height=70,
        center_title=True,
        title=ft.Container(
            content=ft.Text(translator.get("navigation.analysis_title"), size=25),
            padding=10,
            margin=ft.margin.only(top=10, left=20, right=20)
        ),
    )
    settings_app_bar = ft.AppBar(
        toolbar_height=70,
        center_title=True,
        title=ft.Container(
            content=ft.Text(translator.get("navigation.settings_title"), size=25),
            padding=10,
            margin=ft.margin.only(top=10, left=20, right=20)
        ),
    )

        

# MIDDLE - Page layout ==================================================================
    page_layout = ft.SafeArea(
        ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls=[
                body,
            ],
        )
    )


# BOTTOM - Navigation Bar =========================================================================
    def nav_change(e):
        index = e.control.selected_index
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/operations")
        elif index == 2:
            page.go("/analysis")
        elif index == 3:
            page.go("/settings")

    nav_bar = ft.NavigationBar(
        selected_index=0,
        on_change=nav_change,
        destinations=[
            AdaptiveNavigationBarDestination(
                ios_icon=ft.CupertinoIcons.HOME, android_icon=ft.Icons.HOME_OUTLINED, 
                ios_selected=ft.CupertinoIcons.HOME, android_selected=ft.Icons.HOME, 
                label="Home"
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.Icons.POST_ADD, android_icon=ft.Icons.POST_ADD, 
                ios_selected=ft.Icons.POST_ADD, android_selected=ft.Icons.POST_ADD, 
                label=translator.get("navigation.operations_tab")
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.CupertinoIcons.GRAPH_SQUARE, android_icon=ft.Icons.AUTO_GRAPH_OUTLINED, 
                ios_selected=ft.CupertinoIcons.GRAPH_SQUARE, android_selected=ft.Icons.AUTO_GRAPH,
                label=translator.get("navigation.analysis_tab")
            ),
            AdaptiveNavigationBarDestination(
                ios_icon=ft.CupertinoIcons.SETTINGS, android_icon=ft.Icons.SETTINGS_OUTLINED, 
                ios_selected=ft.CupertinoIcons.SETTINGS_SOLID, android_selected=ft.Icons.SETTINGS,
                label=translator.get("navigation.settings_tab")
            )
        ],
    )
    

# Initialize =======================================================================================

    def route_change(e: ft.RouteChangeEvent):
        route = e.route
        if route == "/" or route == "":
            body.content = HomeView(page, account_options, num_operations)
            nav_bar.selected_index = 0
            page.appbar = home_app_bar
        elif route == "/operations":
            body.content = OperationsView(page, account_options, num_operations)
            nav_bar.selected_index = 1
            page.appbar = operations_app_bar
        elif route == "/analysis":
            body.content = AnalysisView(page, account_options, num_operations)
            nav_bar.selected_index = 2
            page.appbar = analysis_app_bar
        elif route == "/settings":
            body.content = SettingsView(page, account_options, num_operations)
            nav_bar.selected_index = 3
            page.appbar = settings_app_bar

        page.update()
        

    page.on_route_change = route_change
    page.add(home_app_bar)
    page.add(page_layout)
    page.add(nav_bar)
    page.go("/")

ft.app(target=main)