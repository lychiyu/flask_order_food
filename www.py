from web.controllers.index import index_blueprint
from web.controllers.user import user_blueprint
from web.controllers.static import static_blueprint
from web.controllers.account import account_buleprint
from web.controllers.stat import stat_blueprint
from web.controllers.food import food_blueprint
from web.controllers.member import member_blueprint
from web.controllers.finance import finance_blueprint
from application import app

# 注册蓝图
app.register_blueprint(index_blueprint, url_prefix="/")
app.register_blueprint(user_blueprint, url_prefix="/user")
app.register_blueprint(static_blueprint, url_prefix="/static")
app.register_blueprint(account_buleprint, url_prefix="/account")
app.register_blueprint(food_blueprint, url_prefix="/food")
app.register_blueprint(stat_blueprint, url_prefix="/stat")
app.register_blueprint(member_blueprint, url_prefix="/member")
app.register_blueprint(finance_blueprint, url_prefix="/finance")
