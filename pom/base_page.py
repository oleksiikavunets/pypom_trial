from pypom import Page
from selenium.webdriver.common.by import By

from pom.top_menu import TopMenu


class BasePage(Page):
    URL_TEMPLATE = '/'

    @property
    def top_menu(self):
        root = self.find_element(By.ID, "top_menu")
        return TopMenu(self, root=root)

