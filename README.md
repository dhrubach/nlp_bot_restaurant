# Restaurant Bot

a restaurant chatbot using open source chat framework [RASA](https://rasa.com/). Integrates with [Zomato API](https://developers.zomato.com/) to fetch restaurant information.

## Repo Information

This repo contains training data and script files necessary to compile and execute this restaurant chatbot. It comprises of the following files:

### Data Files

- **data/nlu/nlu.md** : contains training examples for the NLU model  
- **data/core/stories.md** : contains training stories for the Core model  

### Script Files

- **zomato** : contains Zomato API integration code
  - **zomato_api.py** : contains functions to consume common Zomato APIs like fetch location details, type of cuisines, search for restaurants, etc
  - **zomato_test.py** : contains 3 test functions for Zomato API - location details, cuisine details and restaurant search
- **action_api_test.py** : executes Zomato API test functions from command line
- **actions_server.py** : contains code to start a RASA actions server. This is used to serve RASA custom actions.
- **actions.py** : contains the following custom actions
  - search restaurant
  - validate location
  - validate cuisine
  - send email
  - restart conversation
  - reset slots
- **nlu_test.py** : contains code to test generated NLU models
- **nlu_train.py** : contains code to
  - train a NLU model
  - persist NLU model in 'models' folder
  - run CLI to interact with generated model and validate extracted intents and entities
- **rasa_slack.py** : contains code to integrate with slack channel
- **rasa_train.py** : primary script file to test chatbot from CLI. Contains code to:
  - train both NLU and Core model
  - persist packaged model in 'models' folder
  - start CLI interface to interact with chatbot
    (_RASA action server must be running for this to work_)

### Config Files

- **config.yml** contains model configuration and custom policy
- **credentials.yml** contains authentication token to connect with channels like slack
- **domain.yml** defines chatbot domain like entities, actions, templates, slots  
- **endpoints.yml** contains the webhook configuration for custom action

## Usages

- Train ONLY NLU model and validate

  ```python
  python nlu_train.py --shell
  ```

  This will generate _restaurant-nlu-model.tar.gz_ inside **models** folder and start an interactive shell

- Test generated NLU model (_generated NLU model should be available in 'models' folder prior to test_). 2 options are available:
  - DEFAULT : separate test set is created
  - VALIDATION : uses cross - validation
  
  ```python
  python nlu_test.py --type DEFAULT

  python nlu_test.py --type VALIDATION
  ```

- Run RASA action server ( mandatory step to interact with chatbot) on port **5055**

  ```python
  python actions_server.py
  ```
  