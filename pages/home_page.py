from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    # NEWS & REVIEWS
    NEWS_REVIEWS = (
        By.XPATH,
        "//*[@id='headerNewVNavWrap']/nav/ul/li[1]"
    )

    EXPERT_REVIEWS = (
        By.XPATH,
        "//*[@id='headerNewVNavWrap']/nav/ul/li[1]/ul/li[2]/a"
    )

    # NEW BIKES
    NEW_BIKES = (
        By.XPATH,
        "//*[@id='headerNewVNavWrap']/nav/ul/li[3]/span"
    )

    UPCOMING_BIKES = (
        By.XPATH,
        "//*[@id='headerNewVNavWrap']/nav/ul/li[3]/ul/li[4]/a"
    )

    BIKE_DEALERS = (
        By.XPATH,
        "//*[@id='headerNewVNavWrap']/nav/ul/li[3]/ul/li[7]/a"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_home_page(self):

        self.driver.get(
            "https://www.zigwheels.com/"
        )

    def click_expert_reviews(self):

        actions = ActionChains(
            self.driver
        )

        news_reviews = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(
                self.NEWS_REVIEWS
            )
        )

        actions.move_to_element(
            news_reviews
        ).perform()

        expert_reviews = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.EXPERT_REVIEWS
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            expert_reviews
        )

    def click_upcoming_bikes(self):

        actions = ActionChains(
            self.driver
        )

        new_bikes = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(
                self.NEW_BIKES
            )
        )

        actions.move_to_element(
            new_bikes
        ).perform()

        upcoming = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.UPCOMING_BIKES
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            upcoming
        )

    def click_bike_dealers(self):

        actions = ActionChains(
            self.driver
        )

        new_bikes = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.visibility_of_element_located(
                self.NEW_BIKES
            )
        )

        actions.move_to_element(
            new_bikes
        ).perform()

        bike_dealers = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.BIKE_DEALERS
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            bike_dealers
        )