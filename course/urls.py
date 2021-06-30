from django.urls import path, include
from course import views

urlpatterns = [
    path('', views.my_main_page, name='my_main_page'),

    path('branches/', views.BranchListView.as_view(), name='branches_list'),
    path('branches/create/', views.BranchCreateView.as_view(), name='branch_create'),
    path('branches/<int:branch_id>/', views.BranchDetailView.as_view(), name='branch_detail'),
    path('branches/<int:branch_id>/edit/', views.BranchUpdateView.as_view(), name='branch_edit'),
    
    path('groups/', views.group_list, name='group_list'),
    path('groups/<int:group_id>/', views.group_detail, name='group_detail'),

    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/',
         views.StudentDetailView.as_view(), name='student_detail'),

    path("students/random/", views.student_random, name="student_random"),

    path('api/', include('course.api.urls'))
]
