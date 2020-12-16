from django.db import models

class feedbackdata(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(null=True)
    feedback=models.CharField(max_length=100)

# Create your models here.
