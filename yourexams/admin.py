from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Test)
admin.site.register(models.Answer)
admin.site.register(models.Question)
