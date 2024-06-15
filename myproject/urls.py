from django.contrib import admin
from django.urls import path, include
from users.views import index  # Importa la vista index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', index, name='index'),  # Aggiungi la rotta per la pagina index
]

