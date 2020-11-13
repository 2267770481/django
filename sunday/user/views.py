from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_GET
from django.db import transaction
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
import logging
from .forms import Register
from .models import UserInfo

logger = logging.getLogger('django')  # 获取日志器（在settings中有配置）


@transaction.atomic  # 开启事务
def register(request):
    if request.method == "GET":
        form = Register()
        return render(request, 'user/register.html', {'form': form})

    form = Register(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.cleaned_data.pop('repeat_pwd', None)
        form.cleaned_data['password'] = make_password(form.cleaned_data['password'])  # 使用django自带的加密 加密密码

        print(form.cleaned_data)
        try:
            UserInfo.objects.create(**form.cleaned_data)
        except Exception as e:
            logger.error('数据库操作失败')
            # transaction.rollback()    # 不能有这句 有这句会提交上边插入在执行过程中没有出现问题的数据,如果没有异常会自己提交，有异常自己回退
            raise e

        return HttpResponse('register success')
    else:
        return render(request, 'user/register.html', {'form': form})


'''
使用django自带的用户管理模块替换了
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    print(request.POST)
    try:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        pwd = UserInfo.objects.get(username=username).password
        print(pwd)
        if pwd == password:
            request.session['userinfo'] = username
            return redirect('/index')
        else:
            return HttpResponse('用户名或密码错误')
    except Exception as e:
        logger.info(e)
        return HttpResponse('还未注册')
'''


def login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request, user)
        return HttpResponseRedirect('/index')
    else:
        return HttpResponse('用户名或密码错误')


@require_GET  # 只允许get请求
def logout(request):
    auth.logout(request)
    return HttpResponse('logout.')
