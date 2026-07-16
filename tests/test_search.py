import time

from pages.search_page import SearchPage
from utilities.excel_utils import ExcelUtils


def test_search_bikes(driver):

    page = SearchPage(driver)

    excel = ExcelUtils(
        "test_cases.xlsx"
    )

    row_count = excel.get_row_count()

    for row in range(2, row_count + 1):

        bike_name = excel.get_bike_name(row)

        try:

            print(f"\nSearching : {bike_name}")

            driver.get(
                "https://www.zigwheels.com/"
            )

            page.search_bike(
                bike_name
            )

            time.sleep(3)

            current_url = (
                driver.current_url
                .lower()
            )

            print(
                f"Current URL : {current_url}"
            )

            excel.write_url(
                row,
                current_url
            )

            keyword = (
                bike_name.lower()
                .split()[0]
            )

            if keyword in current_url:

                excel.write_status(
                    row,
                    "Passed"
                )

                print(
                    f"{bike_name} -> PASSED"
                )

            else:

                excel.write_status(
                    row,
                    "Failed"
                )

                print(
                    f"{bike_name} -> FAILED"
                )

        except Exception as e:

            excel.write_status(
                row,
                "Failed"
            )

            excel.write_url(
                row,
                "ERROR"
            )

            print(
                f"Error for {bike_name}"
            )

            print(
                type(e).__name__
            )

            print(str(e))

            continue

    try:

        excel.save()

    except PermissionError:

        print(
            "\nExcel file is open. "
            "Close test_cases.xlsx and rerun."
        )

        raise