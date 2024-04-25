from django.apps import apps
from django.contrib import admin

# Register your models here.

for key, model in apps.get_app_config('user').models.items():
    admin.site.register(model)