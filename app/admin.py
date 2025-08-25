from django.contrib import admin
from .models import Jobcard, Order

# Register your models here.
admin.site.register([Jobcard, Order])