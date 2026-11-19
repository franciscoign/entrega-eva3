from django.urls import path
from . import views

urlpatterns = [
    path('', views.SocioListView.as_view(), name='socio_list'),
    path('socio/<int:pk>/', views.SocioDetailView.as_view(), name='socio_detail'),
    path('socio/nuevo/', views.SocioCreateView.as_view(), name='socio_create'),
    path('socio/<int:pk>/editar/', views.SocioUpdateView.as_view(), name='socio_update'),
    path('socio/<int:pk>/eliminar/', views.SocioDeleteView.as_view(), name='socio_delete'),
]
