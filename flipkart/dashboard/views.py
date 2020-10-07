from rest_framework import viewsets
from .serializers import *
from .models import *

class AttributeList(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewList(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ImageList(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer