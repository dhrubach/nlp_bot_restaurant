"""
    Test ZOMATO developer API endpoints from CLI

    API : /locations
    CMD :  python action_api_test.py --type LOCATION -l seattle
    OUTPUT : 
        {
            "city_id": 279,
            "city_name": "Seattle",
            "country_id": 216,
            "country_name": "United States",
            "entity_id": 279,
            "entity_type": "city",
            "latitude": 47.60577,
            "longitude": -122.329437,
            "title": "Seattle, Washington State"
        }

    API : /cuisines
    CMD : python action_api_test.py --type CUISINE --location bangalore
    OUTPUT :
        {
            "1": "American",
            "25": "Chinese",
            "50": "North Indian",
            "55": "Italian",
            "73": "Mexican",
            "85": "South Indian"
        }

    API : /search
    CMD : python action_api_test.py --type SEARCH --location new york --cuisine mexican
    OUTPUT :
        [
            {
                "address": "32 Spring Street, New York 10012",
                "avg_cost_for_2": 50,
                "name": "Lombardi's Pizza",
                "rating": "4.9"
            },
            {
                "address": "205 East Houston Street, New York 10002",
                "avg_cost_for_2": 30,
                "name": "Katz's Delicatessen",
                "rating": "4.9"
            },
            {
                "address": "179 E Houston Street, New York 10002",
                "avg_cost_for_2": 25,
                "name": "Russ & Daughters",
                "rating": "4.9"
            },
            {
                "address": "65 4th Avenue, New York 10003",
                "avg_cost_for_2": 40,
                "name": "Ippudo",
                "rating": "4.9"
            },
            {
                "address": "Madison Square Park, 23rd & Madison, New York 10010",
                "avg_cost_for_2": 30,
                "name": "Shake Shack",
                "rating": "4.9"
            }
        ]

"""
import argparse
import sys

from zomato.zomato_test import (
    test_cuisine_search,
    test_location_search,
    test_restaurant_search,
)


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--type",
        required=True,
        help="""LOCATION - to test /locations API
                CUISINE - to test /cuisines API 
                SEARCH - to test /search API """,
    )

    parser.add_argument(
        "-l",
        "--location",
        nargs="*",
        help="name of the city where you want to conduct your search in",
    )

    parser.add_argument("-c", "--cuisine", help="list of cuisines available in a city")

    return parser


if __name__ == "__main__":
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()

    test_type = (
        cmdline_arguments.type if cmdline_arguments.type is not None else "SEARCH"
    )
    location = (
        cmdline_arguments.location
        if cmdline_arguments.location is not None
        else "bangalore"
    )
    cuisine = (
        cmdline_arguments.cuisine
        if cmdline_arguments.cuisine is not None
        else "chinese"
    )

    if test_type == "LOCATION":
        test_location_search(location=location)
    elif test_type == "CUISINE":
        test_cuisine_search(location=location)
    else:
        test_restaurant_search(location=location, cuisine=cuisine)
