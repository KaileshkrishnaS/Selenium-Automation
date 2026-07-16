import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UpcomingBikesPage:

    UNDER_5_LAKHS = (
        By.XPATH,
        "//a[contains(text(),'Upcoming Bikes Under 5 Lakhs')]"
    )

    HONDA_FILTER = (
        By.XPATH,
        "//a[contains(text(),'Honda')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_under_5_lakhs(self):

        element = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                self.UNDER_5_LAKHS
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    def click_honda_filter(self):

        honda = WebDriverWait(
            self.driver,
            20
        ).until(
            EC.presence_of_element_located(
                self.HONDA_FILTER
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            honda
        )

        time.sleep(2)

        self.driver.execute_script(
            "arguments[0].click();",
            honda
        )

    def get_honda_bikes(self):

        cards = self.driver.find_elements(
            By.XPATH,
            "//*[@id='modelList']/li"
        )

        bikes = []

        for card in cards:

            try:

                bike_name = card.find_element(
                    By.TAG_NAME,
                    "a"
                ).text

                price = card.find_element(
                    By.XPATH,
                    ".//div[contains(text(),'Rs.')]"
                ).text

                launch = card.find_element(
                    By.XPATH,
                    ".//*[contains(text(),'Expected Launch')]"
                ).text

                bikes.append({
                    "name": bike_name,
                    "price": price,
                    "launch": launch
                })

            except Exception:
                continue

        return bikes