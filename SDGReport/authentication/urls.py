from .views import UserLoginView, UserLogoutView

from django.urls import path


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]