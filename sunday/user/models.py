from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#
'''
    用下面的方法替换l
class UserInfo(models.Model):
    STATE_MAP = (
        ('00', '正常'),
        ('01', '禁止'),
        ('02', '销户'),
    )
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=128)
    state = models.CharField(max_length=2, choices=STATE_MAP, default='00')
    phone = models.CharField(max_length=15, null=True)
    mail = models.CharField(max_length=40, null=True)
    free1 = models.IntegerField(null=True)
    free2 = models.CharField(max_length=20, null=True)
    free3 = models.CharField(max_length=60, null=True)

    class Meta:
        db_table = 'dj_userinfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name
'''


class UserInfo(AbstractUser):
    """
        将django默认的用户信息数据表User替换为自建的UserInfo表
        from django.contrib.auth.models import User    --django默认
    """
    # first_name = None  # 删掉基类中的该字段 不让他在建表的时候生成字段
    # last_name = None  # 删掉基类中的该字段 不让他在建表的时候生成字段

    # username = models.CharField(max_length=40)    # 基类中有这些字段
    # password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15, null=True)
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name='性别', null=True)
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')

    # mail = models.CharField(max_length=40, null=True)
    class Meta:
        db_table = 'dj_UserInfo'
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


