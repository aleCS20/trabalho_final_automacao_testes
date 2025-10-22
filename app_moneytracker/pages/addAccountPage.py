from app_moneytracker.pages.basePage import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC

class AddAccountPage(BasePage):
    # --- Localizadores dos elementos ---
    ACCOUNT_NAME_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/etTitle")
    INITIAL_VALUE_FIELD = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/et_init_sum")

    SAVE_BUTTON_CREATE = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/action_done")
    SAVE_BUTTON_EDIT = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/fabDone")

    DELETE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Arquivar"]')
    CONFIRM_DELETE_BUTTON = (AppiumBy.ID, "android:id/button1")

    ERROR_MESSAGE_TEXT = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/textinput_error")
    ERROR_MESSAGE_NAME_FIELD = (AppiumBy.XPATH,
                                '(//android.widget.TextView[@resource-id="com.blogspot.'
                                'e_kanivets.moneytracker:id/textinput_error"])[1]')
    ERROR_MESSAGE_VALUE_FIELD = (AppiumBy.XPATH,
                                 '(//android.widget.TextView[@resource-id="com.blogspot.'
                                 'e_kanivets.moneytracker:id/textinput_error"])[2]')

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_edit_page_to_load(self):

        print("Aguardando a página de edição de conta carregar...")
        self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON_EDIT))
        print("Página de edição de conta carregada.")

        return self

    def preencher_nome_conta(self, nome):
        print(f"Preenchendo nome da conta: '{nome}'")
        self.send_keys(self.ACCOUNT_NAME_FIELD, nome)

    def preencher_valor_inicial(self, valor):
        print(f"Preenchendo valor inicial: '{valor}'")
        self.send_keys(self.INITIAL_VALUE_FIELD, valor)

    def clicar_salvar_criacao(self):
        from app_moneytracker.pages.accountPage import AccountPage

        print("Clicando no botão Salvar (Criação)...")
        self.click(self.SAVE_BUTTON_CREATE)

        return AccountPage(self.driver)

    def clicar_salvar_edicao(self):
        from app_moneytracker.pages.accountPage import AccountPage

        print("Clicando no botão Salvar (Edição)...")
        self.click(self.SAVE_BUTTON_EDIT)

        return AccountPage(self.driver)

    def clicar_remover(self):
        print("Clicando no ícone para 'Arquivar' a conta...")
        self.click(self.DELETE_BUTTON)

        return self

    def confirmar_remocao(self):
        from app_moneytracker.pages.accountPage import AccountPage

        print("Confirmando a remoção da conta...")
        self.click(self.CONFIRM_DELETE_BUTTON)

        return AccountPage(self.driver)

    def obter_mensagem_de_erro(self):
        print("Aguardando mensagem de erro abaixo do campo...")

        return self.get_text(self.ERROR_MESSAGE_TEXT)

    def obter_mensagem_erro_nome(self):
        print("Aguardando mensagem de erro do campo Nome...")

        return self.get_text(self.ERROR_MESSAGE_NAME_FIELD)

    def obter_mensagem_erro_valor(self):
        print("Aguardando mensagem de erro do campo Valor...")

        return self.get_text(self.ERROR_MESSAGE_VALUE_FIELD)
