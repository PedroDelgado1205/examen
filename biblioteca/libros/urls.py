from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:pk>/', views.detalle_libro, name='detalle_libro'),
    path('libro/nuevo/', views.nuevo_libro, name='nuevo_libro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

