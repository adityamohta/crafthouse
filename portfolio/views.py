from django.shortcuts import render, get_object_or_404
from .models import Slider, SliderBackground, Product, ServiceBackground, GalleryImage


def home(request):
    slider_image_qs = SliderBackground.objects.all()
    if slider_image_qs.exists():
        slider_image = slider_image_qs.first().image.url
    else:
        slider_image = None

    service_image_qs = ServiceBackground.objects.all()
    if service_image_qs.exists():
        service_image = service_image_qs.first()
    else:
        service_image = None

    slider_qs = Slider.objects.all()
    gallery_qs = GalleryImage.objects.order_by('?')

    product_qs = Product.objects.order_by('?')
    if product_qs.count() > 6:
        product_qs = product_qs[:6]

    context = {
        "slider_image": slider_image,
        "service_image": service_image,
        "slider_qs": slider_qs,
        "product_qs": product_qs,
        "gallery_qs": gallery_qs,
    }
    return render(request, "index.html", context)


def product_list(request):
    product_qs = Product.objects.order_by('?')
    context = {
        "product_qs": product_qs
    }
    return render(request, "product_list.html", context)


def product_detail(request, id):
    # print(id)
    product_obj = get_object_or_404(Product, id=id)

    more_products = Product.objects.exclude(id=id).order_by('?')
    if more_products.count() > 4:
        more_products = more_products[:4]

    context = {
        "product_obj": product_obj,
        "more_products": more_products,
    }
    return render(request, "product_detail.html", context)


def about(request):
    context ={}
    return render(request, "about.html", context)


def contact(request):
    context = {}
    return render(request, "contact.html", context)
