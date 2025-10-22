import time

from app_moneytracker.pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class AccountPage(BasePage):
    ADD_ACCOUNT_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/btn_add_account")

    # Localizador dinâmico dos elementos
    ACCOUNT_NAME_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.blogspot.'
                                            'e_kanivets.moneytracker:id/tvTitle" and @text="{}"]')

    ACCOUNT_BALANCE_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@text="{}"]/ancestor::'
                                               'android.widget.RelativeLayout//android.widget.TextView'
                                               '[@resource-id="com.blogspot.e_kanivets.moneytracker:id/tv_cur_sum"]')

    def __init__(self, driver):
        super().__init__(driver)

    def clicar_adicionar_conta(self):

        from app_moneytracker.pages.addAccountPage import AddAccountPage

        print("Clicando no botão para adicionar nova conta...")
        self.click(self.ADD_ACCOUNT_BUTTON)
        return AddAccountPage(self.driver)

    def verificar_se_conta_existe(self, nome_da_conta):

        print(f"Verificando se a conta '{nome_da_conta}' existe na lista...")

        time.sleep(3)

        locator = (self.ACCOUNT_NAME_IN_LIST[0], self.ACCOUNT_NAME_IN_LIST[1].format(nome_da_conta))

        return self.is_visible(locator)

    def obter_saldo_da_conta(self, nome_da_conta):

        print(f"Obtendo saldo da conta '{nome_da_conta}'...")
        locator = (self.ACCOUNT_BALANCE_IN_LIST[0], self.ACCOUNT_BALANCE_IN_LIST[1].format(nome_da_conta))
        return self.get_text(locator)

    def selecionar_conta_por_nome(self, nome_da_conta):

        from app_moneytracker.pages.addAccountPage import AddAccountPage

        print(f"Selecionando a conta '{nome_da_conta}' para edição...")

        locator = (self.ACCOUNT_NAME_IN_LIST[0], self.ACCOUNT_NAME_IN_LIST[1].format(nome_da_conta))
        self.click(locator)

        edit_page = AddAccountPage(self.driver)
        edit_page.wait_for_edit_page_to_load()

        return edit_page