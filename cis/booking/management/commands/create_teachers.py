from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Создать 30 учётных записей учителей'

    def handle(self, *args, **kwargs):
        for i in range(1, 31):
            username = f"teacher{i}"
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password='default_password')
        self.stdout.write(self.style.SUCCESS('Учётные записи учителей созданы.'))
