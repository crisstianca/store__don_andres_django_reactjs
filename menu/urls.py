from django.urls import path, include
from rest_framework import routers
from menu import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductsView, 'products')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/categories", views.categories)
]
