from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard import views

router = DefaultRouter()
router.register(r'attribute', views.AttributeList)
router.register(r'product', views.ProductList)
router.register(r'review', views.ReviewList)
router.register(r'image', views.ImageList)

urlpatterns = [
    path('', include(router.urls)),
]