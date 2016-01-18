from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    phone=models.CharField(max_length=15)
    addr=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
