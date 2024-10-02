from django.urls import path
from views import DoctorList, DoctorDetail, AppointmentList, AppointmentDetail, AvailableTimeSlotList, AvailableTimeSlotDetail

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetail.as_view(), name='doctor-detail'),
    path('appointments/', AppointmentList.as_view(), name='appointment-list'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('available-time-slots/', AvailableTimeSlotList.as_view(), name='available-time-slot-list'),
    path('available-time-slots/<int:pk>/', AvailableTimeSlotDetail.as_view(), name='available-time-slot-detail'),
]