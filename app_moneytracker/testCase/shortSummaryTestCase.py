from app_moneytracker.testCase.baseTestCase import BaseTestCase
from app_moneytracker.pages.mainPage import MainPage
from app_moneytracker.Data import TestData


class ShortSummaryTestCase(BaseTestCase):
    """Conjunto de testes para a funcionalidade de Short Summary."""

    def test_visualizar_short_summary_com_dados(self):
        """Corresponde ao TC-INC-18: Cadastra uma receita e visualiza os dados no "Short Summary"."""
        print("\n--- Iniciando TC-INC-18: Visualizar Short Summary com dados ---")

        main_page = MainPage(self.driver)

        print("Setup: Criando uma receita para o teste...")

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA_RESUMO)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        main_page_after_creation = add_income_page.clicar_salvar()

        short_summary_page = main_page_after_creation.clicar_short_summary()



        self.assertTrue(short_summary_page.verificar_se_tela_carregou(),
                        "A tela 'Short Summary' não foi carregada após o clique.")

        self.assertTrue(short_summary_page.verificar_se_categoria_existe_no_resumo(TestData.CATEGORIA_RECEITA_RESUMO),
                        "A categoria da receita não foi encontrada na lista do resumo.")

        self._take_screenshot()

        print(f"--- TC-INC-18 Concluído com Sucesso! Resumo verificado e categoria encontrada. ---")