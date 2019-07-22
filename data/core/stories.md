<!-- markdownlint-disable -->

<!-- greet, ask restaurant -->
## story_01_location_cuisine_valid_with_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_02_location_invalid_retry_with_email
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
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
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

## story_04_location_cuisine_valid_no_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_05_location_out_of_scope_affirm  
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_06_location_out_of_scope_deny
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

<!-- greet, location + cuisine-->
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
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
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
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_09_location_cuisine_invalid_retry_with_email
* greet
  - utter_greet
* ask_restaurant{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_10_location_cuisine_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_11_cuisine_invalid_retry_deny
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset

<!-- no greet, location + cuisine -->
## story_12_no_greet_location_cuisine_budget_valid_no_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_deny
* thank
  - utter_bye
  - action_restart

## story_13_no_greet_location_cuisine_budget_valid_with_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_14_no_greet_location_cuisine_invalid_retry_no_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_15_no_greet_location_cuisine_invalid_retry_deny
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_16_no_greet_location_cuisine_invalid_retry_with_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

<!-- queries with cuisine only -->

<!-- start with greet, followed by question -->
## story_17_greet_cuisine_valid_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_18_greet_cuisine_valid_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_19_greet_cuisine_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_20_greet_cuisine_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_21_greet_cuisine_valid_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_22_greet_cuisine_valid_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- no greet, start with cuisine -->
## story_23_no_greet_cuisine_valid_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_24_no_greet_cuisine_valid_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_25_no_greet_cuisine_invalid_retry_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_26_no_greet_cuisine_invalid_retry_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_27_no_greet_cuisine_valid_location_invalid_retry_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_28_no_greet_cuisine_valid_location_invalid_retry_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- queries with location only -->

<!-- start with greet, followed by question -->
## story_29_greet_location_valid_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_30_greet_location_valid_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_31_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_32_greet_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

<!-- no greet, start with location -->
## story_33_no_greet_location_cuisine_budget_valid_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_34_no_greet_location_cuisine_budget_valid_no_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_35_no_greet_location_invalid_retry_no_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_36_no_greet_location_invalid_retry_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

<!-- cuisine + location, both invalid -->

<!-- greet, followed by question -->
## story_37_greet_cuisine_and_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity": "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_38_greet_cuisine_and_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- no greet -->
## story_39_no_greet_cuisine_and_location_invalid_retry_email
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_40_no_greet_cuisine_and_location_invalid_retry_no_email
* ask_restaurant{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- invalid search -->
## story_41_location_cuisine_valid_search_invalid
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_42_location_invalid_retry_search_invalid
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
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_43_location_cuisine_budget_valid_search_invalid
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
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## story_44_location_cuisine_invalid_retry_search_invalid
* greet
  - utter_greet
* ask_restaurant{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "701"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_45_no_greet_location_cuisine_budget_valid_search_invalid
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_46_no_greet_location_cuisine_invalid_retry_search_invalid
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## story_47_greet_cuisine_valid_search_invalid
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_48_greet_cuisine_invalid_retry_search_invalid
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_49_greet_cuisine_valid_location_invalid_retry_search_invalid
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## story_50_no_greet_cuisine_valid_search_invalid
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_51_no_greet_cuisine_invalid_retry_search_invalid
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_52_no_greet_cuisine_valid_location_invalid_retry_search_invalid
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_53_greet_location_valid_search_invalid
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_54_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_55_no_greet_location_cuisine_budget_valid_search_invalid
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_56_no_greet_location_invalid_retry_search_invalid
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_57_greet_cuisine_and_location_invalid_retry_search_invalid
* greet
  - utter_greet
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## story_58_no_greet_cuisine_and_location_invalid_retry_search_invalid
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

<!-- chat-bot not helpful -->
## story_59_location_cuisine_valid_no_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_60_location_cuisine_budget_valid_no_email
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
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart
  
## story_61_location_cuisine_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_62_greet_cuisine_valid_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_63_greet_cuisine_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_64_greet_cuisine_valid_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_65_no_greet_cuisine_valid_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_66_no_greet_cuisine_invalid_retry_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_67_no_greet_cuisine_valid_location_invalid_retry_no_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_68_greet_cuisine_and_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_69_greet_location_valid_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_70_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_71_no_greet_location_valid_no_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "indian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_72_no_greet_location_invalid_retry_no_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

<!-- stop conversation with denial-->
## story_73_location_invalid_retry
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_74_location_valid_cuisine_invalid_retry
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_75_no_greet_location_invalid_retry
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_76_greet_location_invalid_retry
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_77_no_greet_cuisine_invalid_retry
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_78_no_greet_cuisine_invalid_retry
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

<!-- drop out of conversation with bye-->
## story_79_greet_drop
* greet
  - utter_greet
* bye
  - utter_bye
  - action_restart

## story_80_ask_restaurant_drop
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_81_no_greet_location_invalid_drop
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* bye
  - utter_bye
  - action_restart

## story_82_no_greet_location_invalid_retry_cuisine_drop
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* bye
  - utter_bye
  - action_restart

## story_83_no_greet_location_invalid_retry_cuisine_drop
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

## story_84_no_greet_location_invalid_retry_affirm_drop
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

## story_85_ask_location_drop
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_86_no_greet_location_invalid_retry_email_drop
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* bye
  - utter_bye
  - action_restart

## story_87_no_greet_location_invalid_retry_email_drop
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* bye
  - utter_bye
  - action_restart

<!-- handling out of scope responses -->
## story_88_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_out_of_scope
  - utter_bye
  - action_restart

## story_89_no_greet_location_retry_out_of_scope
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_90_no_greet_location_invalid_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_91_location_invalid_retry_email_out_of_scope
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## story_92_location_invalid_retry_email_out_of_scope
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_93_location_invalid_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_94_location_invalid_retry_email_out_of_scope
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
  - utter_ask_cuisine
* ask_restaurant{"cuisine":"mexican"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_95_location_invalid_retry_email_out_of_scope
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
  - utter_ask_cuisine
* ask_restaurant{"cuisine":"mexican"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## story_96_location_invalid_retry_email_out_of_scope
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
  - utter_ask_budget
* ask_budget{"budget": "700"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_97_location_invalid_retry_email_out_of_scope
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
  - utter_ask_budget
* ask_budget{"budget": "700"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## story_98_cuisine_location_buget_valid_email_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_99_cuisine_location_buget_valid_email_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## story_100_location_cuisine_budget_valid_with_email
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
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_101_no_greet_location_cuisine_budget_valid_with_email
* ask_restaurant{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget":"701"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_102_location_cuisine_valid_with_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_103_location_out_of_scope_affirm  
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
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_104_greet_cuisine_and_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity": "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_105_location_invalid_retry_with_email
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "299"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_106_greet_cuisine_valid_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_bye
  - action_restart

## story_107_greet_cuisine_valid_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_happy
  - utter_bye
  - action_restart

## story_108_no_greet_cuisine_valid_location_invalid_retry_email
* ask_restaurant{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_109_greet_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## story_110_greet_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_111_no_greet_location_invalid_retry_no_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_happy
  - utter_bye
  - action_restart

## story_112_no_greet_location_invalid_retry_email
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "Chinese"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thank
  - utter_happy
  - utter_bye
  - action_restart

## story_113_greet_cuisine_and_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "Vizag", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* ask_restaurant{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## story_114_no_greet_cuisine_and_location_invalid_retry_email
* ask_restaurant{"location": "Delhi", "cuisine": "french"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* ask_restaurant{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* ask_restaurant{"cuisine": "french"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_115_greet_location_cuisine_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_116_no_greet_location_cuisine_invalid_retry_no_email
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_117_greet_cuisine_location_invalid_retry_no_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_118_no_greet_cuisine_location_invalid_retry_no_email
* ask_restaurant{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_119_greet_location_cuisine_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_120_no_greet_location_cuisine_invalid_retry_email
* ask_restaurant{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* ask_restaurant{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_121_greet_cuisine_location_invalid_retry_email
* greet
  - utter_greet
* ask_restaurant{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## story_122_no_greet_cuisine_location_invalid_retry_email
* ask_restaurant{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* ask_restaurant{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

<!-- markdownlint-restore -->
