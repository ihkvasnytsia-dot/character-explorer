from tkinter import ttk

from views.search_view import SearchView
from views.table_view import TableView


class CatalogView(ttk.Frame):
    def __init__(self, parent, app_controller):
        super().__init__(parent)

        self.app_controller = app_controller
        self.translations = self.app_controller.get_translations()

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        self.title = ttk.Label(
            self,
            text=self.translations["catalog_title"],
            font=("Arial", 18)
        )

        self.title.pack(pady=10)
        
        # # Верхня частина — пошук
        self.search_view = SearchView(
            self, self.app_controller
        )

        self.search_view.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # # Нижня частина — таблиця
        self.table_view = TableView(
            self, self.app_controller
        )

        self.table_view.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

        self.search_view.set_update_callback(
            self.table_view.update_data
        )

    def update_language(self, translations):

        self.translations = translations
        # Оновити власний заголовок
        self.title.config(
            text=translations["catalog_title"]
        )
        
        self.search_view.update_language(translations)
        self.table_view.update_language(translations)
