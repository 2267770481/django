from flask import (Flask, render_template, request, session, redirect, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import pymysql
from .configs import setting

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_pyfile('configs/profile.py')
CSRFProtect(app)
db = SQLAlchemy(app)


@app.errorhandler(404)
def _404(e):
    return render_template('_404.html')


@app.before_request
def before():
    ignore_items = setting.NEED_LOGGED_PATH
    request_path = request.path
    if request_path in ignore_items:
        if session.get('user_id', None) is None:
            # session['isLogged'] = 'Not Logged'
            # return redirect(url_for('user.login'))
            return render_template('login.html', ctx={'tips': '请先登录'})


def create_app():

    from .src import user, index
    app.register_blueprint(user.bp)
    app.register_blueprint(index.bp)
    return app
    app.session_interface