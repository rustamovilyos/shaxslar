from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('members', views.MemberViewSet)

urlpatterns = [
    path('', include(router.urls))
]
