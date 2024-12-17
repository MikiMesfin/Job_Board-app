from django.core.management.base import BaseCommand
from users.models import CustomUser

class Command(BaseCommand):
    help = 'Creates an employer user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)
        parser.add_argument('password', type=str)
        parser.add_argument('email', type=str)

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email']

        if CustomUser.objects.filter(username=username).exists():
            self.stdout.write(self.style.ERROR(f'User {username} already exists'))
            return

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_employer=True
        )

        self.stdout.write(self.style.SUCCESS(f'Successfully created employer user: {username}')) 