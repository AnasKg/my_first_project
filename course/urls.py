from django.urls import path
from course.views import branch_detail, group_detail, group_list, my_main_page, branches_list, student_detail, student_list

urlpatterns = [
    path('', my_main_page, name='my_main_page'),
    path('branches/', branches_list, name='branches_list'),
    path('branches/<int:branch_id>/', branch_detail, name='branch_detail'),
    path('groups/', group_list, name='group_list'),
    path('groups/<int:group_id>/', group_detail, name='group_detail'),
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail')
]
