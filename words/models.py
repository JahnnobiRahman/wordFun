import uuid

from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q



class Word(models.Model):
    word_num = models.TextField()
    defi = models.TextField()
    use_in = models.TextField()
    imp =models.IntegerField(default = 1)
    adder = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self):
    
        return self.word_num

    def summary(self):
          return self.defi[:100]


