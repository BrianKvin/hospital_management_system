from django.db import models
from django.conf import settings
from django.contrib import admin


class Physio(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    @admin.display(ordering='user__email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__is_physio')
    def is_physio(self):
        return self.user.is_physio


class Patient(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    @admin.display(ordering='user__email')
    def email(self):
        return self.user.email

    @admin.display(ordering='user__is_patient')
    def is_patient(self):
        return self.user.is_patient


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    physio = models.ForeignKey(Physio, on_delete=models.CASCADE)
    treatment = models.TextField()
    prescription = models.TextField()
    treatment_date = models.DateField()

    def __str__(self) -> str:
        return f'{self.treatment} {self.patient}'


class Service(models.Model):
    service = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.service}'


class Booking(models.Model):
    TIME_CHOICES = [('one', '8 - 9am'), ('two', '9 - 10am'), ('three', '10 - 11am'),
                    ('four', '11 - 12pm'), ('five', '12 - 1pm'), ('six', '2 - 3pm'), ('seven', '3 - 4pm')]

    STATUS_CHOICES = (
        ('booked', 'Booked'),
        ('active', 'Active'),
        ('seen', 'Seen')
    )

    payment = models.BooleanField(default=False)
    physio = models.ForeignKey(Physio, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    resrv_date = models.DateField()
    resrv_time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default='six')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='booked')

    def __str__(self):
        return f'{self.patient} - {self.service}'


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, default=None)
    date_billed = models.DateField()
    amount = models.IntegerField()

    def __repr__(self):
        return F'{self.patient} {self.resrv} {self.date_billed} {self.amount}'
