from django.contrib import admin
from myapp.models import Student, ClassRoom, StudentProfile

# Register your models here.
admin.site.register(Student)

admin.site.register(ClassRoom)
admin.site.register(StudentProfile)