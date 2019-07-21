<!-- markdownlint-disable -->
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
* bye
  - utter_bye
  - action_restart

## story_05_location_cuisine_budget_valid_with_email
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

## story_06_location_cuisine_budget_valid_no_email
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
* thank
  - utter_bye
  - action_restart

## story_07_location_cuisine_invalid_retry_with_email
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

## story_08_location_cuisine_invalid_retry_no_email
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

## story_09_cuisine_invalid_retry_deny
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

## story_10_location_out_of_scope_affirm  
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

## story_11_location_out_of_scope_deny
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

## story_17_greet_drop
* greet
  - utter_greet
* bye
  - utter_bye
  - action_restart

## story_18_ask_restaurant_drop
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_19_no_greet_location_invalid_drop
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* bye
  - utter_bye
  - action_restart

## story_20_no_greet_location_invalid_retry_cuisine_drop
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

## story_21_no_greet_location_invalid_retry_cuisine_drop
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

## story_22_no_greet_location_invalid_retry_affirm_drop
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

## story_23_ask_location_drop
* greet
  - utter_greet
* ask_restaurant
  - utter_ask_location
* bye
  - utter_bye
  - action_restart

## story_24_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_out_of_scope
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_25_no_greet_location_retry_out_of_scope
* ask_restaurant
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_26_no_greet_location_invalid_out_of_scope
* ask_restaurant{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## story_27_location_invalid_retry_email_out_of_scope
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
  - utter_bye
  - action_restart

## story_28_ask_location_out_of_scope
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

## story_29_location_invalid_out_of_scope
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
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
  - utter_ask_cuisine
* ask_restaurant{"cuisine":"mexican"}
  - utter_ask_budget
* ask_budget{"budget": "300"}
  - action_restaurant
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_bye
  - action_slot_reset  
  - action_restart

## story_31_location_invalid_retry_email_out_of_scope
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
  - utter_bye
  - action_restart

## story_32_cuisine_location_buget_valid_email_out_of_scope
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
  - utter_bye
  - action_restart

## story_33_no_greet_location_invalid_retry_email_drop
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

## story_34_no_greet_location_invalid_retry_email_drop
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

<!-- start with greet, followed by question -->
## story_35_greet_cuisine_valid_email
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

## story_36_greet_cuisine_valid_no_email
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

## story_37_greet_cuisine_invalid_retry_no_email
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

## story_38_greet_cuisine_invalid_retry_email
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

## story_39_greet_cuisine_valid_location_invalid_retry_email
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

## story_40_greet_cuisine_valid_location_invalid_retry_no_email
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

<!-- start with question -->
## story_41_no_greet_cuisine_valid_email
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

## story_42_no_greet_cuisine_valid_no_email
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

## story_43_no_greet_cuisine_invalid_retry_no_email
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

## story_44_no_greet_cuisine_invalid_retry_email
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

## story_45_no_greet_cuisine_valid_location_invalid_retry_email
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

## story_46_no_greet_cuisine_valid_location_invalid_retry_no_email
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

<!-- cuisine + location, both invalid -->

<!-- greet, followed by question -->
## story_47_greet_cuisine_and_location_invalid_retry_email
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

## story_48_greet_cuisine_and_location_invalid_retry_no_email
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
## story_49_no_greet_cuisine_and_location_invalid_retry_email
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

## story_50_no_greet_cuisine_and_location_invalid_retry_no_email
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

## story_51_greet_out_of_scope
* greet
  - utter_greet
* out_of_scope
  - utter_out_of_scope
  - utter_bye
  - action_restart

<!-- chat-bot not helpful -->
## story_01_location_cuisine_valid_no_email
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

## story_02_location_cuisine_budget_valid_no_email
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
  
## story_03_location_cuisine_invalid_retry_no_email
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

## story_04_greet_cuisine_valid_no_email
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

## story_05_greet_cuisine_invalid_retry_no_email
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

## story_06_greet_cuisine_valid_location_invalid_retry_no_email
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

## story_07_no_greet_cuisine_valid_no_email
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

## story_08_no_greet_cuisine_invalid_retry_no_email
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

## story_09_no_greet_cuisine_valid_location_invalid_retry_no_email
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

## story_10_greet_cuisine_and_location_invalid_retry_no_email
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

<!-- stop conversation with denial-->
## story_01_location_invalid_retry
* ask_restaurant{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## story_02_location_valid_cuisine_invalid_retry
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
<!-- markdownlint-restore -->
