import time

from app_moneytracker.testCase.baseTestCase import BaseTestCase
from app_moneytracker.Data import TestData
from app_moneytracker.pages.mainPage import MainPage

class AccountTestCase(BaseTestCase):
    """Conjunto de testes para a funcionalidade de Contas (Accounts)."""

    def test_cadastrar_conta_sucesso(self):
        """Corresponde ao TC-ACC-01: cadastrar uma conta com sucesso."""
        print("\n--- Iniciando TC-ACC-01: Cadastrar conta com sucesso ---")
        main_page = MainPage(self.driver)
        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()
        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(TestData.NOME_CONTA)
        add_account_page.preencher_valor_inicial(TestData.VALOR_CONTA)

        account_page_final = add_account_page.clicar_salvar_criacao()

        self._take_screenshot()

        self.assertTrue(account_page_final.verificar_se_conta_existe(TestData.NOME_CONTA),
                        f"A conta '{TestData.NOME_CONTA}' não foi encontrada na lista após o cadastro.")
        print("--- TC-ACC-01 Concluído com Sucesso ---")

    def test_cadastrar_conta_sem_nome(self):
        """Corresponde ao TC-ACC-02: tentar cadastrar conta sem nome."""
        print("\n--- Iniciando TC-ACC-02: Cadastrar conta sem nome ---")

        main_page = MainPage(self.driver)
        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()
        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_valor_inicial(TestData.VALOR_CONTA)
        add_account_page.clicar_salvar_criacao()

        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida)

        print("--- TC-ACC-02 Concluído com Sucesso! ---")

    def test_cadastrar_conta_sem_valor_inicial(self):
        """Corresponde ao TC-ACC-03: tentar cadastrar conta sem valor inicial."""
        print("\n--- Iniciando TC-ACC-03: Cadastrar conta sem valor inicial ---")

        main_page = MainPage(self.driver)
        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()
        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta("Conta Sem Valor")
        add_account_page.clicar_salvar_criacao()

        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida)

        print("--- TC-ACC-03 Concluído com Sucesso! ---")

    def test_cadastrar_conta_valor_zero(self):
        """Corresponde ao TC-ACC-04: Tentar adicionar conta com campo valor = 0."""
        print("\n--- Iniciando TC-ACC-04: Cadastrar conta com valor zero ---")

        main_page = MainPage(self.driver)
        nome_da_conta = "Conta com Saldo Zero"
        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()
        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(nome_da_conta)
        add_account_page.preencher_valor_inicial("0")

        account_page_final = add_account_page.clicar_salvar_criacao()

        self._take_screenshot()

        self.assertTrue(account_page_final.verificar_se_conta_existe(nome_da_conta))
        saldo_obtido = account_page_final.obter_saldo_da_conta(nome_da_conta)

        #self.assertEqual("--", saldo_obtido.strip())

        print(f"--- TC-ACC-04 Concluído com Sucesso! ---")

    def test_editar_conta_sucesso(self):
        """Corresponde ao TC-ACC-05: Editar uma conta cadastrada."""
        print("\n--- Iniciando TC-ACC-05: Editar conta com sucesso ---")

        main_page = MainPage(self.driver)
        print("Setup: Criando conta inicial para ser editada...")

        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(TestData.NOME_CONTA_PARA_EDITAR)
        add_account_page.preencher_valor_inicial("100")
        account_page = add_account_page.clicar_salvar_criacao()

        edit_account_page = account_page.selecionar_conta_por_nome(TestData.NOME_CONTA_PARA_EDITAR)
        edit_account_page.preencher_nome_conta(TestData.NOME_CONTA_EDITADO)
        final_account_page = edit_account_page.clicar_salvar_edicao()

        self._take_screenshot()

        self.assertTrue(final_account_page.verificar_se_conta_existe(TestData.NOME_CONTA_EDITADO))

        self.assertFalse(final_account_page.verificar_se_conta_existe(TestData.NOME_CONTA_PARA_EDITAR))

        print(f"--- TC-ACC-05 Concluído com Sucesso! ---")

    def test_remover_conta_sucesso(self):
        """Corresponde ao TC-ACC-06: remover uma conta cadastrada."""
        print("\n--- Iniciando TC-ACC-06: Remover conta com sucesso ---")

        main_page = MainPage(self.driver)
        print("Setup: Criando conta para ser removida...")

        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(TestData.NOME_CONTA_PARA_REMOVER)
        add_account_page.preencher_valor_inicial("50")
        account_page = add_account_page.clicar_salvar_criacao()

        edit_account_page = account_page.selecionar_conta_por_nome(TestData.NOME_CONTA_PARA_REMOVER)

        self._take_screenshot()

        final_account_page = edit_account_page.clicar_remover().confirmar_remocao()

        self._take_screenshot()

        time.sleep(2)

        self.assertFalse(final_account_page.verificar_se_conta_existe(TestData.NOME_CONTA_PARA_REMOVER))

        print(f"--- TC-ACC-06 Concluído com Sucesso! ---")

    def test_cadastrar_conta_nome_longo(self):
        """Corresponde ao TC-ACC-07: Prova que o app permite cadastrar conta com nome > 20 caracteres."""
        print("\n--- Iniciando TC-ACC-07: Cadastrar conta com nome longo ---")

        main_page = MainPage(self.driver)

        account_page = main_page.fechar_dialogo_inicial_se_existir().navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(TestData.NOME_CONTA_LONGO)
        add_account_page.preencher_valor_inicial("50")
        add_account_page.clicar_salvar_criacao()

        print("Aguardando mensagem de erro para nome longo...")

        time.sleep(1)

        self._take_screenshot()

        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()

        self.assertEqual(TestData.MSG_ERRO_NOME_LONGO, mensagem_erro_obtida,
                         "A mensagem de erro para nome de conta longo não corresponde ao esperado.")

        print("--- TC-ACC-07 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_cadastrar_conta_valor_longo(self):
        """Corresponde ao TC-ACC-08: Tentar cadastrar uma conta com valor > 13 caracteres."""
        print("\n--- Iniciando TC-ACC-08: Cadastrar conta com valor longo ---")

        main_page = MainPage(self.driver)

        account_page = main_page.fechar_dialogo_inicial_se_existir() \
            .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()

        add_account_page.preencher_nome_conta("Conta com Valor Longo")
        add_account_page.preencher_valor_inicial(TestData.VALOR_CONTA_LONGO)
        add_account_page.clicar_salvar_criacao()

        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()
        time.sleep(1)

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_VALOR_LONGO, mensagem_erro_obtida,
                         "A mensagem de erro para valor de conta longo não corresponde ao esperado.")

        print(f"--- TC-ACC-08 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
              f"exibida como esperado. ---")

    def test_cadastrar_conta_campos_vazios(self):
        """Corresponde ao TC-ACC-09: Tentar cadastrar uma conta com todos os campos vazios."""
        print("\n--- Iniciando TC-ACC-09: Cadastrar conta com campos vazios ---")

        main_page = MainPage(self.driver)

        account_page = main_page.fechar_dialogo_inicial_se_existir() \
            .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()

        add_account_page.clicar_salvar_criacao()

        mensagem_erro_nome = add_account_page.obter_mensagem_erro_nome()
        mensagem_erro_valor = add_account_page.obter_mensagem_erro_valor()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_nome,
                         "A mensagem de erro para o campo NOME não corresponde ao esperado.")

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_valor,
                         "A mensagem de erro para o campo VALOR não corresponde ao esperado.")

        print(f"--- TC-ACC-09 Concluído com Sucesso! Mensagens de erro exibidas "
              f"corretamente para ambos os campos. ---")
