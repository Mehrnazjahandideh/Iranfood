from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class ReserveModel(models.Model):
     name=models.CharField(_("نام و نام خانوادگی"),max_length=50)
     email=models.CharField(_('ایمیل'),max_length=30)
     phone=models.CharField(_("شماره تماس"),max_length=20)
     number=models.IntegerField(_("تعداد نفرات"))
     data=models.DateField(_("تاریخ "),auto_now=False,auto_now_add=False,default='2026-01-01')
     time=models.TimeField(_("زمان"),auto_now=False,auto_now_add=False,default='08:00:00')
     def __str__(self):
      return self.name