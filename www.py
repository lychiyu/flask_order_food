from web.controllers.index import index_blueprint
from application import app

# 注册蓝图
app.register_blueprint(index_blueprint, url_prefix="/")
