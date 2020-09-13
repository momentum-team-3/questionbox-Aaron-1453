from django.db import models
from users.models import User
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='questions', null=True)
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    
class Answer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE, max_length=2000)
    answer_text = models.TextField(max_length=2000)
    star = models.IntegerField(default=0)
    def __str__(self):
        return self.answer_text