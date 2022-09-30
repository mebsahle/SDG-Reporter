# import LoginView, LogoutView
from django.contrib.auth.views import LoginView, LogoutView

#  import reverse_lazy
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'authentication/login.html'
    
    def get_success_url(self):
        user = self.request.user.id
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    template_name = 'authentication/logout.html'
    
    # redirect user to login page after logout
    def get_next_page(self):
        return reverse_lazy("login")


