
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("crud.urls")),
    path('signin/', include("crud.urls")),
    path('error/', include("crud.urls")),
]
