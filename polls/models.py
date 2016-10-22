from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    #a character field like a string with length <= 200 chars
    question_text = models.CharField(max_length=200)
    # a date field to represent when it was published
    pub_date = models.DateTimeField('date published')

    #pretty printing toString method
    def __str__(self):
       return self.question_text

class Choice(models.Model):
    #This stores a foreign key (the identifier) of a question model to which this choice belongs
    #The on_delete/CASCADE part tells the database to delete this coice if the question is deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #pretty printing toString method
    def __str__(self):
        return self.choice_text
