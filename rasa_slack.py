import logging

from rasa.constants import DEFAULT_MODELS_PATH
from rasa.core.run import serve_application

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")

def start_slack_connector() -> None:
    serve_application(
        model_path=DEFAULT_MODELS_PATH,
        channel="slack",
        port="5004",
        credentials="credentials.yml",
    )

if __name__ == "__main__":
    logger.info("Initiating slack connection...")

    start_slack_connector()



