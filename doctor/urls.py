from django.urls import path
from django.views.decorators.cache import cache_page

from doctor.apps import DoctorConfig
from doctor.views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView, \
    OurDoctorView

app_name = DoctorConfig.name

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctor_list'),
    path('our_doctors/', cache_page(60)(OurDoctorView.as_view()), name='our_doctors'),
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_form'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('doctor/<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_confirm_delete'),
]
