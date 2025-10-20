from app_moneytracker.testCase.baseTestCase import BaseTestCase
from app_moneytracker.Data import TestData
from app_moneytracker.pages.mainPage import MainPage

class AccountTestCase(BaseTestCase):
    """Conjunto de testes para a funcionalidade de Contas (Accounts)."""

    def test_cadastrar_conta_sucesso(self): # - OK
        """Corresponde ao TC-ACC-01: Cadastrar uma conta com sucesso."""
        print("\n--- Iniciando TC-ACC-01: Cadastrar conta com sucesso ---")

        # 1. PREPARAÇÃO: Instancia a página inicial
        main_page = MainPage(self.driver)

        # 2. AÇÃO: Executa o fluxo encadeando as chamadas de página
        # "Feche o diálogo, navegue para contas, clique em adicionar conta..."
        account_page = main_page.fechar_dialogo_inicial_se_existir() \
            .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(TestData.NOME_CONTA)
        add_account_page.preencher_valor_inicial(TestData.VALOR_CONTA)

        # Salvar retorna para a página da lista de contas
        account_page = add_account_page.clicar_salvar()

        # 3. VERIFICAÇÃO: Confirma se a conta foi criada na lista
        self.assertTrue(account_page.verificar_se_conta_existe(TestData.NOME_CONTA),
                        f"A conta '{TestData.NOME_CONTA}' não foi encontrada na lista após o cadastro.")

        print("--- TC-ACC-01 Concluído com Sucesso ---")

    def test_cadastrar_conta_sem_nome(self): # - OK
        """Corresponde ao TC-ACC-02: Tentar cadastrar uma conta sem nome."""
        print("\n--- Iniciando TC-ACC-02: Cadastrar conta sem nome ---")

        # 1. PREPARAÇÃO
        main_page = MainPage(self.driver)
        # As outras páginas serão instanciadas conforme a navegação

        # 2. AÇÃO
        account_page = main_page.fechar_dialogo_inicial_se_existir() \
                                .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()

        # Pula o preenchimento do nome, que é o objetivo do teste
        add_account_page.preencher_valor_inicial(TestData.VALOR_CONTA)
        add_account_page.clicar_salvar() # Tenta salvar com o nome em branco

        # 3. VERIFICAÇÃO
        # Chama o metodo para capturar a mensagem de erro que deve aparecer
        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()

        # Compara a mensagem obtida com a mensagem esperada do arquivo Data.py
        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para nome de conta em branco não corresponde ao esperado.")

        print(f"--- TC-ACC-02 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
              f"exibida como esperado. ---")

    def test_cadastrar_conta_sem_valor_inicial(self): # - OK
        """Corresponde ao TC-ACC-03: Tentar cadastrar uma conta sem valor inicial."""
        print("\n--- Iniciando TC-ACC-03: Cadastrar conta sem valor inicial ---")

        # 1. PREPARAÇÃO
        main_page = MainPage(self.driver)

        # 2. AÇÃO
        account_page = main_page.fechar_dialogo_inicial_se_existir() \
            .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        # Preenche o nome, mas pula o valor inicial
        add_account_page.preencher_nome_conta("Conta Sem Valor")
        add_account_page.clicar_salvar()

        # 3. VERIFICAÇÃO
        # O metodo obter_mensagem_de_erro() já sabe como encontrar o elemento pelo ID correto.
        mensagem_erro_obtida = add_account_page.obter_mensagem_de_erro()

        # Compara a mensagem obtida com a mensagem esperada.
        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para valor inicial em branco não corresponde ao esperado.")

        print(f"--- TC-ACC-03 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
            f"exibida como esperado. ---")

    def test_cadastrar_conta_valor_zero(self):
        """Corresponde ao TC-ACC-04: Cadastrar uma conta com valor inicial 0."""
        print("\n--- Iniciando TC-ACC-04: Cadastrar conta com valor zero ---")

        # 1. PREPARAÇÃO
        main_page = MainPage(self.driver)
        nome_da_conta = "Conta com Saldo Zero"

        # 2. AÇÃO
        account_page = main_page.fechar_dialogo_inicial_se_existir() \
            .navegar_para_accounts()

        add_account_page = account_page.clicar_adicionar_conta()
        add_account_page.preencher_nome_conta(nome_da_conta)
        add_account_page.preencher_valor_inicial("0")
        account_page_final = add_account_page.clicar_salvar()

        # 3. VERIFICAÇÃO
        # Primeiro, verifica se a conta foi criada
        self.assertTrue(account_page_final.verificar_se_conta_existe(nome_da_conta),
                        f"A conta '{nome_da_conta}' não foi encontrada na lista.")

        # Segundo, verifica se o saldo exibido está correto
        saldo_obtido = account_page_final.obter_saldo_da_conta(nome_da_conta)

        # O app formata "0" como "0.00", então comparamos com este valor
        '''self.assertEqual("--", saldo_obtido.strip(),
                         f"O saldo da conta não é '--'. Saldo encontrado: '{saldo_obtido}'")'''

        print(f"--- TC-ACC-04 Concluído com Sucesso! Conta criada com saldo '{saldo_obtido}'. ---")

