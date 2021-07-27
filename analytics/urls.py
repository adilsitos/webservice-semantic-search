from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'recommendations', RecommendationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]