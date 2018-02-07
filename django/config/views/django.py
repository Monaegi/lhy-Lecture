import json

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

__all__ = (
    'IndexView',
    'EmailSend',
)


class IndexView(TemplateView):
    template_name = 'index.html'


@method_decorator(csrf_exempt, name='dispatch')
class EmailSend(View):
    def post(self, request):
        subject = 'Lecture test email'
        secrets = json.loads(open(settings.SECRET_BASE).read())
        from_email = secrets['EMAIL_HOST_USER']
        to = secrets['EMAIL_TEST_USER']
        text_content = 'Text content'
        html_content = render_to_string('mail/test.html')
        msg = EmailMultiAlternatives(subject, text_content, to=[to], from_email=from_email)
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return HttpResponse(f'{subject}: {text_content}')
