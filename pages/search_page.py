from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time


class SearchPage:

    SEARCH_BOX = (
        By.XPATH,
        "//*[@id='homeSearch']"
    )

    SUGGESTIONS = (
        By.XPATH,
        "//a[contains(@class,'ui-corner-all')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def search_bike(self, bike_name):

        search = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.SEARCH_BOX
            )
        )

        search.clear()
        search.send_keys(bike_name)

        time.sleep(2)

        keyword = bike_name.lower().split()[0]

        suggestions = self.driver.find_elements(
            *self.SUGGESTIONS
        )

        for i in range(len(suggestions)):

            try:

                suggestions = self.driver.find_elements(
                    *self.SUGGESTIONS
                )

                text = suggestions[i].text.lower()

                print(f"Suggestion: {text}")

                if keyword in text:

                    self.driver.execute_script(
                        "arguments[0].click();",
                        suggestions[i]
                    )

                    return

            except StaleElementReferenceException:
                continue

        raise Exception(
            f"No matching suggestion found for {bike_name}"
        )