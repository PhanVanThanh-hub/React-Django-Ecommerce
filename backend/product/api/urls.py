from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename="product-view-set")
router.register('categorys', CategoryViewSet, basename="category-view-set")
router.register('services', ServiceViewSet, basename="service-view-set")
router.register('sizes', SizeViewSet, basename="size-view-set")
urlpatterns = router.urls