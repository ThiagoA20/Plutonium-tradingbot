from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tb_app.urls'), name='tb_app'),
    path('/api/', include('api.urls'), name='api'),
]
