from django.db import models

class RunwayStatus(models.Model):
    datetimestamp = models.DateTimeField()
    runway_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.datetimestamp} - {self.runway_name}: {self.status}"