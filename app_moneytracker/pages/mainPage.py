from appium.webdriver.common.appiumby import By, AppiumBy
from app_moneytracker.pages.basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from app_moneytracker.pages.accountPage import AccountPage

class MainPage(BasePage):
    """
        Representa a tela principal do aplicativo Money Tracker.
        """
    # --- Localizadores ---
    NO_THANKS_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='NÃO, OBRIGADO']")
    SUMMARY_CARD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/cvSummary")
    NAVIGATION_DRAWER_BUTTON = (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Open navigation drawer"]')

    # --- CORREÇÃO APLICADA AQUI ---
    # Usando o XPath correto para o item de menu "Contas" em português
    ACCOUNTS_MENU_ITEM = (AppiumBy.XPATH,
                          '//android.widget.CheckedTextView[@resource-id="com.blogspot.'
                          'e_kanivets.moneytracker:id/design_menu_item_text" and @text="Contas"]')

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

    ## navegar para adicionar nova conta
    def navegar_para_accounts(self):
        """Abre o menu de navegação e clica no item 'Accounts'.
        Retorna um objeto da página de Contas.
        """
        print("Abrindo menu lateral e navegando para Contas...")
        self.click(self.NAVIGATION_DRAWER_BUTTON)
        self.click(self.ACCOUNTS_MENU_ITEM)
        return AccountPage(self.driver)






