from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


class ProductInfo(models.Model):
    color = models.CharField(max_length=100, verbose_name="رنگ محصول")
    size = models.CharField(max_length=100, verbose_name='سایز محصول')

    # slug = models.SlugField(default='', null=False, db_index=True, verbose_name='اسلاگ')

    def __str__(self):
        return f'{self.color}....{self.size}'

    #
    def save(self, *args, **kwargs):
        self.slug = slugify(self.color)

    class Meta:
        verbose_name = "اطلاعات تکمیلی"
        verbose_name_plural = "لیست اطلاعات تکمیلی"


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(default='', null=False, db_index=True, verbose_name='اسلاگ')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = verbose_name


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام موبایل')

    category = models.ForeignKey(ProductCategory, null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='category_product', verbose_name='دسته بندی ')
    info = models.OneToOneField(ProductInfo, null=True, blank=True, on_delete=models.CASCADE, verbose_name='اطلاعات',
                                related_name='product_info')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    is_active = models.BooleanField(default=True, verbose_name='موجودی')
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                 verbose_name='امتیاز')

    slug = models.SlugField(default='', null=False, db_index=True, verbose_name='اسلاگ')

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}---{self.price}"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

        # Create your models here.
