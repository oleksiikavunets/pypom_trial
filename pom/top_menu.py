from pypom import Region
from selenium.webdriver.common.by import By


class TopMenu(Region):

    @property
    def entries(self):
        return {
            self.Entry(self.page, item) for item in self.find_elements(*self.Entry.entry_locator)
        }

    def _filter_items(self):
        return [el for el in self.entries if len(el.name) > 0]

    def _get_sorted_els(self):
        return sorted(self._filter_items(), key=lambda el: el.name)

    def _get_names(self):
        return [n.name for n in self._get_sorted_els() if len(n.name) > 0]

    def get_items(self):
        return dict(zip(sorted(self._get_names()), self._get_sorted_els()))

    def get_menu_item(self, key):
        return self.get_items()[key]

    def open_menu_item(self, key):
        self.get_items()[key].click()

    class Entry(Region):
        entry_locator = (By.CSS_SELECTOR, 'li>a[href]')

        @property
        def name(self):
            return self.root.text

        @property
        def get_attribute(self):
            return self.root.get_attribute("href")

        def click(self):
            self.root.click()


class Items:
    NP_SHOPPING = 'NP Shopping'
    BUSINESS_CLIENTS = 'Бізнес-Клієнтам'
    PRIVATE_CLIENTS = 'Приватним Клієнтам'
    OFFICES = 'Відділення'
    INCREASE_OPPORTUNITIES = 'Збільшуй можливості '
    INTERNATIONAL_DELIVERY = 'Міжнародна доставка'
    ABOUT_COMPANY = 'Про компанію'
