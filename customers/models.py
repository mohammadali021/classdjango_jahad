from django.db import models
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    family = models.CharField(max_length=100, verbose_name='نشان')
    age = models.IntegerField( verbose_name='سن')
    job = models.CharField(max_length=100, verbose_name='شغل')
    slug = models.SlugField(default='', null=False, db_index=True, verbose_name='اسلاگ')

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name) + '-' + str(self.family))
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}----{self.family}'
    class Meta:
        verbose_name = 'مشتریان'
        verbose_name_plural = "مشتری"
# Create your models here.
