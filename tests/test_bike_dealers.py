import time

from pages.home_page import HomePage
from pages.bike_dealers_page import BikeDealersPage


def test_bike_showrooms_top_cities(driver):

    home = HomePage(driver)

    home.open_home_page()

    home.click_bike_dealers()

    dealers = BikeDealersPage(
        driver
    )

    time.sleep(3)

    cities = (
        dealers.get_top_city_showrooms()
    )

    print("\n")
    print("=" * 60)
    print("BIKE SHOWROOMS IN TOP CITIES")
    print("=" * 60)

    for city in cities:

        print(city)
        print("-" * 60)

    assert len(cities) > 0