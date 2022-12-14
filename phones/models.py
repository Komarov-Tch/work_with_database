from autoslug import AutoSlugField
from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateTimeField()
    lte_exsist = models.BooleanField()
    slug = AutoSlugField(populate_from='name')

    def __str__(self):
        return self.name
