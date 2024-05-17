import datetime
from django.db import models
from django.utils import timezone

## This class is a model for a question. It has a question_text and a publication date.
class Question(models.Model):

    def __str__(self):
        return self.question_text
    
    ## This method returns True if the question was published within the last day.
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

## This class is a model for a choice. It has a question, a choice_text, and a number of votes.
class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)