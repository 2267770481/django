from flask.views import MethodView
from flask import request, session, redirect, url_for, render_template
from ..user import bp
from monday.modles import SqlHelper
from ..forms.register import RegisterForm
from monday.public.db_util import mysql


@bp.route('/login', methods=['POST', "GET"])
def login():
    if request.method == "GET":
        return render_template('login.html', ctx=None)

    username = request.form.get('username', None)
    password = request.form.get('password', None)

    sql = 'select id from db_UserInfo where username=:username and password=:password'
    args = {
        'username': username,
        'password': password
    }
    res = SqlHelper.fetch_one(sql, args)
    if res:
        session['user_id'] = res[0]
        print(res, res[0])
        return redirect(url_for('index.index'))
    else:
        return render_template('login.html', ctx={'tips': '登录失败'})


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return 'logout'


@bp.route('/test', methods=["POST", "GET"])
def test():
    if request.method == "GET":
        form = RegisterForm(data={'gender': 1})  # 默认是1,
        return render_template("register.html", form=form)
    else:
        form = RegisterForm(formdata=request.form)
        if form.validate():  # 判断是否验证成功
            print('用户提交数据通过格式验证，提交的值为：', form.data)  # 所有的正确信息
            return render_template()
        else:
            print(form.errors)  # 所有的错误信息
        return render_template('register.html', form=form)


@bp.route('/user_list')
def user_list():
    sql = 'select id, username, state from db_UserInfo'
    res = SqlHelper.fetch_all(sql)
    print(res)
    # return 'list'
    return render_template('user_list.html', ctx=res)


class Logged(MethodView):

    def get(self):
        # return render_template('register.html')
        form = RegisterForm(data={'gender': 1})  # 默认是1,
        return render_template("register.html", form=form)

    def post(self, *args, **kwargs):
        # username = request.form.get('username', None)
        # password = request.form.get('password', None)
        #
        # if not username or not password:
        #     return redirect(url_for('index.tips', tips='用户名或密码为空'))
        # print(username, password)

        form = RegisterForm(formdata=request.form)
        if form.validate():  # 判断是否验证成功
            print(form.data)

            sql = 'insert into db_userinfo(username, password, state, mail) values (%(username)s, %(password)s, "00", %(mail)s)'
            mysql.insert(sql, form.data)
            return redirect(url_for('index.index'))
        else:
            print(form.errors)  # 所有的错误信息
            return render_template('register.html', form=form)

    @staticmethod
    def _handle(self, username, password):
        sql = """
            insert into db_UserInfo(username, password,state) values(:username, :password, '00')
        """
        args = {'username': username, 'password': password}
        SqlHelper.insert(sql, args)
