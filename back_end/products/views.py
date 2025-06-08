from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductListSerializer
# , ProductImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        if self.action == 'list':
            queryset = queryset.prefetch_related('images')
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer

    @action(detail=True, methods=['post'], url_path='upload-images')
    def upload_images(self, request, pk=None):
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