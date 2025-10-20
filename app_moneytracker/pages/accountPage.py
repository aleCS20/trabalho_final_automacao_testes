import time

from app_moneytracker.pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
#from app_moneytracker.pages.addAccountPage import AddAccountPage

class AccountPage(BasePage):
    ADD_ACCOUNT_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/btn_add_account")

    # Localizador dinâmico para encontrar uma conta na lista pelo seu nome
    ACCOUNT_NAME_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.blogspot.'
                                            'e_kanivets.moneytracker:id/tvTitle" and @text="{}"]')

    ACCOUNT_BALANCE_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@text="{}"]/ancestor::'
                                               'android.widget.RelativeLayout//android.widget.TextView'
                                               '[@resource-id="com.blogspot.e_kanivets.moneytracker:id/tv_cur_sum"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_adicionar_conta(self):
        """Clica no botão '+' para adicionar uma nova conta."""
        from app_moneytracker.pages.addAccountPage import AddAccountPage

        print("Clicando no botão para adicionar nova conta...")
        self.click(self.ADD_ACCOUNT_BUTTON)
        return AddAccountPage(self.driver)

    def verificar_se_conta_existe(self, nome_da_conta):
        """Verifica se uma conta com o nome especificado está visível na lista."""
        print(f"Verificando se a conta '{nome_da_conta}' existe na lista...")

        time.sleep(3)
        # Formata o localizador com o nome da conta
        locator = (self.ACCOUNT_NAME_IN_LIST[0], self.ACCOUNT_NAME_IN_LIST[1].format(nome_da_conta))
        return self.is_visible(locator)

    def obter_saldo_da_conta(self, nome_da_conta):
        """Encontra uma conta na lista e retorna o texto do seu saldo."""
        print(f"Obtendo saldo da conta '{nome_da_conta}'...")
        locator = (self.ACCOUNT_BALANCE_IN_LIST[0], self.ACCOUNT_BALANCE_IN_LIST[1].format(nome_da_conta))
        return self.get_text(locator)
