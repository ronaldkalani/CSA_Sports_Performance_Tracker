from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from .views import homepage

# Root URL view returning a JSON welcome message
def home_view(request):
    return JsonResponse({"message": "Welcome to CSA Sports Performance Tracker API", "api_root": "/api/"})

urlpatterns = [
    path("", homepage, name="homepage"),  # Homepage view (React frontend or landing page)
    path("home/", home_view, name="api_home"),  # API root welcome message
    path("api/", include("backend.api.urls")),  # API endpoints from backend.api.urls
    path("admin/", admin.site.urls),  # Django Admin panel
]
