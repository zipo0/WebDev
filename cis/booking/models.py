# models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Shelf(models.Model):
    FLOOR_CHOICES = (
        (2, 'Floor 2'),
        (3, 'Floor 3'),
    )
    floor = models.IntegerField(choices=FLOOR_CHOICES)
    number = models.IntegerField()  # Shelf number (1-20)

    class Meta:
        unique_together = ('floor', 'number')
        ordering = ['floor', 'number']

    def __str__(self):
        return f"Floor {self.floor} - N {self.number}"

class Reservation(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        ordering = ['start_time']
        # Дополнительные проверки на уникальность по интервалу времени можно добавить через валидацию

    def __str__(self):
        return f"{self.shelf} booked by {self.teacher} from {self.start_time} to {self.end_time}"

    @property
    def booking_period(self):
        local_start = timezone.localtime(self.start_time)
        local_end = timezone.localtime(self.end_time)
        # Форматирование с точками: день.месяц.год часы:минуты
        return f"{local_start:%d.%m.%Y %H:%M} - {local_end:%d.%m.%Y %H:%M}"
