from django.contrib import admin
from .models import Female,Male
from .models import Login


admin.site.register(Female)
admin.site.register(Male)
admin.site.register(Login)