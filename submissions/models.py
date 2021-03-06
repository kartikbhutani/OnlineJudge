from django.db import models
from django.contrib.auth.models import User
from problems.models import Problem
from utils.models import CodeLang

from utils.vars import JUDGE_STATUS
from django.db.models.signals import post_save

from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class Submission(models.Model):
    """基本信息"""
    # 运行编号
    id = models.AutoField('运行编号', primary_key=True)
    # 提交用户
    author = models.ForeignKey(
        User, models.SET_NULL, null=True,
        related_name='submissions'
    )
    # 题目
    problem = models.ForeignKey(
        Problem, models.SET_NULL, null=True,
        related_name='problem'
    )
    # 提交时间
    submit_time = models.DateTimeField('提交时间', auto_now_add=True)

    """判题数据"""
    # 状态
    status = models.IntegerField('判题状态', choices=JUDGE_STATUS, default=-1)
    # 使用内存
    exec_memory = models.IntegerField('使用内存', default=0)
    # 使用时间
    exec_time = models.IntegerField('使用时间', default=0)

    """其它信息"""
    # 语言
    language = models.ForeignKey(CodeLang)
    # 代码
    source_code = models.TextField('源代码', blank=True)
    highlighted = models.TextField('高亮源代码', blank=True)
    # 公开代码
    public = models.BooleanField('公开代码', default=False)
    # 备注
    notes = models.CharField('备注', max_length=200, blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = '提交记录'
        verbose_name_plural = '提交记录'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language.name)
        formatter = HtmlFormatter(style='friendly', linenos=True, full=True)
        self.highlighted = highlight(self.source_code, lexer, formatter)
        super(Submission, self).save(*args, **kwargs)


# 创建Submission时自动判题
def judge_submission(sender, instance, created, **kwargs):
    if created:
        from random import choice
        result = choice(JUDGE_STATUS)
        print('=' * 20, 'Judge: ', result[1], '=' * 20)
        instance.status = result[0]
        print('=' * 20, 'Judge: ', result[1], '=' * 20)
        instance.save()

post_save.connect(judge_submission, sender=Submission)
