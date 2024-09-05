from django.db import models


class FormModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(FormModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
# Create your models here.
