import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    URL_BASE = 'https://api.github.com/repos/{github}/{repo}/commits'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs='+', type=str)

    def handle(self, *args, **options):
        for username in options['username']:
            user = User.objects.get(username=username)
            response = requests.get(
                self.URL_BASE.format(
                    github=user.github,
                    repo=user.blog_repository,
                )
            )
            data = response.json()
            for item in data:
                print(item['sha'])
