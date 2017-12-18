from django.contrib.auth.views import LoginView as DjangoLoginView

from .forms import LoginForm


class LoginView(DjangoLoginView):
    template_name = 'members/login.html'
    authentication_form = LoginForm
