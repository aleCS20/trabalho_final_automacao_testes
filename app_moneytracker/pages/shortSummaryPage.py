from appium.webdriver.common.appiumby import AppiumBy
from app_moneytracker.pages.basePage import BasePage

class ShortSummaryPage(BasePage):
    # ---- Indicadores ------------
    SUMMARY_INDICATOR_ELEMENT = (AppiumBy.ID, "com.blogspot.e_kanivets.moneytracker:id/tvCategory")
    CATEGORY_IN_SUMMARY_LIST = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.blogspot.'
                                                'e_kanivets.moneytracker:id/tvCategory" and @text="{}"]')

    def __init__(self, driver):
        super().__init__(driver)

    def verificar_se_tela_carregou(self):

        print("Verificando se a tela 'Short Summary' foi carregada...")

        return self.is_visible(self.SUMMARY_INDICATOR_ELEMENT)

    def verificar_se_categoria_existe_no_resumo(self, nome_da_categoria):

        print(f"Verificando se a categoria '{nome_da_categoria}' existe no resumo...")
        locator = (self.CATEGORY_IN_SUMMARY_LIST[0], self.CATEGORY_IN_SUMMARY_LIST[1].format(nome_da_categoria))

        return self.is_visible(locator)