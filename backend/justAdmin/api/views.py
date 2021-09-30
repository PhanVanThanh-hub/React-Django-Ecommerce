from .serializers import *
from product.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import generics
from django.http import JsonResponse
from .utilsProduct import *
from cart.api.serializers import *
from justAdmin.models import *

class AddProductViewSet(generics.GenericAPIView):

    permission_classes = [AllowAny, ]


    def post(self, request, *args, **kwargs):
        getData = request.data


        createNewProduct(getData)
        product = Product.objects.get(title=getData["title"])
        createBill(getData, product)
        createIncome(getData["purchasePrice"], getData["amout"])

        return JsonResponse({
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class UpdataProductViewSet(generics.GenericAPIView):

    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        getData = request.data

        # cập nhật giá và số lượng sản phẩm

        product = Product.objects.get(title=getData["product"]["title"])
        product.price=getData["price"]
        product.amout = product.amout+getData["amout"]
        product.save()
        ###########

        createBill(getData,product)

        createIncome(getData["purchasePrice"],getData["amout"])


        return JsonResponse({
            "message": "User Created Successfully.  Now perform Login to get your token",
        })



class ListUserViewSet(generics.ListAPIView):
    queryset =  User.objects.all().exclude(id=1)
    permission_classes = [IsAdminUser, ]
    serializer_class = CustomerSeriaLizer

class TotalOrderPerViewSet(generics.ListAPIView):
    queryset =  Order.objects.all()
    serializer_class=OrderSerializer
    permission_classes = [AllowAny, ]

    def post(self,request):

        id = request.data["data"]
        user = User.objects.get(id = id)
        profile = Profile.objects.get(user = user)

        order = Order.objects.filter(customer = profile)
        total = sum(total.get_total_item() for total in order)

        return JsonResponse({
            "total":  total,
        })

class RevenueViewSet(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class = IncomeSeriaLizer

    def get_queryset(self):
        # income = Income.objects.exclude(id=1)
        # test = Income.objects.first()
        # cost = test.total_cost
        # profit = test.total_profit()
        # revenue = test.total_revenue
        #
        # for i in income:
        #     i.growth_revenue = ((float(i.total_revenue) - float(revenue)) / abs(float(revenue)))*100
        #
        #     try:
        #         i.growth_cost = ((float(i.total_cost) - float(cost)) / abs(float(cost)))*100
        #     except:
        #         i.growth_cost = 0
        #     i.growth_profit = ((float(i.total_profit()) - float(profit)) / abs(float(profit)))*100
        #     cost = i.total_cost
        #     profit = i.total_profit()
        #     revenue = i.total_revenue
        #     i.save()
        try:
            workspace = int(self.request.query_params.get('year'))
            queryset = Income.objects.filter(data_create__year=workspace)
        except:
            queryset = Income.objects.all()
        return queryset

from datetime import datetime, timedelta

from django.utils import timezone
class OrderLast7Days(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class= OrderLast7DaySeriaLizer

    def get_queryset(self):
        workspace = int(self.request.query_params.get('day'))
        queryset = Order.objects.filter( data_ordered__gte=datetime.now()-timedelta(days=workspace))
        return queryset


class BillLast7Days(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class= BillLast7DaySeriaLizer

    def get_queryset(self):
        workspace = int(self.request.query_params.get('day'))
        queryset = Bill.objects.filter( date_create__gte=datetime.now()-timedelta(days=workspace))
        return queryset


