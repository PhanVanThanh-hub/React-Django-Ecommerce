from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('cart',CartViewSet, basename="cart-view-set")
urlpatterns = router.urls