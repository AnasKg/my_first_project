from django.urls import path
from course.views import group_list, my_main_page, branches_list, student_list

urlpatterns = [
    path('', my_main_page, name='my_main_page'),
    path('branches/', branches_list, name='branches_list'),
    path('groups/', group_list, name='group_list'),
    path('students/', student_list, name='student_list')
]
