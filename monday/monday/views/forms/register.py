"""
    注册页面表单生成以及数据检查
"""

from wtforms import Form, widgets
from wtforms.fields import core, simple, html5
from wtforms import validators
from flask_wtf import FlaskForm
from email_validator import validate_email, EmailNotValidError


class RegisterForm(FlaskForm):
    # csrf_token = CSRFTokenField(
    #     # default=generate_csrf
    #     # default=generate_csrf_token()
    # )

    username = simple.StringField(
        label="用户名",
        validators=[
            validators.DataRequired(message="用户名不能为空")  # 必填项检查 message 为返回的错误内容
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "form-control"},
        default="wd"
    )
    password = simple.PasswordField(
        label="密码",
        validators=[
            validators.DataRequired(message="密码不能为空"),
            validators.length(6, 10, message='密码长度为6~10位'),
            # Regexp(r'')   # 写正则
        ]
    )
    pwd_confim = simple.PasswordField(
        label="重复密码",
        validators=[
            validators.DataRequired(message='重复密码不能为空.'),
            validators.EqualTo('password', message="两次密码不一致")  # 相等校验
        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    mail = html5.EmailField(  # 注意这里用的是html5.EmailField
        label='邮箱',
        validators=[
            validators.DataRequired(message='邮箱不能为空.'),
            validators.Email(message='邮箱格式错误')
        ],
        widget=widgets.TextInput(input_type='email'),
        render_kw={'class': 'form-control'}
    )

    gender = core.RadioField(
        label="性别",
        choices=(
            (1, "男"),
            (1, "女"),
        ),
        coerce=int  # 限制是int类型的
    )
    city = core.SelectField(
        label="城市",
        choices=(
            ("bj", "北京"),
            ("sh", "上海"),
        )
    )
    hobby = core.SelectMultipleField(
        label='爱好',
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        coerce=int
    )
    favor = core.SelectMultipleField(
        label="喜好",
        choices=(
            (1, '篮球'),
            (2, '足球'),
        ),
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
        coerce=int,
        default=[1, 2]
    )

    # submit = simple.SubmitField(
    #     label="提交",
    #     render_kw={
    #         "class": "btn btn-primary btn-block",
    #     },
    # )

    def __init__(self, *args, **kwargs):  # 动态更行字段的值（可以从数据库中查到数据并赋值）
        '''重写__init__方法'''
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.favor.choices = ((1, '篮球'), (2, '足球'), (3, '羽毛球'))  # 把RegisterForm这个类里面的favor重新赋值，实现动态改变复选框中的选项

    # def validate_pwd_confim(self, field):
    #     '''
    #     钩子函数 以 validate 开头 后面跟要自定义的字段
    #     这个是自定义pwd_confim字段规则，检查与pwd字段是否一致
    #     :param field:
    #     :return:
    #     '''
    #     # 最开始初始化时，self.data中已经有所有的值
    #     if field.data != self.data['password']:
    #         # raise validators.ValidationError("密码不一致") # 继续后续验证
    #         raise validators.StopValidation("密码不一致")  # 不再继续后续验证
