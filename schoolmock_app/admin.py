from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TeacherInput)
admin.site.register(Option)
admin.site.register(TeacherQuestion)
admin.site.register(StudentInput)

class OptionAdmin(admin.ModelAdmin):
    model = Option
    extra = 4
    max_num = 4
