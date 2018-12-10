from flask import Blueprint

# 实例化蓝图
index_blueprint = Blueprint('index', __name__)


@index_blueprint.route("/")
def index():
    return "hello world"
