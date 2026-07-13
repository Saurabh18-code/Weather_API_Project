import requests
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 200:

            data = response.json()

            print("\n==============================")
            print("      WEATHER REPORT")
            print("==============================")
            print(f"City          : {data['name']}")
            print(f"Country       : {data['sys']['country']}")
            print(f"Temperature   : {data['main']['temp']} °C")
            print(f"Feels Like    : {data['main']['feels_like']} °C")
            print(f"Humidity      : {data['main']['humidity']} %")
            print(f"Pressure      : {data['main']['pressure']} hPa")
            print(f"Weather       : {data['weather'][0]['main']}")
            print(f"Description   : {data['weather'][0]['description']}")
            print(f"Wind Speed    : {data['wind']['speed']} m/s")
            print("==============================\n")

        elif response.status_code == 404:
            print("\n❌ City not found.\n")

        elif response.status_code == 401:
            print("\n❌ Invalid API Key.\n")

        else:
            print(f"\n❌ Error: {response.status_code}\n")

    except requests.exceptions.ConnectionError:
        print("\n❌ No Internet Connection.\n")

    except requests.exceptions.Timeout:
        print("\n❌ Request Timed Out.\n")

    except Exception as e:
        print("\nUnexpected Error:", e)


def main():

    print("=" * 40)
    print("   WEATHER API INTEGRATION PROJECT")
    print("=" * 40)

    while True:

        city = input("\nEnter City Name (or type exit): ")

        if city.lower() == "exit":
            print("\nThank you for using the Weather App.")
            break

        if city.strip() == "":
            print("Please enter a valid city.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()