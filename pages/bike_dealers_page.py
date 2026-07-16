from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BikeDealersPage:

    TOP_CITIES_SECTION = (
        By.XPATH,
        "//*[@id='zwn-search']/div/div/div[1]/div[5]"
    )

    CITY_CARDS = (
        By.XPATH,
        "//*[@id='zwn-search']/div/div/div[1]/div[5]//li"
    )

    def __init__(self, driver):
        self.driver = driver

    def get_top_city_showrooms(self):

        section = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                self.TOP_CITIES_SECTION
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            section
        )

        city_cards = self.driver.find_elements(
            *self.CITY_CARDS
        )

        showroom_data = []

        for city in city_cards:

            text = city.text.strip()

            if text:

                showroom_data.append(
                    text
                )

        return showroom_data