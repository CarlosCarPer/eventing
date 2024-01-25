from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("eventing/", include("eventing.urls")),
    path("admin/", admin.site.urls),
]