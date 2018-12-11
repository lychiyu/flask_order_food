from flask import Blueprint, render_template

account_buleprint = Blueprint('account', __name__)


@account_buleprint.route('/index/')
def index():
    return render_template('account/index.html')


@account_buleprint.route('/info/')
def info():
    return render_template('account/info.html')


@account_buleprint.route('/set/')
def set():
    return render_template('account/set.html')
