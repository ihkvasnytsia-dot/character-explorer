from tkinter import ttk


class SearchView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller
        self.translations = self.controller.get_translations()

        self.search_types = [
            "symbol",
            "decimal",
            "hexadecimal",
            "binary",
            "octal",
            "unicode",
            "name"
        ]

        self.create_widgets()


    def create_widgets(self):
        search_frame = ttk.Frame(self)
        search_frame.pack(pady=10)

        self.search_label = ttk.Label(
            search_frame,
            text=self.translations["search_by"]
        )

        self.search_label.grid(
            row=0,
            column=0,
            padx=5
        )

        self.search_type = ttk.Combobox(
            search_frame,
            values=self.get_search_type_names(),
            state="readonly"
        )

        self.search_type.grid(
            row=0,
            column=1,
            padx=5
        )

        self.search_type.current(0)

        self.search_entry = ttk.Entry(
            search_frame,
            width=30
        )

        self.search_entry.grid(
            row=0,
            column=2,
            padx=5
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_event
        )


    def set_update_callback(self, method):
        self.update_table = method


    def search_event(self, event=None):
        results = self.controller.search(
            self.search_entry.get(), 
            self.search_type.current()
        )

        self.update_table(results)


    def get_search_type_names(self):
        return [
            self.translations[search_type]
            for search_type in self.search_types
        ]


    def update_language(self, translations):

        self.translations = translations
        
        self.search_label.config(
            text=translations["search_by"]
        )

        current_index = self.search_type.current()

        self.search_type.config(
            values=self.get_search_type_names()
        )

        self.search_type.current(current_index)


    


    


    