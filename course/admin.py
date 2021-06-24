from django.contrib import admin
from .models import Branch, Course, Group, Student

# Register your models here.
admin.site.register(Branch)
admin.site.register(Group)
admin.site.register(Student)
admin.site.register(Course)
