from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import json

from rasa.constants import DEFAULT_DATA_PATH
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet

from zomato.zomato_api import Zomato


logger = logging.getLogger("__name__")
user_key = ""
config = {"user_key": user_key}
_zomato = Zomato(config)


""" Custom action to fetch list of restaurants
"""
class ActionSearchRestaurants(Action):
    def name(self):
        return "action_restaurant"

    def run(self, dispatcher, tracker, domain):

        restaurants_found = []
        response_message = ""

        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")

        if not location:
            dispatcher.utter_template("utter_ask_location", tracker)
        else:
            """
				retrieve location details
			"""
            response = _zomato.get_location(location)
            location_details = {}

            if response is not None:
                response_json = json.loads(response)
                if response_json["status"] == "success":
                    """
						fetch location details and store 'city_id'
					"""
                    location_details = response_json["location_suggestions"][0]
                    city_id = location_details["city_id"]

                    """
						fetch all cuisines available in the location
					"""
                    response_cuisine = _zomato.get_cuisines(city_id)
                    supported_cuisines = [
                        "American",
                        "Chinese",
                        "Italian",
                        "Mexican",
                        "North Indian",
                        "South Indian",
                    ]
                    filtered_cuisine = {
                        key: value
                        for key, value in response_cuisine.items()
                        if value in supported_cuisines
                    }

                    if cuisine is not None:
                        cuisine_list = [
                            key
                            for key, value in filtered_cuisine.items()
                            if str(value).lower() == cuisine.lower()
                        ]
                    else:
                        cuisine_list = [key for key, value in filtered_cuisine.items()]

                    restaurants_found = self.search_restaurant(
                        location, location_details, cuisine_list
                    )

                    if len(restaurants_found) > 0:
                        for restaurant in restaurants_found:
                            response_message = (
                                response_message
                                + restaurant["name"]
                                + " in "
                                + restaurant["address"]
                                + " has been rated "
                                + restaurant["rating"]
                                + "\n"
                            )
                    else:
                        response_message = "no results"
            else:
                dispatcher.utter_message("no results")

        dispatcher.utter_message(response_message)

        return [SlotSet("location", location)]

    def search_restaurant(
        self, location="", location_details={}, cuisine_list=[]
    ) -> list:
        restaurants_found = []

        """
			Search restaurants
		"""
        response = _zomato.restaurant_search(
            location,
            location_details["latitude"],
            location_details["longitude"],
            cuisine_list,
            location_details["city_id"],
            "city",
        )

        if response is not None:
            response_json = json.loads(response)
            if response_json["results_found"] > 0:
                for restaurant in response_json["restaurants"]:
                    restaurants_found.append(
                        {
                            "name": restaurant["restaurant"]["name"],
                            "address": restaurant["restaurant"]["location"]["address"],
                            "avg_cost_for_2": restaurant["restaurant"]["average_cost_for_two"],
                            "rating": restaurant["restaurant"]["user_rating"]["aggregate_rating"],
                        }
                    )

        return restaurants_found


""" Custom action to validate input location
"""
class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location_validity = "valid"

        if not location:
            dispatcher.utter_template("utter_ask_location", tracker)
            location_validity = "invalid"
        else:
            filepath = DEFAULT_DATA_PATH + "/cities.json"

            with open(filepath) as cities_file:

                data = json.load(cities_file)

                if data is not None:
                    tier1_cities = data["data"]["tier1"]
                    tier2_cities = data["data"]["tier2"]

                    tier1_cities_lower = [city.lower() for city in tier1_cities]
                    tier2_cities_lower = [city.lower() for city in tier2_cities]

                    location_validity = (
                        "invalid"
                        if location.lower() not in tier1_cities_lower and location.lower() not in tier2_cities_lower
                        else "valid"
                    )
                else:
                    location_validity = "invalid"

        return [SlotSet("location_validity", location_validity)]


""" Custom action to validate input cuisine
"""
class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            dispatcher.utter_template("utter_ask_cuisine", tracker)
            cuisine_validity = "invalid"
        else:
            supported_cuisines = [
                "american",
                "chinese",
                "italian",
                "mexican",
                "north indian",
                "south indian",
            ]

            cuisine_validity = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid"
            )

        return [SlotSet("cuisine_validity", cuisine_validity)]
