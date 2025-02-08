from django.core.management.base import BaseCommand
from django.utils import timezone
from booking.models import Reservation

class Command(BaseCommand):
    help = 'Deletes reservations that have expired (end_time is in the past)'

    def handle(self, *args, **options):


        # ВНИМАНИЕ НА ЧАСОВОЙ ПОЯС!!!
        now = timezone.now() + timezone.timedelta(hours=3)

        expired_reservations = Reservation.objects.filter(end_time__lt=now)
        count = expired_reservations.count()
        self.stdout.write(self.style.NOTICE(f"Current time: {now}"))
        self.stdout.write(self.style.NOTICE(f"Found {count} expired reservation(s):"))
        for res in expired_reservations:
            self.stdout.write(f"- {res}")
        expired_reservations.delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} expired reservation(s)."))
