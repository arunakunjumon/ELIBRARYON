from django.contrib import admin

# Register your models here.
from .models import user_reg,Book
admin.site.register(user_reg)
admin.site.register(Book)
