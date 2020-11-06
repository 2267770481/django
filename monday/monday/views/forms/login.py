from wtforms import Form, widgets
from wtforms.fields import core, simple, html5
from wtforms import validators
from flask_wtf import FlaskForm
from email_validator import validate_email, EmailNotValidError


class LoginForm(FlaskForm):
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
    submit = simple.SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-primary btn-block",
        },
    )