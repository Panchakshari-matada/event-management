from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet, AddEventViewSet

# Define Router
router = DefaultRouter()
router.register(r'registers', RegisterViewSet)  # URL for Register API
router.register(r'events', AddEventViewSet)  # URL for AddEvent API

# Include Router URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes defined by the router
]