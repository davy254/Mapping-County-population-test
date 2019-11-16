from django.contrib.gis import admin
from .models import County

# Register your models here.
admin.site.register(County,admin.OSMGeoAdmin)