from django.contrib import admin
from .models import Physio, Patient, Service, Booking, Billing, Treatment

# Register your models here.


@admin.register(Physio)
class PhysioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_physio']


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_patient']


@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'physio',
                    'treatment', 'prescription', 'treatment_date']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'cost']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['physio', 'patient', 'service',
                    'resrv_date', 'resrv_time', 'status', 'payment']


@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ['booking', 'patient', 'amount', 'date_billed']
