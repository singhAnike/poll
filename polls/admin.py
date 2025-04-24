from django.contrib import admin

from .models import Question, Choice, AdminBase

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(AdminBase)