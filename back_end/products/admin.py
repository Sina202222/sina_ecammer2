# from django.contrib import admin
# from .models import Product, ProductImage

# # ثبت مدل‌ها به صورت ساده
# admin.site.register(Product)
# admin.site.register(ProductImage)

from django.contrib import admin
from django.utils.html import format_html
from .models import Product, ProductImage

class ProductImageInline(admin.TabularInline):  # استفاده از TabularInline برای نمایش جدولی
    model = ProductImage
    extra = 5  # تعداد فرم‌های خالی برای اضافه کردن تصاویر جدید
    max_num = 10  # حداکثر تعداد تصاویر مجاز
    fields = ['image', 'is_main', 'image_preview']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "هنوز تصویری آپلود نشده است"
    image_preview.short_description = 'پیش‌نمایش'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]  # اضافه کردن اینلاین برای تصاویر
    list_display = ['name', 'main_image_preview', 'created_at']
    search_fields = ['name']
    
    def main_image_preview(self, obj):
        main_img = obj.images.filter(is_main=True).first()
        if main_img:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', main_img.image.url)
        return "بدون تصویر اصلی"
    main_image_preview.short_description = 'تصویر اصلی'