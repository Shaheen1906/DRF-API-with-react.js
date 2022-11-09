from django.urls import path, include
from .views import *
from api import views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('api', views.ProductViewSet, basename='product')
urlpatterns = router.urls