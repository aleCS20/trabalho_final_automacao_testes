from app_moneytracker.Data import TestData
from app_moneytracker.pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
#from app_moneytracker.pages.accountPage import AccountPage

class AddAccountPage(BasePage):

    ACCOUNT_NAME_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/etTitle")
    INITIAL_VALUE_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/et_init_sum")
    SAVE_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/action_done")
    ERROR_MESSAGE_TEXT = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/textinput_error")

    def obter_mensagem_de_erro(self):
        """Captura e retorna o texto da mensagem de erro que aparece abaixo do campo de texto."""
        print("Aguardando mensagem de erro abaixo do campo...")
        # Usa o novo localizador com o ID correto
        return self.get_text(self.ERROR_MESSAGE_TEXT)

    def __init__(self, driver):
        super().__init__(driver)

    def preencher_nome_conta(self, nome):
        """Preenche o campo 'Nome da Conta'."""
        print(f"Preenchendo nome da conta: '{nome}'")
        self.send_keys(self.ACCOUNT_NAME_FIELD, nome)

    def preencher_valor_inicial(self, valor):
        """Preenche o campo 'Valor Inicial'."""
        print(f"Preenchendo valor inicial: '{valor}'")
        self.send_keys(self.INITIAL_VALUE_FIELD, valor)

    def clicar_salvar(self):
        """Clica no botão de salvar."""
        from app_moneytracker.pages.accountPage import AccountPage

        print("Clicando no botão Salvar...")
        self.click(self.SAVE_BUTTON)
        return AccountPage(self.driver)

