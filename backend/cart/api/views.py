from .serializers import *
from cart.models import *
from product.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework import generics
from django.http import JsonResponse
from .utils import *
from django_filters.rest_framework import DjangoFilterBackend

class CartViewSet(generics.GenericAPIView):
    queryset = Order.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = CartSerializer



    def post(self, request, *args, **kwargs):
        getData = request.data.get("params")

        products=getData["products"]
        location = getData["location"]
        user = getData["newUser"]


        user = User.objects.get(username=user)
        customer = Profile.objects.get(user=user)

        #Lưu sản phẩm đã mua
        order = Order.objects.create(customer = customer)

        createOrderItem(order,products)
        print("getTotal:",order.get_total_item())

        # Tính doanh thu
        createIncome(order.get_total_item())

        #Lưu vị trí
        country =countryUser(location["country"])
        locationUser(order,customer,country,location["region"])

        customer.save()
        order.save()



        return JsonResponse({

            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class OrderViewSet(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):

        username=request.data["username"]
        user = User.objects.get(username=username)
        customer = Profile.objects.get(user=user)
        order = Order.objects.filter(customer=customer)
        return JsonResponse({
            "order": OrderSerializer(order, context=self.get_serializer_context(),many=True).data,

        })

class OrderProductViewSet(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrderProductSerializer

    def post(self, request, *args, **kwargs):
        id=request.data["transaction_id"]
        order = Order.objects.filter(transaction_id=id)
        listProduct = OrderItem.objects.filter(order= order[0])
        return JsonResponse({
            "order": OrderProductSerializer(listProduct, context=self.get_serializer_context(),many=True).data,

        })

class ProductPopular(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = OrderProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product"]

    def get_queryset(self):
        workspace = self.request.query_params.get('product')
        queryset = OrderItem.objects.filter(product=workspace)
        return queryset


