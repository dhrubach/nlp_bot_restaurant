import logging

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer

from rasa.constants import DEFAULT_ACTIONS_PATH
from rasa_sdk.constants import DEFAULT_SERVER_PORT
from rasa_sdk.endpoint import endpoint_app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")


def run_action_server() -> None:
    edp_app = endpoint_app(cors_origins="*", action_package_name=DEFAULT_ACTIONS_PATH)

    http_server = WSGIServer(("0.0.0.0", DEFAULT_SERVER_PORT), edp_app)

    http_server.start()
    logger.info("Action endpoint is up and running. on {}".format(http_server.address))

    http_server.serve_forever()


if __name__ == "__main__":
    logger.info("Starting action endpoint server...")
    run_action_server()
