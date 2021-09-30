from rest_framework import viewsets
from .serializers import *
from .filtersSet import *
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from register.models import *
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser
from rest_framework import generics
from django.http import JsonResponse
from urllib.parse import urlparse
import urllib.request as urllib2
import io
from cart.models import *
from product.models import *

import datetime
class RegisterViewSet(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    user = None
    profile = None

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile = Profile.objects.create(user=user, phone_number=request.data.get("phoneNumber"))

        static = StatisticalUser.objects.all().latest('id')

        if static.data_create.month == datetime.datetime.now().month:
            static.amout = static.amout+1
            static.save()

        else:
            StatisticalUser.objects.create(
                amout=1
            )

        profile.save()
        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class UsersViewSet(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "username"]

    # def get_queryset(self):
    #
    #     workspace = self.request.query_params
    #     print("work2111111111111111:",workspace)

class UserDetailViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "user"]


class ProfileViewSet(generics.GenericAPIView):
    queryset = Profile.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id", "user"]

    def post(self,request):
        print("dmm",request.data)
        getData=request.data
        user = User.objects.get(id =getData["data"]["id"])
        print("user:",user)
        profile = Profile.objects.get(user = user)
        print("profile:",profile)
        return JsonResponse(
            {"user": ProfileSerializer(profile, context=self.get_serializer_context()).data,}
        )
class changeUserViewSet(generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = UserSerializer

    def post(self,request):

        getData=request.data
        profile=getData["data"]

        user = User.objects.get(username = profile["username"])

        profi = Profile.objects.get(user= user)
        profi.phone_number=profile["data"]["phone"]
        profi.save()
        user.first_name = profile["data"]["firstName"]
        user.last_name = profile["data"]["lastName"]
        user.email = profile["data"]["email"]
        user.save()

        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

import datetime
import random
from django.contrib.auth import authenticate
class decentralizationUser(generics.ListCreateAPIView):
    permission_classes = [AllowAny, ]
    def post(self,request):


        user = authenticate(request, username=request.data["username"], password=request.data["password"])
        print('user:', user)

        group = None
        if user.groups.exists():
            group = user.groups.all()[0].name

            print('group', group)
        if group == "admin":
            return JsonResponse({

                "message": "Is admin",
            })
        LoginAttempts.objects.create(
            customer=user,
            start=datetime.datetime.now()
        )
        return JsonResponse({

            "message": "not admin",
        })

class Logout(generics.GenericAPIView):
    permission_classes = [AllowAny, ]
    def post(self,request):
        print("re:S",request.data["username"])
        user = User.objects.get(username= request.data["username"])
        group = None
        if user.groups.exists():
            group = user.groups.all()[0].name

            print('group', group)
        if group != "admin":
            t = LoginAttempts.objects.filter(customer=user).latest('th')
            t.end = datetime.datetime.now()
            t.save()
            print("t:",t.start,':',t.end)
        return JsonResponse({

            "message": "true",
        })

    def options(self,request):
        print("???????????????????????dasdsadsadsadsadasdsadsadadsasda")
        return JsonResponse({

            "message": "true",
        })

class LoginAttemptsViews(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class= LoginAttemptsSerializer
    queryset =  LoginAttempts.objects.all()

