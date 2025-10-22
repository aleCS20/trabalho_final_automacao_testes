from appium.webdriver.common.appiumby import By, AppiumBy
from app_moneytracker.pages.basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from app_moneytracker.pages.accountPage import AccountPage
from app_moneytracker.pages.addIncomePage import AddIncomePage

class MainPage(BasePage):

    # --------- Localizadores -------
    NO_THANKS_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='NÃO, OBRIGADO']")
    SUMMARY_CARD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/cvSummary")
    NAVIGATION_DRAWER_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    ACCOUNTS_MENU_ITEM = (AppiumBy.XPATH,
                          '//android.widget.CheckedTextView[@resource-id="com.blogspot.'
                          'e_kanivets.moneytracker:id/design_menu_item_text" and @text="Contas"]')

    ADD_INCOME_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/btnAddIncome")

    TRANSACTION_NOTE_IN_LIST = (AppiumBy.XPATH,
                                '//android.widget.LinearLayout[@resource-id="com.blogspot.'
                                'e_kanivets.moneytracker:id/container"]/android.widget.LinearLayout[1]')

    TRANSACTION_DATE_IN_LIST = (AppiumBy.XPATH,
                                '//android.widget.LinearLayout[.//android.widget.TextView[@resource-id="'
                                'com.blogspot.e_kanivets.moneytracker:id/tvTitle" and @text="{}"]]//android.widget.'
                                'TextView[@resource-id="com.blogspot.e_kanivets.moneytracker:id/tvDate"]')

    PERIODO_SPINNER = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/spinner")
    PERIODO_OPTION_TEXT = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="{}"]')

    # -----------  --------  ----------  #
    def __init__(self, driver):
        super().__init__(driver)

    def fechar_dialogo_inicial_se_existir(self):
        try:
            short_wait = WebDriverWait(self.driver, 5)
            no_thanks_btn = short_wait.until(EC.element_to_be_clickable(self.NO_THANKS_BUTTON))
            print("Dialogo inicial encontrado. Clicando em 'Não, obrigado' . ")
            no_thanks_btn.click()
        except Exception:
            print("Dialogo inicial não encontrado. Prosseguindo!! ")

        return self

    def verificar_se_tela_principal_carregou(self):
        return self.is_visible(self.SUMMARY_CARD)

    def navegar_para_accounts(self):
        print("Abrindo menu lateral e navegando para Contas...")
        self.click(self.NAVIGATION_DRAWER_BUTTON)
        self.click(self.ACCOUNTS_MENU_ITEM)

        return AccountPage(self.driver)

    def clicar_adicionar_receita(self):

        print("Clicando no botão 'ADD INCOME'...")
        self.click(self.ADD_INCOME_BUTTON)

        return AddIncomePage(self.driver)

    def verificar_se_transacao_existe_por_nota(self, nota):
        print(f"Verificando se a transação com a nota '{nota}' existe na lista...")
        locator = (self.TRANSACTION_NOTE_IN_LIST[0], self.TRANSACTION_NOTE_IN_LIST[1].format(nota))

        return self.is_visible(locator)

    def selecionar_transacao_por_nota(self, nota):

        from app_moneytracker.pages.addIncomePage import AddIncomePage

        print(f"Selecionando a transação com a nota '{nota}'...")

        locator = (self.TRANSACTION_NOTE_IN_LIST[0], self.TRANSACTION_NOTE_IN_LIST[1].format(nota))
        self.click(locator)

        return AddIncomePage(self.driver)

    def obter_data_da_transacao_por_nota(self, nota):

        print(f"Obtendo a data da transação com a nota '{nota}'...")
        locator = (self.TRANSACTION_DATE_IN_LIST[0], self.TRANSACTION_DATE_IN_LIST[1].format(nota))

        return self.get_text(locator)

    def selecionar_periodo_do_resumo(self, periodo):

        print(f"Selecionando o período de resumo: '{periodo}'")
        self.click(self.PERIODO_SPINNER)

        locator = (self.PERIODO_OPTION_TEXT[0], self.PERIODO_OPTION_TEXT[1].format(periodo))
        self.click(locator)

        return self

    def clicar_short_summary(self):

        from app_moneytracker.pages.shortSummaryPage import ShortSummaryPage

        print("Clicando no card 'Short Summary'...")
        self.click(self.SUMMARY_CARD)

        return ShortSummaryPage(self.driver)


