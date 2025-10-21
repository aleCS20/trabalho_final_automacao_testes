from appium.webdriver.common.appiumby import AppiumBy
from app_moneytracker.pages.basePage import BasePage


class AddIncomePage(BasePage):
    # --- Localizadores Corrigidos (com base na sua imagem e IDs) ---
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

    # Opção de texto dentro de uma lista de dropdown
    OPTION_TEXT_IN_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="{}"]')

    SAVE_BUTTON = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/fabDone")

    def __init__(self, driver):
        super().__init__(driver)

    def obter_mensagem_erro_nota(self):
        """Captura o texto da mensagem de erro abaixo do campo NOTA/TÍTULO."""
        print("Aguardando mensagem de erro do campo Nota/Título...")
        return self.get_text(self.ERROR_MESSAGE_NOTE)

    def preencher_valor(self, valor):
        print(f"Preenchendo valor: '{valor}'")
        self.send_keys(self.AMOUNT_FIELD, valor)

    def preencher_nota(self, nota):
        print(f"Preenchendo nota (título): '{nota}'")
        self.send_keys(self.NOTE_FIELD, nota)

    # --- MÉTODO CORRIGIDO ---
    def preencher_categoria(self, nome_categoria):
        """Digita diretamente no campo de texto da categoria."""
        print(f"Preenchendo categoria: '{nome_categoria}'")
        self.send_keys(self.CATEGORY_FIELD, nome_categoria)

    def selecionar_conta(self, nome_conta):
        """Clica no dropdown de conta e seleciona a opção desejada."""
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
        """Captura o texto da mensagem de erro abaixo do campo VALOR."""
        print("Aguardando mensagem de erro do campo Valor...")
        return self.get_text(self.ERROR_MESSAGE_PRICE)

    def obter_mensagem_erro_categoria(self):
        """Captura o texto da mensagem de erro abaixo do campo CATEGORIA."""
        print("Aguardando mensagem de erro do campo Categoria...")
        return self.get_text(self.ERROR_MESSAGE_CATEGORY)