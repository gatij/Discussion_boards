from django.contrib import admin
from .models import Board

# Register your models here.
# Board will available for CRUD operations in admin panel
admin.site.register(Board)