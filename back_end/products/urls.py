from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,  RecentProductsView
# , api_root, ProductImageViewSet
# from .views import ProductViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet)
# router.register(r'product-images', ProductImageViewSet, basename='productimage')er.register(r'products', ProductViewSet)

urlpatterns = [
   # path('', api_root, name='api-root'),
   path('api/', include(router.urls)),  # اضافه کردن router.urls به مسیر api/
   path('api/recent-products/', RecentProductsView.as_view(), name='recent-products'),
]



