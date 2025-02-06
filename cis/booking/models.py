from django.db import models
from django.contrib.auth.models import User

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
        # You may add uniqueness constraints on shelf and time interval via additional validations

    def __str__(self):
        return f"{self.shelf} booked by {self.teacher} from {self.start_time} to {self.end_time}"
