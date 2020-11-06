from flask.views import MethodView
from flask import request, session, redirect, url_for, render_template, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from ..user import bp
from ..forms.register import RegisterForm
from ..forms.login import LoginForm
from monday.public.db_util import mysql


@bp.route('/login', methods=['POST', "GET"])
def login():
    if request.method == "GET":
        form = LoginForm()
        return render_template('login.html', form=form, ctx=None)

    form = LoginForm(formdata=request.form)
    if form.validate():
        print(form.data)
        sql = 'select id from db_UserInfo where username=%(username)s and password=%(password)s'
        res = mysql.fetch_one(sql, form.data)
        if res:
            session['user_info'] = {
                'id': res['id'],
                'username': form.data['username']
            }
            current_app.logger.info(f'用户：[{form.data["username"]}]成功登录')
            return redirect(url_for('index.index'))
        return render_template('login.html', form=form, ctx={'tips': '用户名或密码错误'})
    else:
        return render_template('login.html', form=form, ctx=None)


@bp.route('/logout')
def logout():
    current_app.logger.info(f'用户: [{session["user_info"]["id"]}] 退出登录')
    session.pop('user_info', None)
    return 'logout'


@bp.route('/user_list')
def user_list():
    sql = 'select id, username, password, state from db_UserInfo'
    res = mysql.fetch_all(sql)
    print(res)
    return render_template('user_list.html', ctx=res)


class Register(MethodView):

    def get(self):
        # return render_template('register.html')
        form = RegisterForm(data={'gender': 1})  # 默认是1,
        return render_template("register.html", form=form)

    def post(self, *args, **kwargs):
        form = RegisterForm(formdata=request.form)
        if form.validate():  # 判断是否验证成功
            print(form.data)
            sql = 'insert into db_userinfo(username, password, state, mail) values (%(username)s, %(password)s, "00", %(mail)s)'
            mysql.insert(sql, form.data)
            return redirect(url_for('index.index'))
        else:
            print(form.errors)  # 所有的错误信息
            return render_template('register.html', form=form)
