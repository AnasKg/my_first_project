from django.urls import path, include
from course.api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('branches', views.BranchViewSet)
router.register('groups', views.GroupViewSet)


urlpatterns = [
    path('v1/', include(router.urls))
    # path('v1/branches/',  views.BranchListView.as_view(), name='branches'),
    # path('v1/branches/<int:pk>/', views.BranchDetailView.as_view(), name='branch_detail')
]
