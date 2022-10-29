from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls'))
]
