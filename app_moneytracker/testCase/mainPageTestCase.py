from app_moneytracker.pages.mainPage import MainPage
from app_moneytracker.testCase.baseTestCase import BaseTestCase

class MainPageTestCase(BaseTestCase):

    def test_open_app_and_close_initial_dialog(self):
        print("\n ----- Iniciando o teste da tela inicial e caixa de dialogo ------ ")

        main_page = MainPage(self.driver)
        main_page.fechar_dialogo_inicial_se_existir()

        self.assertTrue(main_page.verificar_se_tela_principal_carregou(),
                        "A tela principal não foi carregada após fechar o diálogo inicial")

        print("--- Teste de abertura concluído com sucesso! ---")
