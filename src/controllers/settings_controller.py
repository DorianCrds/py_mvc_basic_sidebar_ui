import json


class SettingsController:
    @staticmethod
    def load_settings_json():
        with open("./config/settings.json", "r") as file:
            return json.load(file)

    @staticmethod
    def load_theme_json() -> dict[str]:
        with open("./src/views/style/themes.json", "r") as file:
            return json.load(file)

    def get_all_themes_names(self) -> list[str]:
        themes_list = []
        for key, items in self.load_theme_json().items():
            themes_list.append(key)
        return themes_list

    def load_style_sheet_for_theme(self, empty_stylesheet: str) -> str:
        theme = self.load_theme_json()[self.get_current_theme_name()]

        new_style_sheet = empty_stylesheet

        for key, color in theme.items():
            new_style_sheet = new_style_sheet.replace(f"{{{key}}}", color)

        return new_style_sheet

    def set_new_theme(self, theme_name):
        settings = self.load_settings_json()
        settings["theme"] = theme_name

        with open("./config/settings.json", "w") as file:
            json.dump(settings, file, indent=4)

    def get_current_theme_name(self) -> str:
        return self.load_settings_json()["theme"]
