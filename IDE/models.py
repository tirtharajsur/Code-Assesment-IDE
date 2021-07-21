from django.db import models


class Questions(models.Model):
    _id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=120)
    difficulty_level = models.CharField(
        max_length=20, choices=[('EASY', 'easy'), ('DIFFICULT', 'difficult')], default='EASY')

    def __str__(self):
        return self.question
