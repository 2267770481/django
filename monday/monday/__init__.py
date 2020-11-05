from flask import (Flask, render_template, request, session, redirect, url_for)
from flask_session import Session
import pymysql
from .configs import setting
from monday.views.forms.login import LoginForm
from .public.log_util import logger_init

pymysql.install_as_MySQLdb()

logger = logger_init(path=setting.LOG_PATH, debug=True)  # 日志模块初始化


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('configs/profile.py')
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

    @app.errorhandler(404)
    def _404(e):
        return render_template('_404.html')

    @app.errorhandler(500)
    def _500(e):
        return '服务器出错了'

    @app.before_request
    def before():
        '''登陆检查'''
        ignore_items = setting.NEED_LOGGED_PATH
        request_path = request.path
        if request_path in ignore_items:
            if session.get('user_info', None) is None:
                form = LoginForm()
                return render_template('login.html', form=form, ctx={'tips': '请先登录'})

    from .views import user, index
    app.register_blueprint(user.bp)
    app.register_blueprint(index.bp)
    return app
