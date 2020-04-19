from django.db import models


# Create your models here.
class InputData(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField

    def extract(self):
        self.save()

    def __str__(self):
        return self.title
