from django.contrib import admin
from .models import data_management_model,user_management_model

admin.site.register(data_management_model)
admin.site.register(user_management_model)
