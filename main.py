from controllers.app_controller import AppController
from models.ascii_data import ASCIIData
from services.character_search_service import CharacterSearchService
from services.localization_service import LocalizationService
from views.main_view import MainView


def main():

    data = ASCIIData()
    search_engine = CharacterSearchService(data)
    localization_service = LocalizationService()
    app_controller = AppController(search_engine, data, localization_service)
    
    MainView(app_controller).run()   


if __name__ == "__main__":
    main()