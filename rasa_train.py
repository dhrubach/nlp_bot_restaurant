import argparse
import logging
import os

from rasa.cli.run import run
from rasa.constants import (
    DEFAULT_ACTIONS_PATH,
    DEFAULT_DATA_PATH,
    DEFAULT_DOMAIN_PATH,
    DEFAULT_MODELS_PATH,
    DEFAULT_CONFIG_PATH,
)
from rasa.train import train
from rasa.utils.io import configure_colored_logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("__name__")


def clear_model_folder() -> None:
    for file_object in os.listdir(DEFAULT_MODELS_PATH):
        file_object_path = os.path.join(DEFAULT_MODELS_PATH, file_object)
        if os.path.isfile(file_object_path):
            os.unlink(file_object_path)


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-sh",
        "--shell",
        action="store_true",
        help="Run RASA shell to test trained RASA model",
    )

    return parser


def run_rasa_shell() -> None:
    argument = argparse.Namespace()
    argument.model = DEFAULT_MODELS_PATH
    argument.connector = "cmdline"
    argument.enable_api = False
    argument.endpoints = None
    argument.credentials = None
    argument.remote_storage = None

    run(argument)


def train_nlu_core_model() -> None:
    train(
        domain=DEFAULT_DOMAIN_PATH,
        config=DEFAULT_CONFIG_PATH,
        training_files=DEFAULT_DATA_PATH,
        fixed_model_name="restaurant_rasa_model",
        force_training=False,
    )


if __name__ == "__main__":
    configure_colored_logging(loglevel="ERROR")

    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()

    train_nlu_core_model()

    if cmdline_arguments.shell:
        run_rasa_shell()
