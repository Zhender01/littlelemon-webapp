from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import index, MenuItemViewSet, BookingViewSet

router = DefaultRouter()
router.register(r"menu-items", MenuItemViewSet, basename="menuitem")
router.register(r"bookings",    BookingViewSet, basename="booking")

urlpatterns = [
    path("", views.index, name="home"),
    path("api/", include(router.urls)),
]


