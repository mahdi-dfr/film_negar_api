from django.contrib import admin
from django.apps import apps

# Register your models here.


for key, model in apps.get_app_config('movie').models.items():
    admin.site.register(model)
