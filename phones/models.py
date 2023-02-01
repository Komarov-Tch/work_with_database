from django.db import models
from autoslug import AutoSlugField

class Phone(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name')
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.CharField(max_length=10)
    lte_exists = models.CharField(max_length=5)


