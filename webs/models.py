from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Food(models.Model):
    FOODS=[
        ('iranifood','غذای ایرانی'),
        ('fastfood','فست فود'),
        ('salad','سالاد'),
    ]
    name=models.CharField(('نام غذا'),max_length=100)
    text=models.TextField(('توضیحات'))
    price=models.IntegerField(('قیمت'),default=100000)
    time=models.IntegerField(('زمان انتظار'),default=2)
    created=models.DateTimeField(('نام غذا'),auto_now_add=True)
    image=models.ImageField(('عکس غذا'),upload_to='webs/')
    type=models.CharField(('نوع غذا'),max_length=50,choices=FOODS,default='fastfood')
    def __str__(self):
        return self.name
        