from flask import Blueprint, render_template

# 实例化蓝图
index_blueprint = Blueprint('index', __name__)


@index_blueprint.route("/")
def index():
    return render_template('index/index.html')
