import app_moneytracker

from appium.webdriver.common.appiumby import By, AppiumBy
from .basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    NO_THANKS_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@text='NÃO, OBRIGADO']")
    SUMMARY_CARD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/cvSummary")

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






