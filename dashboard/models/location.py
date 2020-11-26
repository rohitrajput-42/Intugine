from django.db import models
from datetime import datetime

class Location(models.Model):
    
    status = models.CharField(max_length = 150)
    date = models.DateTimeField(default=datetime.now, blank=True)

    @staticmethod
    def get_all_stats():
        return Location.objects.all
    