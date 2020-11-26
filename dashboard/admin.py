from django.contrib import admin
from .models.data import Data
from .models.category import Category
from .models.location import Location

class AdminData(admin.ModelAdmin):
    list_display = ['awbno', 'startdate', 'etd', 'status', 'category'] 

class AdminLocation(admin.ModelAdmin):
    list_display = ['status', 'date']

admin.site.register(Data, AdminData)
admin.site.register(Category)
admin.site.register(Location, AdminLocation)