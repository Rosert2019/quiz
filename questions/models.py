from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=500)
    choose_1 = models.CharField(max_length=150,null=True)
    choose_2 = models.CharField(max_length=150,null=True)
    choose_3 = models.CharField(max_length=150,null=True)
    choose_4 = models.CharField(max_length=150,null=True)
    answer = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.question
