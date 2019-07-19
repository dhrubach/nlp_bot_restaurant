<!-- markdownlint-disable -->
## story_01_location_cuisine_valid
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid"}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_02_location_invalid_retry
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
  - action_slot_reset
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}  
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_03_location_invalid
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset  
  - action_restart

## story_04_cuisine_invalid_retry
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}  
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_05_cuisine_invalid
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset  
  - action_restart

## story_06_location_cuisine_valid_no_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
* bye
  - utter_bye
  - action_restart

## story_07_location_cuisine_budget_valid_with_email
* greet
  - utter_greet
* ask_restaurant{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "701"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_08_location_cuisine_budget_valid_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_bye
  - action_restart

## story_09_location_out_of_scope_affirm  
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}  
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_10_location_out_of_scope_deny
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_11_cuisine_out_of_scope_affirm  
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* out_of_scope
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}  
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_12_cuisine_out_of_scope_deny
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* out_of_scope
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset  
  - action_restart

## story_13_only_cuisine_out_of_scope_affirm  
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_cuisine
* out_of_scope
  - action_slot_reset
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}  
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_14_only_cuisine_out_of_scope_deny
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_cuisine
* out_of_scope
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset  
  - action_restart

<!-- markdownlint-restore -->
