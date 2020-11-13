from django import forms
import re


class Register(forms.Form):
    username = forms.CharField(
        label='用户名：',
        required=True,
        max_length=20,
        widget=forms.widgets.TextInput(attrs={'class': 'username'}),
        error_messages={
            'required': '用户名不能为空',
            'max_length': '长度超长'
        },
    )
    password = forms.CharField(
        label='密码：',
        required=True,
        min_length=6,
        max_length=20,
        widget=forms.widgets.PasswordInput(attrs={'class': 'password'}),
        error_messages={
            'required': '密码不能为空',
            'min_length': '密码长度不够',
            'max_length': '长度超长'
        },
    )
    repeat_pwd = forms.CharField(
        label='重复密码：',
        required=True,
        widget=forms.widgets.PasswordInput(attrs={'class': 'repeat_pwd'}),
    )

    phone = forms.CharField(
        label='手机号码：',
        widget=forms.widgets.TextInput(attrs={'class': 'phone'})
    )

    email = forms.EmailField(
        label='电子邮箱：',
        widget=forms.widgets.EmailInput(attrs={'class': 'mail'})
    )

    def clean_repeat_pwd(self):  # 自定义校验规则 clean_ 后边跟要校验的字段名
        repeat_pwd = self.cleaned_data.get('repeat_pwd', None)
        if repeat_pwd != self.cleaned_data.get('password', None):
            raise forms.ValidationError("两次输入的密码不一致")
        return repeat_pwd

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', None)
        prog = re.compile(r'^1[356789]\d{9}$')
        res = prog.match(phone)
        if not res:
            raise forms.ValidationError('电话号码不正确')
        return phone
