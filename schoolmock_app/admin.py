from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(School, ClassGroup,)
admin.site.register(Student, Test,)
admin.site.register(Question, Result,)
admin.site.register(TeacherInput, TeacherQuestion,)
admin.site.register(Option)