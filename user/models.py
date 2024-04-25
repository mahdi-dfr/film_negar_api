from django.contrib.auth.models import AbstractUser
from django.db import models

from utilities.validation_helper import mobile_validator


# Create your models here.

class User(AbstractUser):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران (همه)'

    ROLE = [
        ('0', 'ادمین'),
        ('1', 'کاربر عادی'),
    ]
    role = models.CharField(max_length=1, choices=ROLE, default='1')
    mobile_number = models.CharField(max_length=11, verbose_name='شماره موبایل', null=False, blank=False, unique=True,
                                     validators=[mobile_validator])
    birth_date = models.CharField(max_length=10, verbose_name='تاریخ تولد', null=True, blank=True, )
    last_login = models.DateTimeField(auto_now=True, blank=True, verbose_name='آخرین ورود')
    create_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='تاریخ ایجاد')
    delete_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='تاریخ حذف')
    update_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='تاریخ تغییر')

    def __str__(self):
        return self.username


class ProfileDashboard(models.Model):
    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='user_account',
                             null=False, blank=False)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='movie_profile', null=False, blank=False)
