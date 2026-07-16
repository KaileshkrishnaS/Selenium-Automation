import time

from pages.home_page import HomePage
from pages.expert_reviews_page import ExpertReviewsPage


def test_bike_expert_reviews(driver):

    home = HomePage(driver)

    home.open_home_page()

    home.click_expert_reviews()

    reviews_page = ExpertReviewsPage(
        driver
    )

    time.sleep(3)

    reviews_page.click_bike_filter()

    time.sleep(3)

    reviews = reviews_page.get_all_reviews()

    print("\n")
    print("=" * 70)
    print("BIKE EXPERT REVIEWS")
    print("=" * 70)

    for review in reviews:

        print(f"\nTitle     : {review['title']}")
        print(f"Author    : {review['author']}")
        print(f"Date      : {review['date']}")
        print(f"Views     : {review['views']}")
        print(f"Read Time : {review['read_time']}")

        print("-" * 70)

    assert len(reviews) > 0