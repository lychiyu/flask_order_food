import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


class Application(Flask):
    def __init__(self, import_name):
        super(Application, self).__init__(import_name)
        self.config.from_pyfile('config/base_settings.py')
        if 'ops_config' in os.environ:
            self.config.from_pyfile(f'config/{os.environ["ops_config"]}_settings.py')
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__)
manager = Manager(app)
