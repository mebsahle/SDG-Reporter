from .views import HomeView, GoalDetailView,PerformanceDetailView, PerformanceCreateView
from django.urls import path


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('goal_detail/<int:pk>/', GoalDetailView.as_view(), name='goal_detail'),
    path('performance_detail/<int:id>/<int:pk>/', PerformanceDetailView.as_view(), name='performance_detail'),
    path('performance_create/<int:id>/', PerformanceCreateView.as_view(), name='performance_create'),
]