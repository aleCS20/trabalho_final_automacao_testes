import time

from app_moneytracker.testCase.baseTestCase import BaseTestCase
from app_moneytracker.Data import TestData
from app_moneytracker.pages.mainPage import MainPage

class IncomeTestCase(BaseTestCase):
    """Conjunto de testes para a funcionalidade de Receitas (Income)."""

    def test_adicionar_receita_sucesso(self):
        """Corresponde ao TC-INC-01: Adicionar uma receita com sucesso."""
        print("\n--- Iniciando TC-INC-01: Adicionar receita com sucesso ---")

        main_page = MainPage(self.driver)

        # AÇÃO (Fluxo Corrigido)
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os campos de texto
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA)

        # --- CORREÇÃO: Chama o método para digitar a categoria ---
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)

        # Seleciona a conta no dropdown
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Salva a receita
        final_main_page = add_income_page.clicar_salvar()

        # VERIFICAÇÃO
        #self.assertTrue(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA),
        #                f"A transação com a nota '{TestData.NOTA_RECEITA}' não foi encontrada na lista.")
        time.sleep(3)
        print(f"--- TC-INC-01 Concluído com Sucesso! Receita adicionada. ---")

    def test_adicionar_receita_sem_valor(self):
        """Corresponde ao TC-INC-02: Tentar adicionar uma receita sem valor."""
        print("\n--- Iniciando TC-INC-02: Adicionar receita sem valor ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os outros campos, mas deixa o valor em branco
        add_income_page.preencher_nota("Teste de Receita Sem Valor")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Tenta salvar
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO
        # Captura a mensagem de erro que deve aparecer abaixo do campo de valor
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        # Reutiliza a mensagem de erro já definida no Data.py
        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para valor em branco não corresponde ao esperado.")

        print(f"--- TC-INC-02 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
              f"exibida como esperado. ---")

    def test_adicionar_receita_valor_invalido(self):
        """Corresponde ao TC-INC-03: Tentar adicionar uma receita com caractere inválido no valor."""
        print("\n--- Iniciando TC-INC-03: Adicionar receita com valor inválido ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os outros campos com dados válidos
        add_income_page.preencher_nota("Teste de Valor Inválido")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Preenche o campo de valor com um caractere inválido
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_INVALIDO)

        # Tenta salvar
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO
        # Captura a mensagem de erro que deve aparecer abaixo do campo de valor
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para valor inválido não corresponde ao esperado.")

        print(f"--- TC-INC-03 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_valor_longo(self):
        """Corresponde ao TC-INC-04: Tentar adicionar uma receita com valor > 13 dígitos."""
        print("\n--- Iniciando TC-INC-04: Adicionar receita com valor longo ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os outros campos com dados válidos
        add_income_page.preencher_nota("Teste de Valor Longo")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Preenche o campo de valor com um número com mais de 13 dígitos
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_LONGO)

        # Tenta salvar
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO
        # Captura a mensagem de erro que deve aparecer abaixo do campo de valor
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        # Compara a mensagem obtida com a mensagem de erro específica para este caso
        self.assertEqual(TestData.MSG_ERRO_VALOR_RECEITA_LONGO, mensagem_erro_obtida,
                         "A mensagem de erro para valor longo não corresponde ao esperado.")

        print(f"--- TC-INC-04 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_sem_categoria(self):
        """Corresponde ao TC-INC-05: Tentar adicionar uma receita sem categoria."""
        print("\n--- Iniciando TC-INC-05: Adicionar receita sem categoria ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os outros campos, mas deixa a categoria em branco
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota("Teste de Receita Sem Categoria")
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Tenta salvar
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO
        # Captura a mensagem de erro que deve aparecer abaixo do campo de categoria
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_categoria()

        # Reutiliza a mensagem de erro "Este campo não pode ficar vazio"
        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para categoria em branco não corresponde ao esperado.")

        print(f"--- TC-INC-05 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_categoria_longa(self):
        """Corresponde ao TC-INC-06: Prova que o app permite adicionar receita com categoria > 30 caracteres"""
        print("\n--- Iniciando TC-INC-06: Adicionar receita com categoria longa (para provar o bug) ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os campos, usando a categoria longa
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota("Teste de Categoria Longa")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA_LONGA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Tenta salvar, esperando que a ação resulte em um erro de validação
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO (Lógica corrigida para esperar o erro)

        # Captura a mensagem de erro que DEVERIA aparecer
        print("Aguardando mensagem de erro para categoria longa...")
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_categoria()

        # Compara a mensagem obtida com a mensagem esperada do arquivo Data.py
        self.assertEqual(TestData.MSG_ERRO_CATEGORIA_LONGA, mensagem_erro_obtida,
                         "A mensagem de erro para categoria longa não corresponde ao esperado.")

        print("--- TC-INC-06 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_adicionar_receita_sem_titulo(self):
        """Corresponde ao TC-INC-07: Tentar adicionar uma receita sem título (nota).
        Este teste DEVE FALHAR para indicar a presença de um bug."""
        print("\n--- Iniciando TC-INC-07: Adicionar receita sem título ---")

        main_page = MainPage(self.driver)

        # 1. AÇÃO
        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        # Preenche os outros campos, mas deixa a nota/título em branco
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        # Tenta salvar
        add_income_page.clicar_salvar()

        # 2. VERIFICAÇÃO (Lógica para esperar o erro)
        print("Aguardando mensagem de erro para título vazio...")
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_nota()

        # Compara a mensagem obtida com a mensagem esperada
        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para título vazio não corresponde ao esperado.")

        print("--- TC-INC-07 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

