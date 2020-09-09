from django.db import models
from users.models import User
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=255)
    
    body = models.TextField(max_length=2000)
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='answers', null=True)
    
    body = models.TextField(max_length=2000)
    def __str__(self):
        return self.title