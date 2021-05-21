#Imports
import time
from covid import Covid

#Stats function
def stats():
    covid = Covid()
    country = input("Enter country you wish to view COVID-19 data for: ")

    #Effective aliases for US and UK
    if country in ('UK', 'U.K.', 'GB', 'G.B.', 'Great Britain', 'Britain'):
        country = 'United Kingdom'
    if country in ('United States', 'USA', 'U.S.A', 'America'):
        country = 'US'
        
    try:
        data = covid.get_status_by_country_name(country)
        print(f"Here are the latest statistics for {country}:")
        print("")
        for key in data:
            print(f"{key} : {data[key]}")

    except ValueError:
        print(f"{country} not found. Try an alternative name or spelling, like US instead of USA.")
    print("")
    answer = input("View data for another country? (Y or anything else to quit): ")
    print("")

    if answer in ('Y', 'y', 'yes', 'Yes', 'YES'):
        stats()

    else:
        print("Exiting program...")
        time.sleep(0.5)

#Initial call
stats()
