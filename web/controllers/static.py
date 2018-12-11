from flask import Blueprint, send_from_directory
from application import app

static_blueprint = Blueprint('static', __name__)


@static_blueprint.route("/<path:filename>")
def index(filename):
    return send_from_directory(app.root_path + "/web/static/", filename)
