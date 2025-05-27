import requests

API_KEY=''
BASE_URL="http://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params={
        'q':city,
        'aapid':API_KEY,
        'units':'metric'

    }
    response=requests.get(BASE_URL,params=params)
    if response.status_code==200:
        data=response.json()
        temp=data['main']['temp']
        humidity=data['main']['humidity']
        description=data['weather'][0]['description']

        print(f"\n Weather in{city.title()}")

        print(f"Temperature: {temp}C")
        print(f"Humidity:{humidity}")
        print(f"Description:{description.capitalize()}")
    else:
        print("City not found or error in API request")


def main():
    city=input("Enter city name: ")
    get_weather(city)

main()

