from appium.webdriver.common.appiumby import AppiumBy
from app_moneytracker.pages.basePage import BasePage
from datetime import date

class AddIncomePage(BasePage):
    # -------- Localizadores  -------
    AMOUNT_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/etPrice")
    NOTE_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/etTitle")
    CATEGORY_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/etCategory")
    ACCOUNT_SPINNER = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/spinnerAccount")

    ERROR_MESSAGE_NOTE = (AppiumBy.XPATH,
                          '(//android.widget.TextView[@resource-id="com.blogspot.'
                          'e_kanivets.moneytracker:id/textinput_error"])[1]')
    ERROR_MESSAGE_PRICE = (AppiumBy.XPATH,
                           '(//android.widget.TextView[@resource-id="com.blogspot.'
                           'e_kanivets.moneytracker:id/textinput_error"])[1]')
    ERROR_MESSAGE_CATEGORY = (AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="com.blogspot.'
                                              'e_kanivets.moneytracker:id/textinput_error"])[1]')

    OPTION_TEXT_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="{}"]')

    SAVE_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/fabDone")
    DELETE_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/action_delete")

    DATE_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/tvDate")

    CALENDAR_PREV_MONTH_BUTTON = (AppiumBy.ID, "android:id/prev")
    CALENDAR_DAY_VIEW = (AppiumBy.XPATH, '//android.view.View[@content-desc="{}"]')  # Para o dia dinâmico
    CALENDAR_OK_BUTTON = (AppiumBy.ID, "android:id/button1")
    CALENDAR_NEXT_MONTH_BUTTON = (AppiumBy.ID, "android:id/next")

    TOAST_MESSAGE = (AppiumBy.XPATH, '//android.widget.Toast[1]')
    # ------------------ ----------- ------------------ #
    def __init__(self, driver):
        super().__init__(driver)

    def clicar_campo_data(self):
        print("Abrindo o calendário...")
        self.click(self.DATE_FIELD)

    def voltar_mes_calendario(self):
        print("Voltando para o mês anterior...")
        self.click(self.CALENDAR_PREV_MONTH_BUTTON)

    def selecionar_dia_calendario(self, content_desc_dia):
        print(f"Selecionando o dia: '{content_desc_dia}'")
        locator = (self.CALENDAR_DAY_VIEW[0], self.CALENDAR_DAY_VIEW[1].format(content_desc_dia))
        self.click(locator)

    def verificar_data_atual_selecionada(self):

        hoje = date.today()

        meses_pt = {1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril", 5: "maio", 6: "junho",
                    7: "julho", 8: "agosto", 9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro"}

        content_desc_hoje = f"{hoje.day} {meses_pt[hoje.month]} {hoje.year}"
        print(f"Verificando se o dia selecionado é: '{content_desc_hoje}'")

        dia_selecionado_locator = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{content_desc_hoje}"]')

        return self.is_visible(dia_selecionado_locator)

    def clicar_ok_calendario(self):
        print("Confirmando a data no calendário...")
        self.click(self.CALENDAR_OK_BUTTON)

    def avancar_mes_calendario(self):
        print("Avançando para o próximo mês...")
        self.click(self.CALENDAR_NEXT_MONTH_BUTTON)

    def obter_mensagem_toast(self):
        print("Aguardando mensagem de erro (Toast)...")

        return self.get_toast_text()

    def obter_mensagem_erro_nota(self):
        print("Aguardando mensagem de erro do campo Nota/Título...")

        return self.get_text(self.ERROR_MESSAGE_NOTE)

    def preencher_valor(self, valor):
        print(f"Preenchendo valor: '{valor}'")
        self.send_keys(self.AMOUNT_FIELD, valor)

    def preencher_nota(self, nota):
        print(f"Preenchendo nota (título): '{nota}'")
        self.send_keys(self.NOTE_FIELD, nota)

    def preencher_categoria(self, nome_categoria):
        print(f"Preenchendo categoria: '{nome_categoria}'")
        self.send_keys(self.CATEGORY_FIELD, nome_categoria)

    def selecionar_conta(self, nome_conta):
        print(f"Selecionando conta: '{nome_conta}'")
        self.click(self.ACCOUNT_SPINNER)
        locator = (self.OPTION_TEXT_IN_LIST[0], self.OPTION_TEXT_IN_LIST[1].format(nome_conta))
        self.click(locator)

    def clicar_salvar(self):
        from app_moneytracker.pages.mainPage import MainPage

        print("Clicando no botão Salvar...")
        self.click(self.SAVE_BUTTON)

        return MainPage(self.driver)

    def obter_mensagem_erro_valor(self):
        print("Aguardando mensagem de erro do campo Valor...")

        return self.get_text(self.ERROR_MESSAGE_PRICE)

    def obter_mensagem_erro_categoria(self):
        print("Aguardando mensagem de erro do campo Categoria...")

        return self.get_text(self.ERROR_MESSAGE_CATEGORY)

    def clicar_remover(self):
        from app_moneytracker.pages.mainPage import MainPage

        print("Clicando no ícone para 'Arquivar' (remover) a transação...")
        self.click(self.DELETE_BUTTON)

        return MainPage(self.driver)