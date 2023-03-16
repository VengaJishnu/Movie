from django.db import models


# Create your models here.

class cinema(models.Model):  # models.Model is a common code for creating table
    name1 = models.CharField(max_length=230)
    budget2 = models.IntegerField()
    desc3 = models.TextField()
    img4 = models.ImageField(upload_to='media')
    def __str__(self):
        return self.name1