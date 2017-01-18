import json
import requests

import weather_secrets as secrets

# get the base url as a constant
BASE_URL = "http://api.wunderground.com/api/{}/conditions/q".format(secrets.KEY)


def main():

    # prompt user for input
    location = input("Where would you like to get the weather for? ")

    # request for the weather update of location user entered
    response = requests.get(BASE_URL + "/{}.json".format(location))
    weather = response.json()
    current = weather['current_observation']
    country = current['display_location']['country']
    city = current['display_location']['city']
    state = current['display_location']['state']
    temp = current['temperature_string']
    condition = current['weather']

    print(weather)


if __name__ == "__main__":
    main()
