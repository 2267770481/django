from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # login_required 检查登录情况，如果没有登录会跳转到登录页面， 在settings中有LOGIN_URL='xxx' 配置登录页面的路由
    path('', login_required(views.index), name='index'),
]
