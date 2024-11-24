from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from denuncias import views

urlpatterns = [
    path('registrar/', views.registrar_denuncia, name='registrar_denuncia'),
    path('admin/', admin.site.urls),
    
    
]