import json
import requests

import weather_secrets as secrets

# get the base url as a constant
BASE_URL = "http://api.wunderground.com/api/{}/conditions/q".format(secrets.KEY)


def getWeather(location):

    # prompt user for input
    location = location

    # request for the weather update of location user entered
    response = requests.get(BASE_URL + "/{}.json".format(location))
    weather = response.json()

    # check if location was found and notify if it wasn't found
    try:
        current = weather['current_observation']
        country = current['display_location']['country']
        city = current['display_location']['city']
        state = current['display_location']['state']
        temp = current['temperature_string']
        condition = current['weather']
    except KeyError:  # if a location is not found the reponse does not have ['current_observation'] key
        return "Could not find that location"

    return "Currently its {}, {} in {} {}, {}".format(condition, temp, city, state, country)


def main():
    location = input("Where would you like to get the weather for?"
                     "[city, state] ").capitalize()
    response = getWeather(location)

    # print the results
    print(response)

    # if location was not found rerun
    if response == 'Could not find that location':
        main()


if __name__ == "__main__":
    main()
