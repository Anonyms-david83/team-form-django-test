from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    score = models.FloatField()

    def __str__(self):
        return self.fname
