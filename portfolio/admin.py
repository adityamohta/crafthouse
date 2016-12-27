from django.contrib import admin

from .models import (
    GalleryImage,
    Slider,
    SliderBackground,
    ServiceBackground,
    Product,
    ProductImage,
    About,
    Member
)


class ProductImageInLine(admin.TabularInline):
    model = ProductImage
    extra = 2
    max_num = 10


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'in_stock']
    list_display_links = ['id', 'title']
    list_editable = ['description', 'in_stock']
    search_fields = ['id', 'title']
    list_filter = ['created_at', 'updated_at']
    inlines = [ProductImageInLine]

    class Meta:
        model = Product

admin.site.register(Slider)
admin.site.register(SliderBackground)
admin.site.register(ServiceBackground)
admin.site.register(GalleryImage)
admin.site.register(Product, ProductModelAdmin)
admin.site.register(ProductImage)
admin.site.register(About)
admin.site.register(Member)
