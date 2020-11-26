from django.db import models
from datetime import datetime
from .category import Category

class Data(models.Model):
    awbno = models.CharField(max_length = 100)
    transporter = models.CharField(max_length = 50)
    source = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    brand = models.CharField(max_length = 100)
    startdate = models.DateTimeField(default=datetime.now, blank=True)
    etd = models.DateTimeField(default=datetime.now, blank=True)
    status = models.CharField(max_length = 100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @staticmethod
    def get_all_datas(): 
        return Data.objects.all

    @staticmethod
    def get_all_datas_by_categoryid(category_id):
        if category_id:
            return Data.objects.filter(category = category_id)
        else:
            return Data.get_all_datas()

    def __str__(self):
        return self.status