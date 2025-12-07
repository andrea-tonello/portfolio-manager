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

# Get the absolute path of the current script file
cw_dir = os.path.abspath(__file__)
script_dir = os.path.dirname(cw_dir)
config_folder = os.path.join(script_dir, "config")

config_res_folder = os.path.join(config_folder, "resources")
os.makedirs(config_res_folder, exist_ok=True)

config_path = os.path.join(config_folder, "config.ini")
config = configparser.ConfigParser()


translator = Translator(language_code="it")
lang_code = None
if os.path.exists(config_path):
    config.read(config_path)
    if 'Language' in config and 'Code' in config['Language']:
        lang_code = config['Language']['Code']
translator.load_language(lang_code)


brokers = {}
# Try to load brokers from config

if os.path.exists(config_path) and 'Brokers' in config:
    try:
        # Convert keys to int (configparser reads keys as strings)
        brokers = {int(k): v for k, v in config.items('Brokers')}
    except ValueError:
        pass

account_options = [translator.get("account_selection.total_portfolio")]
account_options.extend(list(brokers.values()))
num_operations = 76
account_options_dropdown = str_to_dropdown(account_options)




def main(page: ft.Page):
    page.title = "Portfolio Manager"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.theme = ft.Theme(color_scheme_seed=ft.Colors.BLUE)
    page.adaptive = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    # --- CHANGED: Use AnimatedSwitcher with scrollable content ---
    body = ft.AnimatedSwitcher(
        content=ft.Container(),
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=400,
        switch_in_curve=ft.AnimationCurve.FAST_LINEAR_TO_SLOW_EASE_IN,
        expand=True,  # Allow it to fill available space
    )


    # APP BARS =========================================================================
    home_app_bar = ft.AppBar(
        toolbar_height=100,
        bgcolor=ft.Colors.SURFACE,
        center_title=True,
        title=ft.Container(
            content=ft.Dropdown(
                width=310,
                text_size=19,
                filled=True,
                fill_color=ft.Colors.ON_INVERSE_SURFACE,
                border_color=ft.Colors.SECONDARY,
                focused_border_color=ft.Colors.INVERSE_PRIMARY,
                border_width=3,
                focused_border_width=8,
                border_radius=ft.border_radius.all(15),
                trailing_icon=ft.Icons.KEYBOARD_ARROW_DOWN,
                selected_trailing_icon=ft.Icons.KEYBOARD_ARROW_UP,
                
                options=account_options_dropdown, 
                value=translator.get("account_selection.select_prompt"),
            ),
            padding=10,
            margin=ft.margin.only(top=15, left=20, right=20)
        ),
    )
        
    operations_app_bar = TitleAppbar(translator.get("navigation.operations_title"), text_size=25)
    analysis_app_bar = TitleAppbar(translator.get("navigation.analysis_title"), text_size=25)
    settings_app_bar = TitleAppbar(translator.get("navigation.settings_title"), text_size=25)

        
    # MIDDLE - Page layout with scrolling ==================================================================
    page_layout = ft.Column(
        controls=[
            body,
        ],
        expand=True,
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
                ios_icon=ft.CupertinoIcons.GRAPH_SQUARE, android_icon=ft.Icons.DATA_THRESHOLDING_OUTLINED, 
                ios_selected=ft.CupertinoIcons.GRAPH_SQUARE, android_selected=ft.Icons.DATA_THRESHOLDING,
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
            body.content = HomeView(page, account_options, num_operations, key="home")
            nav_bar.selected_index = 0
            page.appbar = home_app_bar
        elif route == "/operations":
            body.content = OperationsView(page, account_options_dropdown, num_operations, key="operations")
            nav_bar.selected_index = 1
            page.appbar = operations_app_bar
        elif route == "/analysis":
            body.content = AnalysisView(page, account_options_dropdown, num_operations, key="analysis")
            nav_bar.selected_index = 2
            page.appbar = analysis_app_bar
        elif route == "/settings":
            body.content = SettingsView(page, account_options, num_operations, key="settings")
            nav_bar.selected_index = 3
            page.appbar = settings_app_bar

        page.update()
        

    page.on_route_change = route_change
    page.add(home_app_bar)
    page.add(page_layout)
    page.add(nav_bar)
    page.go("/")

ft.app(target=main)