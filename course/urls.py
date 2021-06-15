from django.urls import path
from course import views

urlpatterns = [
    path('', views.my_main_page, name='my_main_page'),
    path('branches/', views.branches_list, name='branches_list'),
    path('branches/create/', views.branch_create, name='branch_create'),
    path('branches/<int:branch_id>/', views.branch_detail, name='branch_detail'),

    path('branches/<int:branch_id>/edit/', views.branch_edit, name='branch_edit'),
    
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail')
]
