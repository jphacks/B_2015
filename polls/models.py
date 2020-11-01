
import datetime

from django.db import models
from django.utils import timezone

class InputForm(models.Model):
    name = models.CharField()
    age = models.IntegerFiels();
    comment = models.TextField()

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