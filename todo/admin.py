#modelleri gostermmek ve kontrol etmek iscin register etmek lazim
from django.contrib import admin
from . models import Todo

# Register your models here.
admin.site.register(Todo)
