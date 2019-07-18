<!-- markdownlint-disable -->
## story_01
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid  
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - action_restaurant
  - utter_ask_details  
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye

## story_02
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid  
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - action_restaurant
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
* bye
  - utter_bye
  
## story_03
* greet
  - utter_greet
* ask_restaurant{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid  
  - action_restaurant
  - utter_ask_budget
* ask_budget{"budget": "300 to 700"}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye

## story_04
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid  
  - action_restaurant
  - utter_ask_budget
* ask_budget{"budget": "300 to 700"}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_bye
<!-- markdownlint-restore -->
