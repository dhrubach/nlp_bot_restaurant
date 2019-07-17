# Restaurant Bot

a restaurant chatbot using open source chat framework [RASA](https://rasa.com/). Integrates with [Zomato API](https://developers.zomato.com/) to fetch restaurant information.

## Repo Information

This repo contains training data and main files needed to compile and execute this restaurant chatbot. It comprises of the following files:

- **data/nlu/nlu.md** : contains training examples for the NLU model  
- **data/core/stories.md** : contains training stories for the Core model  
- **zomato** : contains Zomato API integration code
  - **zomato_api.py** : contains functions to consume common Zomato APIs like fetch location details, type of cuisines, search for restaurants, etc
  - **zomato_test.py** : contains 3 test functions for Zomato API - location details, cuisine details and restaurant search
- **action_api_test.py** : executes Zomato API test functions from command line
- **config.yml** contains model configuration and custom policy
- **domain.yml** contains the domain of the chatbot  
- **endpoints.yml** contains the webhook configuration for custom action  

## Usage
