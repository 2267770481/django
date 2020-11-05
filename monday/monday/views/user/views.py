from flask.views import MethodView
from flask import request, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from ..user import bp
from monday.modles import SqlHelper
from ..forms.register import RegisterForm
from ..forms.login import LoginForm
from monday.public.db_util import mysql
from monday import logger as log


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
            log.info(f'用户：[{form.data["username"]}]成功登录')
            return redirect(url_for('index.index'))
        return render_template('login.html', form=form, ctx={'tips': '用户名或密码错误'})
    else:
        return render_template('login.html', form=form, ctx=None)


@bp.route('/logout')
def logout():
    log.info(f'用户: [{session["user_info"]["id"]}] 退出登录')
    session.pop('user_info', None)
    return 'logout'


@bp.route('/test', methods=["POST", "GET"])
def test():
    if request.method == "GET":
        form = LoginForm()
        return render_template("login.html", form=form, ctx=None)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():  # 判断是否验证成功
            print('用户提交数据通过格式验证，提交的值为：', form.data)  # 所有的正确信息
            sql = 'insert into db_userinfo(sdaas)'
            mysql.insert(sql)
            return render_template('login.html', form=form, ctx={'tips': '用户名或密码错误'})
        else:
            print(form.errors)  # 所有的错误信息
            return render_template("login.html", form=form, ctx=None)


@bp.route('/user_list')
def user_list():
    sql = 'select id, username, password, state from db_UserInfo'
    res = SqlHelper.fetch_all(sql)
    print(res)
    # return 'list'
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
