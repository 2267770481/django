from flask.views import MethodView
from flask import request, session, redirect, url_for, render_template
from dev.configs import setting
from dev import db
from ..user import bp
from dev.modles import SqlHelper


@bp.route('/login')
def login():
    ctx = {}
    if session.get('isLogged', None):
        session.pop('isLogged', None)
        ctx.update({'logged_tips': setting.LOGGED_TIPS})
    return render_template('login.html', ctx=ctx)


@bp.route('/logup')
def logup():
    # sql = 'insert into db_userinfo(username, password, state) values (:a, :b, "01")'
    # sql = 'select id, username from db_userinfo where username=:username'
    sql = 'update db_userinfo set username = :username where id=:id'
    args = {
        'username': 'luoxiang',
        'id': '1123'
    }
    res = SqlHelper.update(sql, args)
    print(res)
    return render_template('logup.html')


@bp.route('/logout')
def logout():
    session.pop('logged_info', None)
    return 'logout'


class Logged(MethodView):
    def post(self, *args, **kwargs):
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        if not username or not password:
            return redirect(url_for('index.tips', tips='用户名或密码为空'))
        print(username, password)

        self._handle(username, password)
        session['logged_info'] = username

        return redirect(url_for('index.index'))

    def _handle(self, username, password):
        sql = """
            insert into db_UserInfo(username, password,state) values(:username, :password, '00')
        """
        args = {'username': username, 'password': password}
        SqlHelper.insert(sql, args)
