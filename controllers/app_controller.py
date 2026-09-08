class AppController:
    def __init__(self, search_service , data, localization_service):
        self.search_engine = search_service
        self.model = data
        self.localization_service = localization_service

    def search(self, entry, search_type):
    
        search_methods = {
            0: self.search_engine.by_symbol,
            1: self.search_engine.by_decimal,
            2: self.search_engine.by_hexadecimal,
            3: self.search_engine.by_binary,
            4: self.search_engine.by_octal,
            5: self.search_engine.by_unicode,
            6: self.search_engine.by_name
        }

        method = search_methods.get(search_type)

        if method:
            return method(entry)

        return []


    def get_all_characters(self):
        return self.model.characters


    def change_language(self, language):
        if not self.localization_service.change_language(language):
            return None

        return self.localization_service.get_all()


    def get_translations(self):
        return self.localization_service.get_all()


    def get_current_language(self):
        return self.localization_service.get_current_language()