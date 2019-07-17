import json
import logging

from .zomato_api import Zomato

logger = logging.getLogger("__name__")

user_key = ""
config = {"user_key": user_key}
_zomato = Zomato(config)


def test_location_search(location="") -> dict:
    response = _zomato.get_location(location)
    location_details = {}

    if response is not None:
        response_json = json.loads(response)
        if response_json["status"] == "success":
            location_details = response_json["location_suggestions"][0]

    logger.info("calling Zomato /locations API with location - '%s'", location)
    logger.info(json.dumps(location_details, sort_keys=True, indent=4))

    return location_details


def test_cuisine_search(location="", city_id=0) -> dict:
    response_cuisine = {}
    filtered_cuisine = {}

    if city_id is None or city_id == 0:
        location_details = test_location_search(location)
        city_id = location_details["city_id"]

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

    logger.info(
        "calling Zomato /cuisines API with location - '%s' or city_id - '%s'",
        location,
        city_id,
    )
    logger.info(json.dumps(filtered_cuisine, sort_keys=True, indent=4))

    return filtered_cuisine


def test_restaurant_search(location="", cuisine="") -> None:
    """
        Step 1 : retrieve details about the location
    """
    if location is not None:
        location_details = test_location_search(location=location)

        """
            Step 2 : Cuisine details
        """
        cuisine_details = test_cuisine_search(city_id=location_details["city_id"])
        if cuisine is not None:
            cuisine_list = [
                key
                for key, value in cuisine_details.items()
                if str(value).lower() == cuisine.lower()
            ]
        else:
            cuisine_list = [key for key, value in cuisine_details.items()]

        """
            Step 3 : Search restaurants
        """
        response = _zomato.restaurant_search(
            location,
            location_details["latitude"],
            location_details["longitude"],
            cuisine_list,
            location_details["city_id"],
            'city'
        )

        restaurants_found = []

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

        logger.info(
            "calling Zomato /search API with '%s' location and '%s' cuisine",
            location,
            cuisine,
        )
        logger.info(json.dumps(restaurants_found, sort_keys=True, indent=4))


if __name__ == "__main__":
    raise RuntimeError(
        "Calling `zomato.zomato_test` directly is no longer supported. Please use "
        "`action_api_test` to test the APIs "
    )
