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
  - slot{"search_validity" : "valid"}
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
  - action_slot_reset
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

## story_13_start_question_location_cuisine_budget_valid_no_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid"}
  - utter_ask_details
* deny
  - utter_deny
* thank
  - utter_bye
  - action_restart

## story_14_start_question_location_cuisine_budget_valid_with_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
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

## story_15_greet_drop
* greet
  - utter_greet
* bye
  - utter_bye
  - action_restart

## story_16_ask_restaurant_drop
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_17_no_greet_location_invalid_drop
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* bye
  - utter_bye
  - action_restart

## story_18_no_greet_location_invalid_retry_cuisine_drop
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* bye
  - utter_bye
  - action_restart

## story_19_no_greet_location_invalid_retry_cuisine_drop
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* bye
  - utter_bye
  - action_restart

## story_20_no_greet_location_invalid_retry_affirm_drop
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_21_ask_location_drop
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_22_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_bye
  - action_restart

## story_23_no_greet_location_retry_out_of_scope
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_24_no_greet_location_invalid_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_25_location_invalid_retry_email_out_of_scope
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* out_of_scope
  - utter_bye
  - action_restart

## story_26_with_location_invalid_retry_cuisine_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* out_of_scope
  - utter_bye
  - action_restart

## story_27_ask_location_out_of_scope
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_28_location_invalid_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_29_cuisine_location_valid_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"} 
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* out_of_scope
  - utter_bye
  - action_restart

## story_30_location_invalid_retry_email_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* out_of_scope
  - utter_bye
  - action_slot_reset  
  - action_restart

## story_31_location_invalid_retry_budget_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* out_of_scope
  - utter_bye
  - action_slot_reset
  - action_restart

## story_32_location_invalid_retry_budget_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* out_of_scope
  - utter_bye
  - action_restart

## story_33_location_invalid_retry_email_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* ask_budget{"budget": "700"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* out_of_scope
  - utter_bye
  - action_restart

## story_34_cuisine_location_buget_valid_email_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid"}  
  - utter_ask_details
* out_of_scope
  - utter_bye
  - action_restart

## story_35_no_greet_location_invalid_retry_email_drop
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* bye
  - utter_bye
  - action_restart

## story_36_no_greet_location_invalid_retry_email_drop
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
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
* bye
  - utter_bye
  - action_restart

<!-- markdownlint-restore -->
