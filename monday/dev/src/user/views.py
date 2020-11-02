from flask.views import MethodView
from flask import request, session, redirect, url_for, render_template
from dev.configs import setting
from ..user import bp


@bp.route('/login')
def login():
    ctx = {}
    if session.get('isLogged', None):
        session.pop('isLogged', None)
        ctx.update({'logged_tips': setting.LOGGED_TIPS})
    return render_template('login.html', ctx=ctx)


@bp.route('/logup')
def logup():
    return render_template('logup.html')


@bp.route('/logout')
def logout():
    session.pop('logged_info', None)
    return 'logout'


class Logged(MethodView):
    def post(self, *args, **kwargs):
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        print(username, password)

        session['logged_info'] = username

        return redirect(url_for('index'))
