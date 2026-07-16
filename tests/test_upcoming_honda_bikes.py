import time

from pages.home_page import HomePage
from pages.upcoming_bikes_page import UpcomingBikesPage


def test_honda_upcoming_bikes(driver):

    home =    home = HomePage(driver)

    home.open_home_page()

    home.click_upcoming_bikes()

    upcoming = UpcomingBikesPage(driver)

    time.sleep(3)

    upcoming.click_under_5_lakhs()

    time.sleep(3)

    upcoming.click_honda_filter()

    time.sleep(5)

    bikes = upcoming.get_honda_bikes()

    print("\n" + "=" * 60)
    print("HONDA UPCOMING BIKES")
    print("=" * 60)

    for bike in bikes:

        print(f"\nBike Name : {bike['name']}")
        print(f"Price     : {bike['price']}")
        print(f"Launch    : {bike['launch']}")

    print(f"\nTotal Bikes Found : {len(bikes)}")

