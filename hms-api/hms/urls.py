from django.urls import path
from django.contrib import admin
from .views import PhysiosView, PatientsView, ServicesView, ServiceDetailsView, BookingsView, BillingsView, BillingDetailsView, PatientDetailView, PhysioDetailView, BookingDetailsView, TreatmentsView, TreatmentDetailsView


urlpatterns = [
    path('physio/', PhysiosView.as_view()),
    path('physio/<int:pk>/', PhysioDetailView.as_view()),
    path('patient/', PatientsView.as_view()),
    path('patient/<int:pk>/', PatientDetailView.as_view()),
    path('service/', ServicesView.as_view()),
    path('service/<int:pk>/', ServiceDetailsView.as_view()),
    path('booking/', BookingsView.as_view()),
    path('booking/<int:pk>/', BookingDetailsView.as_view()),
    path('billing/', BillingsView.as_view()),
    path('billing/<int:pk>/', BillingDetailsView.as_view()),
    path('treatment/', TreatmentsView.as_view()),
    path('treatment/<int:pk>/', TreatmentDetailsView.as_view()),
]
