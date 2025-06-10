from rest_framework import viewsets
from rest_framework.decorators import action, api_view 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductListSerializer
# , ProductImageSerializer

from rest_framework.views import APIView

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    @api_view(['GET'])
    def api_root(request, format=None):
        from .models import Product
        from .serializers import ProductSerializer
        
        recent_products = Product.objects.order_by('-created_at')[:3]
        serializer = ProductSerializer(recent_products, many=True, context={'request': request})
        
        return Response({
            'recent_products': serializer.data,
            'endpoints': {
                'all_products': reverse('product-list', request=request, format=format),
                'upload_images': reverse('product-upload-images', request=request, format=format),
            }
        })
        
        
        
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=True, methods=['post'], url_path='upload-images')
    def upload_images(self, request):
        product = self.get_object()
        images = request.FILES.getlist('images')
        main_image_id = request.data.get('main_image_id')

        for image in images:
            ProductImage.objects.create(product=product, image=image)

        if main_image_id:
            try:
                image = product.images.get(id=main_image_id)
                image.is_main = True
                image.save()
            except ProductImage.DoesNotExist:
                pass

        return Response({'status': 'images uploaded'})

    @action(detail=True, methods=['patch'], url_path='set-main-image')
    def set_main_image(self, request, pk=None):
        product = self.get_object()
        image_id = request.data.get('image_id')

        try:
            image = product.images.get(id=image_id)
            image.is_main = True
            image.save()
            return Response({'status': 'main image set'})
        except ProductImage.DoesNotExist:
            return Response({'error': 'image not found'}, status=404)
        
        
class RecentProductsView(APIView):
    def get(self, request):
        products = Product.objects.order_by('-created_at')[:3]
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)