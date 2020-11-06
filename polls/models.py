
import datetime

from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

# class Diary(models.Model):
#     """日記モデル"""

#     user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
#     title = models.CharField(verbose_name='タイトル', max_length=40)
#     content = models.TextField(verbose_name='本文', blank=True, null=True)
#     # photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
#     # photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
#     # photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
#     created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
#     updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

#     class Meta:
#         verbose_name_plural = 'Diary'

#     def __str__(self):
#         return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    """
    モデルを変更する (models.py の中の)
    これらの変更のためのマイグレーションを作成するために python manage.py makemigrations を実行します。
    データベースにこれらの変更を適用するために python manage.py migrate を実行します。
    """


"""
http://localhost:8000/polls/ 
"""