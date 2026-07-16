from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ExpertReviewsPage:

    BIKE_FILTER = (
        By.XPATH,
        "//*[@id='filter_tags']/li[2]/a"
    )

    REVIEW_CARDS = (
        By.XPATH,
        "//*[@id='latest-reviews']/div"
    )

    def __init__(self, driver):
        self.driver = driver

    def click_bike_filter(self):

        bike = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.BIKE_FILTER
            )
        )

        bike.click()

    def get_all_reviews(self):

        cards = self.driver.find_elements(
            *self.REVIEW_CARDS
        )

        reviews = []

        for card in cards:

            try:

                title = card.find_element(
                    By.CSS_SELECTOR,
                    "div.clr-bl.b"
                ).text

                author = card.find_element(
                    By.CSS_SELECTOR,
                    "span.reviewer a"
                ).text

                details = card.find_elements(
                    By.TAG_NAME,
                    "li"
                )

                date = details[1].text
                views = details[2].text
                read_time = details[3].text

                reviews.append(
                    {
                        "title": title,
                        "author": author,
                        "date": date,
                        "views": views,
                        "read_time": read_time
                    }
                )

            except Exception:
                continue

        return reviews