<!-- markdownlint-disable -->
## story_01
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
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
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
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
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_bye
<!-- markdownlint-restore -->
