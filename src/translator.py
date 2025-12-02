import json
import os
import sys

class Translator:
    def __init__(self, language_code="en"):
        self.language_code = language_code
        self.strings = {}
        # Determine base path: sys._MEIPASS if frozen (PyInstaller), else current dir
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.getcwd()
        self.locales_dir = os.path.join(base_path, "locales")
        self.load_language(language_code)

    def load_language(self, language_code):
        self.language_code = language_code
        path = os.path.join(self.locales_dir, f"{language_code}.json")
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                self.strings = json.load(f)
        except FileNotFoundError:
            self.strings = {} 
            print(f"FATAL ERROR: Language file '{path}' not found.")

    def get(self, key, **kwargs):
        """
        Gets a translated string by its key, using dot-notation for nesting.
        Example: translator.get("main_menu.options.exit")
        """
        try:
            # Split the key by '.' to navigate the nested dictionary
            keys = key.split('.')
            
            # Start at the top level of the strings dictionary
            value = self.strings
            
            # Loop through each part of the key to "walk" down
            for k in keys:
                value = value[k] # This will raise KeyError if a key is missing
            
            # 'value' is now the final string template
            template = value

            # Return the formatted string, or just the template if no kwargs
            return template.format(**kwargs)
            
        except (KeyError, TypeError, AttributeError):
            # KeyError: A key in the path (e.g., 'main_menu.bad_key') was not found.
            # TypeError: The final 'value' was another dictionary, not a string.
            # AttributeError: A value in the middle was not a dictionary.
            
            # Fallback: return the key itself so the user knows what's missing
            print(f"Warning: Translation key '{key}' not found in '{self.language_code}.json'.")
            return f"<{key}>"