import os
import logging

from rasa.constants import DEFAULT_DATA_PATH, DEFAULT_MODELS_PATH
from rasa.train import train_nlu

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")


def train_nlu_model():
    train_nlu(
        "config.yml",
        DEFAULT_DATA_PATH,
        DEFAULT_MODELS_PATH,
        fixed_model_name="restaurant-nlu-model",
    )


def clear_model_folder():
    for file_object in os.listdir(DEFAULT_MODELS_PATH):
        file_object_path = os.path.join(DEFAULT_MODELS_PATH, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)


if __name__ == "__main__":
    clear_model_folder()
    train_nlu_model()
