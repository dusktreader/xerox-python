from http import HTTPStatus

from flask import Blueprint

api = Blueprint("health", __name__)


@api.route("", methods=["GET"])
def fetch_health():
    return ("", HTTPStatus.NO_CONTENT)
