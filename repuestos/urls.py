from django.contrib import admin
from django.urls import path

from .views import RepuestosView, CarritoView, TarjetaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", RepuestosView.as_view(), name="landing_page"),
    path('carrito/', CarritoView.as_view(), name='carrito_page'),
    path("tarjeta/", TarjetaView.as_view(), name="tarjeta"),  
]
