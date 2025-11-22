from django.db import models

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='technologies/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
