from django.db import models
import datetime


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=120, verbose_name='问题描述')
    date = models.DateTimeField(verbose_name='发布时间')

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'dj_questions'
        verbose_name = '问题库'
        verbose_name_plural = verbose_name

    def isNow(self):
        """是否当天发布"""
        now = datetime.datetime.now()
        if now - datetime.timedelta(1) < self.date < now + datetime.timedelta(1):
            return True
        return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外键 与Question中的主键 id相关联
    choice_text = models.CharField(max_length=120, verbose_name='选择项描述')
    votes = models.IntegerField(default=0, verbose_name='票数')

    def __str__(self):
        return self.choice_text

    class Meta:
        db_table = 'dj_choice'
        verbose_name = '选项库'
        verbose_name_plural = verbose_name
