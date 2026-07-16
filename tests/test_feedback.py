import time

from pages.feedback_page import FeedbackPage


def test_feedback_positive(driver):

    driver.get(
        "https://www.zigwheels.com/"
    )

    feedback = FeedbackPage(driver)

    feedback.open_feedback_popup()

    feedback.select_happy_emoji()

    feedback.enter_feedback(
        "This website provides excellent bike information and reviews."
    )

    feedback.click_submit()

    msg = feedback.get_thank_you_message()

    print("\nThank You Message:")
    print(msg)

    assert "thank you" in msg.lower()


def test_feedback_without_emoji(driver):

    driver.get(
        "https://www.zigwheels.com/"
    )

    feedback = FeedbackPage(driver)

    feedback.open_feedback_popup()

    feedback.enter_feedback(
        "This website provides excellent bike information."
    )

    feedback.click_submit()

    time.sleep(2)

    assert (
        "feedback"
        in driver.page_source.lower()
    )


def test_feedback_less_than_20_characters(driver):

    driver.get(
        "https://www.zigwheels.com/"
    )

    feedback = FeedbackPage(driver)

    feedback.open_feedback_popup()

    feedback.select_happy_emoji()

    feedback.enter_feedback(
        "Good website"
    )

    feedback.click_submit()

    time.sleep(2)

    assert (
        "feedback"
        in driver.page_source.lower()
    )