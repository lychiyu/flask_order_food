import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        self.config.from_pyfile('config/base_settings.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile(f'config/{os.environ["ops_config"]}_settings.py')
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=f'{os.getcwd()}/web/templates', root_path=os.getcwd())
manager = Manager(app)
"""
函数模板
"""
from common.libs.url_manager import UrlManager

app.add_template_global(UrlManager.build_url, 'build_url')
app.add_template_global(UrlManager.build_image_url, 'build_image_url')
app.add_template_global(UrlManager.build_static_url, 'build_static_url')
