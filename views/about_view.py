from tkinter import ttk


class AboutView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.translations = self.controller.get_translations()
        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations["about"],
            font=("Arial", 18)
        )

        self.title.pack(
            pady=10
        )

        # Опис
        self.description = ttk.Label(
            self,
            text=self.translations["about_description"],
            justify="left",
            anchor="w"
        )

        self.description.pack(
            fill="x",
            padx=30,
            pady=20
        )

        self.bind(
            "<Configure>",
            lambda event: self.description.configure(
                wraplength=max(1, event.width - 60)
            )
        )

    def update_language(self, translations):
        self.translations = translations
        self.title.config(
            text=self.translations["about"]
        )
        
        self.description.config(
            text=self.translations["about_description"]
        )

