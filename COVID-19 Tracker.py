import time
from covid import Covid
def tracker():
    covid = Covid()
    country = input("Enter country you wish to view COVID-19 data for: ")
    try:
     data = covid.get_status_by_country_name(country)
     print(f"Showing details for {country}")
     for key in data:
            print(f"{key} : {data[key]}")

    except ValueError:
        print("Country not found, please check input.")
        print("Try alternative spellings of names. Sub-countries like Wales may not work")
    answer = input("View another countries COVID data? (N to end program.) Y/N: ")

    if answer == 'N' or answer == 'n':
        print("Exiting program...")
        time.sleep(1)
        
    elif answer == 'Y' or answer == 'y':
        tracker()

tracker()
