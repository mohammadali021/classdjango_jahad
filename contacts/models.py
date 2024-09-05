from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام")
    email = models.EmailField(max_length=100,verbose_name = "ایمیل")
    last_name = models.CharField(max_length=100,verbose_name ="نام خانوادگی")
    password=models.CharField(max_length=100 , verbose_name="رمز عبور")
    phone_number = models.CharField(max_length=100,verbose_name ="شماره تماس")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name ="تاریخ ثبت نام")

    def __str__(self):
        return f'{self.name}...{self.last_name}...{self.email}...{self.phone_number}'
    class Meta:
        verbose_name = "مشترکین ما"
        verbose_name_plural = verbose_name

# Create your models here.
