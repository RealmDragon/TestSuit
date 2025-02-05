from django.urls import path, include

from health.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView, RecordDetailView, DiagnosticsListView
from health.apps import HealthConfig

app_name = HealthConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_form'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('record/', RecordListView.as_view(), name='record_list'),
    path('record/<int:pk>', RecordDetailView.as_view(), name='record_detail'),
    path('record/create/', RecordCreateView.as_view(), name='record_form'),
    path('record/<int:pk>/update/', RecordUpdateView.as_view(), name='record_update'),
    path('record/<int:pk>/delete/', RecordDeleteView.as_view(), name='record_confirm_delete'),
    path('diagnostics/', DiagnosticsListView.as_view(), name='diagnostics_list'),

]
