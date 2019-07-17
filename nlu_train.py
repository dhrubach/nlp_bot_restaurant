import argparse
import os
import logging

from rasa.constants import DEFAULT_DATA_PATH, DEFAULT_MODELS_PATH
from rasa.train import train_nlu
from rasa.cli.shell import shell_nlu


logging.basicConfig(level=logging.INFO)
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
        "-nlu",
        action="store_true",
        help="Run RASA shell to test trained NLU model",
    )

    return parser


def run_nlu_shell() -> None:
    argument = argparse.Namespace()
    argument.model = DEFAULT_MODELS_PATH

    shell_nlu(argument)


def train_nlu_model() -> None:
    train_nlu(
        "config.yml",
        DEFAULT_DATA_PATH,
        DEFAULT_MODELS_PATH,
        fixed_model_name="restaurant-nlu-model",
    )


if __name__ == "__main__":
    parser = create_argument_parser()
    cmdline_arguments = parser.parse_args()
    clear_model_folder()
    train_nlu_model()

    if cmdline_arguments.shell:
        run_nlu_shell()
