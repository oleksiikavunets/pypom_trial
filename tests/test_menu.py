from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pom.base_page import BasePage
from pom.top_menu import Items
from time import sleep


class TestMenu:

    def test_menu_1(self):

        driver = webdriver.Chrome(ChromeDriverManager().install())

        bp = BasePage(driver, 'https://novaposhta.ua').open()
        bp.top_menu.get_menu_item(Items.NP_SHOPPING)
        item_name = bp.top_menu.get_menu_item(Items.ABOUT_COMPANY).name

        print(item_name)
        bp.top_menu.get_menu_item(Items.ABOUT_COMPANY).click()

        print("CLICKED")
        sleep(5)

        driver.quit()

