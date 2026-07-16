from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FeedbackPage:

    FEEDBACK_LINK = (
        By.XPATH,
        "/html/body/footer/div[2]/div/ul[2]/li[3]/span"
    )

    HAPPY_EMOJI = (
        By.XPATH,
        "//*[@id='feedback_form']/div/div[1]/div[3]/label/span"
    )

    FEEDBACK_TEXT = (
        By.XPATH,
        "//*[@id='feedback_comment']"
    )

    SUBMIT_BUTTON = (
        By.XPATH,
        "//*[@id='feedback_submit']"
    )

    THANK_YOU_MESSAGE = (
        By.XPATH,
        "//*[@id='feedback_thankYou']/div/p"
    )

    def __init__(self, driver):
        self.driver = driver

    def open_feedback_popup(self):

        feedback = WebDriverWait(
            self.driver,
            15
        ).until(
            EC.element_to_be_clickable(
                self.FEEDBACK_LINK
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView(true);",
            feedback
        )

        self.driver.execute_script(
            "arguments[0].click();",
            feedback
        )

    def select_happy_emoji(self):

        emoji = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.HAPPY_EMOJI
            )
        )

        emoji.click()

    def enter_feedback(self, text):

        textbox = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.FEEDBACK_TEXT
            )
        )

        textbox.clear()
        textbox.send_keys(text)

    def click_submit(self):

        submit = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.element_to_be_clickable(
                self.SUBMIT_BUTTON
            )
        )

        submit.click()

    def get_thank_you_message(self):

        message = WebDriverWait(
            self.driver,
            10
        ).until(
            EC.visibility_of_element_located(
                self.THANK_YOU_MESSAGE
            )
        )

        return message.text