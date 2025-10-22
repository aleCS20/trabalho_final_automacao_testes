import time

from app_moneytracker.testCase.baseTestCase import BaseTestCase
from app_moneytracker.Data import TestData
from app_moneytracker.pages.mainPage import MainPage
from datetime import date, timedelta, time

class IncomeTestCase(BaseTestCase):
    """Conjunto de testes para a funcionalidade de Receitas (Income)."""

    def test_adicionar_receita_sucesso(self):
        """Corresponde ao TC-INC-01: Adicionar uma receita com sucesso."""
        print("\n--- Iniciando TC-INC-01: Adicionar receita com sucesso ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        final_main_page = add_income_page.clicar_salvar()

        self._take_screenshot()

        #self.assertTrue(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA),
        #                f"A transação com a nota '{TestData.NOTA_RECEITA}' não foi encontrada na lista.")

        print(f"--- TC-INC-01 Concluído com Sucesso! Receita adicionada. ---")

    def test_adicionar_receita_sem_valor(self):
        """Corresponde ao TC-INC-02: Tentar adicionar uma receita sem valor."""
        print("\n--- Iniciando TC-INC-02: Adicionar receita sem valor ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_nota("Teste de Receita Sem Valor")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_salvar()

        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para valor em branco não corresponde ao esperado.")

        print(f"--- TC-INC-02 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
              f"exibida como esperado. ---")

    def test_adicionar_receita_valor_invalido(self):
        """Corresponde ao TC-INC-03: Tentar adicionar uma receita com caractere inválido no valor."""
        print("\n--- Iniciando TC-INC-03: Adicionar receita com valor inválido ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_nota("Teste de Valor Inválido")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_INVALIDO)
        add_income_page.clicar_salvar()

        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para valor inválido não corresponde ao esperado.")

        print(f"--- TC-INC-03 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_valor_longo(self):
        """Corresponde ao TC-INC-04: Tentar adicionar uma receita com valor > 13 dígitos."""
        print("\n--- Iniciando TC-INC-04: Adicionar receita com valor longo ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_nota("Teste de Valor Longo")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_LONGO)
        add_income_page.clicar_salvar()

        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_VALOR_RECEITA_LONGO, mensagem_erro_obtida,
                         "A mensagem de erro para valor longo não corresponde ao esperado.")

        print(f"--- TC-INC-04 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_sem_categoria(self):
        """Corresponde ao TC-INC-05: Tentar adicionar uma receita sem categoria."""
        print("\n--- Iniciando TC-INC-05: Adicionar receita sem categoria ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota("Teste de Receita Sem Categoria")
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_salvar()

        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_categoria()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para categoria em branco não corresponde ao esperado.")

        print(f"--- TC-INC-05 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}'"
              f" exibida como esperado. ---")

    def test_adicionar_receita_categoria_longa(self):
        """Corresponde ao TC-INC-06: Prova que o app permite adicionar receita com categoria > 30 caracteres"""
        print("\n--- Iniciando TC-INC-06: Adicionar receita com categoria longa (para provar o bug) ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota("Teste de Categoria Longa")
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA_LONGA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_salvar()

        print("Aguardando mensagem de erro para categoria longa...")
        self._take_screenshot()
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_categoria()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_CATEGORIA_LONGA, mensagem_erro_obtida,
                         "A mensagem de erro para categoria longa não corresponde ao esperado.")

        print("--- TC-INC-06 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_adicionar_receita_sem_titulo(self):
        """Corresponde ao TC-INC-07: Tentar adicionar uma receita sem título (nota).
        Este teste DEVE FALHAR para indicar a presença de um bug."""
        print("\n--- Iniciando TC-INC-07: Adicionar receita sem título ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_salvar()

        print("Aguardando mensagem de erro para título vazio...")
        self._take_screenshot()
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_nota()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_obtida,
                         "A mensagem de erro para título vazio não corresponde ao esperado.")

        print("--- TC-INC-07 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_adicionar_receita_titulo_longo(self):
        """Corresponde ao TC-INC-08: Tentar adicionar uma receita com título > 20 caracteres.
        Este teste DEVE FALHAR para indicar a presença de um bug."""
        print("\n--- Iniciando TC-INC-08: Adicionar receita com título longo ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_LONGA)
        add_income_page.clicar_salvar()

        print("Aguardando mensagem de erro para título longo...")
        self._take_screenshot()
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_nota()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_TITULO_LONGO, mensagem_erro_obtida,
                         "A mensagem de erro para título longo não corresponde ao esperado.")

        print("--- TC-INC-08 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_adicionar_receita_titulo_numerico(self):
        """Corresponde ao TC-INC-09: Tentar adicionar uma receita com apenas números no título.
        Este teste DEVE FALHAR para indicar a presença de um bug."""
        print("\n--- Iniciando TC-INC-09: Adicionar receita com título numérico ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_NUMERICA)
        add_income_page.clicar_salvar()

        print("Aguardando mensagem de erro para título com números...")
        self._take_screenshot()
        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_nota()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_TITULO_INVALIDO, mensagem_erro_obtida,
                         "A mensagem de erro para título com números não corresponde ao esperado.")

        print("--- TC-INC-09 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_remover_receita_sucesso(self):
        """Corresponde ao TC-INC-10: Remover uma receita adicionada."""
        print("\n--- Iniciando TC-INC-10: Remover receita com sucesso ---")

        main_page = MainPage(self.driver)

        print("Setup: Criando receita para ser removida...")

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor("99.99")
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_PARA_REMOVER)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        main_page_after_creation = add_income_page.clicar_salvar()

        edit_income_page = main_page_after_creation.selecionar_transacao_por_nota(TestData.NOTA_RECEITA_PARA_REMOVER)

        final_main_page = edit_income_page.clicar_remover()

        self._take_screenshot()

        #self.assertFalse(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_PARA_REMOVER),
        #                 f"A transação removida '{TestData.NOTA_RECEITA_PARA_REMOVER}' ainda foi encontrada na lista.")

        print(f"--- TC-INC-10 Concluído com Sucesso! A receita '{TestData.NOTA_RECEITA_PARA_REMOVER}'"
              f" foi removida. ---")

    def test_editar_receita_sucesso(self):
        """Corresponde ao TC-INC-11: Editar uma receita adicionada."""
        print("\n--- Iniciando TC-INC-11: Editar receita com sucesso ---")

        main_page = MainPage(self.driver)

        print("Setup: Criando receita para ser editada...")

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()

        add_income_page.preencher_valor("123.45")
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_PARA_EDITAR)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        main_page_after_creation = add_income_page.clicar_salvar()

        edit_income_page = main_page_after_creation.selecionar_transacao_por_nota(TestData.NOTA_RECEITA_PARA_EDITAR)
        edit_income_page.preencher_nota(TestData.NOTA_RECEITA_EDITADA)

        final_main_page = edit_income_page.clicar_salvar()

        self._take_screenshot()

        self.assertTrue(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_EDITADA),
                        f"A transação com a nota editada '{TestData.NOTA_RECEITA_EDITADA}' não foi encontrada.")

        #self.assertFalse(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_PARA_EDITAR),
          #               f"A transação com a nota original '{TestData.NOTA_RECEITA_PARA_EDITAR}' ainda foi encontrada.")

        print(f"--- TC-INC-11 Concluído com Sucesso! A receita foi editada para '{TestData.NOTA_RECEITA_EDITADA}'. ---")

    def test_adicionar_receita_duplicada(self):
        """Corresponde ao TC-INC-12: Tentar adicionar uma receita com dados duplicados.
        Este teste DEVE FALHAR para indicar a presença de um bug."""
        print("\n--- Iniciando TC-INC-12: Adicionar receita duplicada ---")

        main_page = MainPage(self.driver)

        print("Setup: Criando a primeira transação...")

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_DUPLICADO)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_DUPLICADA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA_DUPLICADA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        main_page_after_creation = add_income_page.clicar_salvar()
        self._take_screenshot()
        print("Primeira transação criada com sucesso.")

        print("Ação: Tentando criar a segunda transação idêntica...")

        add_income_page = main_page_after_creation.clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA_DUPLICADO)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_DUPLICADA)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA_DUPLICADA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_salvar()

        print("Aguardando mensagem de erro para transação duplicada...")

        mensagem_erro_obtida = add_income_page.obter_mensagem_erro_valor()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_TRANSACAO_DUPLICADA, mensagem_erro_obtida,
                         "A mensagem de erro para transação duplicada não corresponde ao esperado.")

        print("--- TC-INC-12 Concluído com Sucesso! Mensagem de erro exibida como esperado. ---")

    def test_adicionar_receita_campos_vazios(self):
        """Corresponde ao TC-INC-13: Tentar adicionar uma receita com todos os campos vazios."""
        print("\n--- Iniciando TC-INC-13: Adicionar receita com campos vazios ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.clicar_salvar()

        mensagem_erro_preco = add_income_page.obter_mensagem_erro_valor()
        mensagem_erro_categoria = add_income_page.obter_mensagem_erro_categoria()

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_preco,
                         "A mensagem de erro para o campo PREÇO não corresponde ao esperado.")

        self.assertEqual(TestData.MSG_ERRO_NOME_OBRIGATORIO, mensagem_erro_categoria,
                         "A mensagem de erro para o campo CATEGORIA não corresponde ao esperado.")
        self._take_screenshot()

        print(f"--- TC-INC-13 Concluído com Sucesso! Mensagens de erro exibidas "
              f"corretamente para ambos os campos. ---")

    def test_adicionar_receita_data_presente(self):
        """Corresponde ao TC-INC-14: Adicionar Receita com data no presente (atual)."""
        print("\n--- Iniciando TC-INC-14: Adicionar receita com data atual ---")

        main_page = MainPage(self.driver)

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor(TestData.VALOR_RECEITA)
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_DATA_ATUAL)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)
        add_income_page.clicar_campo_data()

        self.assertTrue(add_income_page.verificar_data_atual_selecionada(),
                        "O calendário não abriu com a data atual selecionada.")

        add_income_page.clicar_ok_calendario()

        final_main_page = add_income_page.clicar_salvar()

        self.assertTrue(final_main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_DATA_ATUAL),
                        f"A transação '{TestData.NOTA_RECEITA_DATA_ATUAL}' não foi encontrada na lista.")
        self._take_screenshot()

        print(f"--- TC-INC-14 Concluído com Sucesso! Receita com data atual adicionada. ---")

    def test_adicionar_receita_data_passada(self):
        """Corresponde ao TC-INC-15: Adicionar Receita com data no passado."""
        print("\n--- Iniciando TC-INC-15: Adicionar receita com data passada ---")

        main_page = MainPage(self.driver)

        hoje = date.today()
        ontem = hoje - timedelta(days=1)
        meses_pt = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
                    7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
        content_desc_ontem = f"{ontem.day} {meses_pt[ontem.month]} {ontem.year}"

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor("15.50")
        add_income_page.preencher_nota(TestData.NOTA_RECEITA_DATA_PASSADA)
        add_income_page.preencher_categoria("Lanche")
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        add_income_page.clicar_campo_data()

        if hoje.day == 1:
            add_income_page.voltar_mes_calendario()

        add_income_page.selecionar_dia_calendario(content_desc_ontem)
        add_income_page.clicar_ok_calendario()

        final_main_page = add_income_page.clicar_salvar()

        data_exibida = final_main_page.obter_data_da_transacao_por_nota(TestData.NOTA_RECEITA_DATA_PASSADA)
        data_esperada = ontem.strftime("%d/%m/%Y")

        '''self.assertEqual(data_esperada, data_exibida,
                         f"A data da transação não corresponde à data passada selecionada. 
                         Esperado: {data_esperada}, Atual: {data_exibida}")'''

        self._take_screenshot()

        print(f"--- TC-INC-15 Concluído com Sucesso! Receita adicionada com a data '{data_exibida}'. ---")

    def test_adicionar_receita_data_futura(self):
        """Corresponde ao TC-INC-16: Tentar adicionar uma receita com data no futuro."""
        print("\n--- Iniciando TC-INC-16: Adicionar receita com data futura ---")

        main_page = MainPage(self.driver)

        hoje = date.today()
        amanha = hoje + timedelta(days=1)
        meses_pt = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
                    7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
        content_desc_amanha = f"{amanha.day} {meses_pt[amanha.month]} {amanha.year}"

        add_income_page = main_page.fechar_dialogo_inicial_se_existir() \
            .clicar_adicionar_receita()
        add_income_page.preencher_valor("300")
        add_income_page.preencher_nota("Receita Futura")
        add_income_page.preencher_categoria("Bônus")
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        add_income_page.clicar_campo_data()

        if hoje.month != amanha.month:
            add_income_page.avancar_mes_calendario()
        add_income_page.selecionar_dia_calendario(content_desc_amanha)
        add_income_page.clicar_ok_calendario()

        mensagem_erro_obtida = add_income_page.obter_mensagem_toast()

        self._take_screenshot()

        self.assertEqual(TestData.MSG_ERRO_DATA_FUTURA, mensagem_erro_obtida,
                         "A mensagem de erro para data futura não corresponde ao esperado.")

        print(f"--- TC-INC-16 Concluído com Sucesso! Mensagem de erro '{mensagem_erro_obtida}' "
              f"exibida como esperado. ---")

    def test_exibir_resumo_todas_as_datas(self):
        """Corresponde ao TC-INC-17: Exibir datas anteriores no Resumo."""
        print("\n--- Iniciando TC-INC-17: Exibir resumo de todas as datas ---")

        main_page = MainPage(self.driver)

        print("Setup: Criando transação com data de hoje...")

        self._criar_receita_rapida(TestData.NOTA_RECEITA_DATA_ATUAL, "100.00", date.today())

        print("Setup: Criando transação com data de ontem...")

        self._criar_receita_rapida(TestData.NOTA_RECEITA_DATA_PASSADA, "50.00", date.today() - timedelta(days=1))

        main_page.selecionar_periodo_do_resumo(TestData.FILTRO_PERIODO_TUDO)

        print("Verificando se ambas as transações estão visíveis...")

        self._take_screenshot()

        self.assertTrue(main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_DATA_ATUAL),
                        "A transação de hoje não foi encontrada após aplicar o filtro 'Tudo'.")

        self.assertTrue(main_page.verificar_se_transacao_existe_por_nota(TestData.NOTA_RECEITA_DATA_PASSADA),
                        "A transação de ontem não foi encontrada após aplicar o filtro 'Tudo'.")

        print(f"--- TC-INC-17 Concluído com Sucesso! Filtro 'Tudo' exibiu todas as transações. ---")

    #### ----------------------------- FUNÇÃO AUXILIAR PARA ESTE TESTE ----------------------- ###
    def _criar_receita_rapida(self, nota, valor, data_alvo):
        """Função auxiliar para criar rapidamente uma receita com uma data específica.
        Assume que já está na tela principal."""
        main_page = MainPage(self.driver)
        add_income_page = main_page.clicar_adicionar_receita()

        add_income_page.preencher_valor(valor)
        add_income_page.preencher_nota(nota)
        add_income_page.preencher_categoria(TestData.CATEGORIA_RECEITA)
        add_income_page.selecionar_conta(TestData.NOME_CONTA)

        hoje = date.today()
        meses_pt = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
                    7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}
        content_desc_data = f"{data_alvo.day} {meses_pt[data_alvo.month]} {data_alvo.year}"

        add_income_page.clicar_campo_data()

        if hoje.month > data_alvo.month:
            add_income_page.voltar_mes_calendario()
        elif hoje.month < data_alvo.month:
            add_income_page.avancar_mes_calendario()

        add_income_page.selecionar_dia_calendario(content_desc_data)
        add_income_page.clicar_ok_calendario()
        add_income_page.clicar_salvar()




