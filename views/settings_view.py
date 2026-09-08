from tkinter import ttk


class SettingsView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.translations = self.controller.get_translations()

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations["settings_title"],
            font=("Arial", 18)
        )

        self.title.pack(
            pady=10
        )

        # Мова
        self.language_label = ttk.Label(
            self,
            text=self.translations["language_label"]
        )

        self.language_label.pack(
            anchor="w",
            padx=20,
            pady=(10, 5)
        )

        self.language_combobox = ttk.Combobox(
            self,
            state="readonly"
        )

        self.language_combobox.pack(
            anchor="w",
            padx=20
        )

        self.update_language_combobox()


    def set_language_change_callback(self, callback):
        self.language_callback = callback

        self.language_combobox.bind(
            "<<ComboboxSelected>>",
            self.on_language_change
        )


    def on_language_change(self, event=None):
        selected_name = self.language_combobox.get()

        for code, name in self.languages.items():
            if name == selected_name:
                self.language_callback(code)
                break


    def update_language(self, translations):
        self.translations = translations
        # Оновити власний заголовок
        self.title.config(
            text=self.translations["settings_title"]
        )

        # Оновити мітку мови
        self.language_label.config(
            text=self.translations["language_label"]
        )

        # Оновити значення комбобоксу мови
        self.update_language_combobox()


    def update_language_combobox(self):
    
            self.languages = {
                "en": self.translations["english"],
                "uk": self.translations["ukrainian"]
            }
    
            sorted_languages = sorted(
                self.languages.items(),
                key=lambda item: item[1]
            )
    
            self.language_combobox.config(
                values=[name for code, name in sorted_languages]
            )

            current_language = self.controller.get_current_language()
    
            for index, (code, name) in enumerate(sorted_languages):
                if code == current_language:
                    self.language_combobox.current(index)
                    break