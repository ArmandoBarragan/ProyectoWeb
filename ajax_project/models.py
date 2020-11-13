from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    def __unicode(self):
        return self.name