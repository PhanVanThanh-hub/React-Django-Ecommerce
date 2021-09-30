from product.models import *
from rest_framework import viewsets
from .pageSerializers import ResultsSetPagination
from .serializers import *
from .filtersSet import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import AllowAny




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes=[AllowAny,]
    serializer_class = ProductSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filter_class = ProductFilter
    ordering_fields = ['sold']



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes=[AllowAny,]
    serializer_class = CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes=[AllowAny,]
    serializer_class = ServiceSerializer


class SizeViewSet(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    permission_classes=[AllowAny,]
    serializer_class = SizeSerializer