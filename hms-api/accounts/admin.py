from django.contrib import admin
from .models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number', 'is_staff',
                    'is_superuser', 'is_active', 'is_patient', 'is_physio']

    list_per_page = 10
