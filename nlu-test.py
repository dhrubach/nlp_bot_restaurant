from rasa.constants import DEFAULT_DATA_PATH, DEFAULT_MODELS_PATH
from rasa.test import test_nlu

if __name__ == "__main__":
    test_nlu(DEFAULT_MODELS_PATH, DEFAULT_DATA_PATH, {})
