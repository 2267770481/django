from flask_wtf import FlaskForm
from wtforms.fields import simple
from wtforms import validators, widgets


class AddCmpInfoForm(FlaskForm):
    name = simple.StringField(
        label="公司名称",
        validators=[
            validators.DataRequired(message="用户名不能为空"),  # 必填项检查 message 为返回的错误内容
            validators.length(max=20)
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "name"}
    )

    location = simple.StringField(
        label="公司地址",
        validators=[
            validators.DataRequired(message="用户名不能为空"),  # 必填项检查 message 为返回的错误内容
            validators.length(max=20)
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "location"}
    )

    submit = simple.SubmitField(
        label="提交",
        render_kw={
            "class": "btn",
        },
    )