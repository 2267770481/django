from flask_wtf import FlaskForm
from wtforms.fields import simple
from wtforms import validators, widgets


class AddPneInfoForm(FlaskForm):
    model = simple.StringField(
        label="型号",
        validators=[
            validators.DataRequired(message="型号不能为空"),  # 必填项检查 message 为返回的错误内容
            validators.length(max=20)
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "model"}
    )

    price = simple.StringField(
        label="价格",
        validators=[
            validators.DataRequired(message="价格不能为空"),  # 必填项检查 message 为返回的错误内容
            validators.length(max=20)
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "price"}
    )

    company = simple.StringField(
        label="公司名称",
        validators=[
            validators.DataRequired(message="公司名称不能为空"),  # 必填项检查 message 为返回的错误内容
            validators.length(max=20)
        ],
        widget=widgets.TextInput(),
        render_kw={"class": "company"}
    )

    submit = simple.SubmitField(
        label="提交",
        render_kw={
            "class": "btn",
        },
    )