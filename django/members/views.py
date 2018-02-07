from django.contrib import messages
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView
)
from django.contrib.messages.views import SuccessMessageMixin

from .forms import LoginForm


class LoginView(DjangoLoginView):
    template_name = 'members/login.html'
    authentication_form = LoginForm

    def form_valid(self, *args, **kwargs):
        messages.info(self.request, '로그인 되었습니다')
        return super().form_valid(*args, **kwargs)


class LogoutView(DjangoLogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(self.request, '로그아웃 되었습니다')
        return super().dispatch(request, *args, **kwargs)
