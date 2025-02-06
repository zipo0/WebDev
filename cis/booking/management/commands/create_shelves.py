from django.core.management.base import BaseCommand
from booking.models import Shelf

class Command(BaseCommand):
    help = 'Создать полки для 2-го и 3-го этажей'

    def handle(self, *args, **kwargs):
        for floor in [2, 3]:
            for number in range(1, 21):
                Shelf.objects.get_or_create(floor=floor, number=number)
        self.stdout.write(self.style.SUCCESS('Полки успешно созданы.'))
