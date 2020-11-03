from flask import (Flask, render_template, request, session, redirect, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_session import Session
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
    '''
        将session存储到redis中
        1.配置
            SESSION_TYPE = 'redis'
            SESSION_REDIS = Redis(host='localhost', password=12345)
        2.注册
            from flask_session import Session
            Session(app)
    '''
    Session(app)  # 将session存到redis中（配置文件中有关于redis的相关配置）

    from .src import user, index
    app.register_blueprint(user.bp)
    app.register_blueprint(index.bp)
    return app
