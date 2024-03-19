# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import APIView
# from django.shortcuts import get_object_or_404

from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin
from .models import Billing, Patient, Physio, Booking, Service, Treatment
from .serializers import BillingSerializer, PhysioSerializer, PatientSerializer, BookingSerializer, ServiceSerializer, TreatmentSerializer


class PhysiosView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PhysioSerializer
    queryset = Physio.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PhysioDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = PhysioSerializer
    queryset = Physio.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class PatientsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PatientDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class ServicesView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ServiceDetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


class BillingsView(GenericAPIView, CreateModelMixin, ListModelMixin):
    serializer_class = BillingSerializer
    queryset = Billing.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BillingDetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = BillingSerializer
    queryset = Billing.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class BillingsView(GenericAPIView):
#     def get(self, request):
#         bill = Billing.objects.all()
#         serializer = BillingSerializer(bill, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BillingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BillingDetailsView(APIView):
#     def get(self, request, pk):
#         bill = get_object_or_404(Billing, pk=pk)
#         serializer = BillingSerializer(bill, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         patient = Billing.objects.get(pk=pk)
#         serializer = BillingSerializer(patient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         patient = Billing.objects.get(pk=pk)
#         patient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class BookingsView(APIView):
#     def get(self, request):
#         booking = Booking.objects.all()
#         serializer = BookingSerializer(booking, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookingDetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TreatmentsView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TreatmentDetailsView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = TreatmentSerializer
    queryset = Treatment.objects.all()
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class TreatmentsView(APIView):
#     def get(self, request):
#         treatment = Treatment.objects.all()
#         serializer = TreatmentSerializer(treatment, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TreatmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TreatmentDetailsView(APIView):
#     def get(self, request, pk):
#         treatment = get_object_or_404(Treatment, pk=pk)
#         serializer = TreatmentSerializer(treatment)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         treatment = Treatment.objects.get(pk=pk)
#         serializer = TreatmentSerializer(treatment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         treatment = Treatment.objects.get(pk=pk)
#         treatment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
