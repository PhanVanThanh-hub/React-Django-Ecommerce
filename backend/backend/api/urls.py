from rest_framework import routers
from product.api.views import *
from register.api.views import *
from cart.api.views import *
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from justAdmin.api.views import *

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename="product-view-set")
router.register('categorys', CategoryViewSet, basename="category-view-set")
router.register('services', ServiceViewSet, basename="service-view-set")
router.register('sizes', SizeViewSet, basename="size-view-set")




urlpatterns = [
    #path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterViewSet.as_view()),
    path('users/', UsersViewSet.as_view()),
    path('users/<pk>/', UserDetailViewSet.as_view()),
    path('detail/', ProfileViewSet.as_view()),
    path('cart/',CartViewSet.as_view(),),
    path('decentralization/',decentralizationUser.as_view() ,),

    path('getOrder/',OrderViewSet.as_view() ,),
    path('addProduct/',AddProductViewSet.as_view() ,),
    path('updataProduct/',UpdataProductViewSet.as_view() ,),

    path('listUser/',ListUserViewSet.as_view() ,),
    path('orderProduct/', OrderProductViewSet.as_view(), ),
    path('changeProfile/',changeUserViewSet.as_view() ,),

    path('revenue/',RevenueViewSet.as_view() ,),
    path('oredr7day/',OrderLast7Days.as_view() ,),
    path('bill7day/',BillLast7Days.as_view() ,),
    path('orderPerUser/',TotalOrderPerViewSet.as_view() ,),


    path('logout/',Logout.as_view() ,),
    path('loginAttempt/',LoginAttemptsViews.as_view() ,),

    path('productPopular/',ProductPopular.as_view() ,),
    # path('users/<pk>/', UserDetailViewSet.as_view()),
    # path('detail/', ProfileViewSet.as_view()),
]

urlpatterns += router.urls