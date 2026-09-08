import tkinter as tk
from tkinter import ttk
from views.about_view import AboutView
from views.catalog_view import CatalogView
from views.settings_view import SettingsView


class MainView:
    def __init__(self, app_controller):
        
        self.app_controller = app_controller

        # Отримуємо локалізацію через Controller
        self.translations = self.app_controller.get_translations()

        self.window = tk.Tk()
        
        self.window.title(self.translations["title"])

        width = 850
        height = 500

        # Розмір екрана
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Координати верхнього лівого кута
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.window.geometry(
            f"{width}x{height}+{x}+{y}"
        )

        self.window.minsize(400, 300)

        self.create_notebook()


    def create_notebook(self):
        self.notebook = ttk.Notebook(self.window)

        self.notebook.pack(
            fill="both",
            expand=True
        )

        # Вкладки
        self.catalog_view = CatalogView(
            self.notebook,
            self.app_controller
        )

        self.settings_view = SettingsView(
            self.notebook,
            self.app_controller
        )

        self.about_view = AboutView(
            self.notebook,
            self.app_controller
        )

        self.settings_view.set_language_change_callback(
            self.change_language
        )

        # Додаємо вкладки
        self.notebook.add(
            self.catalog_view,
            text=self.translations["catalog"]
        )

        self.notebook.add(
            self.settings_view,
            text=self.translations["settings"]
        )

        self.notebook.add(
            self.about_view,
            text=self.translations["about"]
        )


    def change_language(self, language):
        self.translations = self.app_controller.change_language(language)
        self.update_language()

    
    def update_language(self):
        
        # Оновити назви вкладок
        self.notebook.tab(
            self.catalog_view,
            text=self.translations["catalog"]
        )

        self.notebook.tab(
            self.settings_view,
            text=self.translations["settings"]
        )

        self.notebook.tab(
            self.about_view,
            text=self.translations["about"]
        )

        # Оновити вміст View
        self.catalog_view.update_language(self.translations)
        self.settings_view.update_language(self.translations)
        self.about_view.update_language(self.translations)


    def run(self):
        self.window.mainloop()