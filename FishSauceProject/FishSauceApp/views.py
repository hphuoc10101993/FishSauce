from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render

from FishSauceApp.models import FishSauce, Company


def index(request):
    list_product = FishSauce.objects.all().order_by('-id')
    company = Company.objects.all()
    list_slide = list_product[0:5]
    paginator = Paginator(list_product, 12)  # Show 12 products per page
    page = request.GET.get('page')
    try:
        list_product_per_page = paginator.page(page)
    except PageNotAnInteger:
        list_product_per_page = paginator.page(1)
    except EmptyPage:
        list_product_per_page = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'products': list_product_per_page, 'slides' : list_slide, 'company': company})


def get_detail_product(request, id):
    product = FishSauce.objects.get(id=id)
    data = {
        'name_product' : product.name_product,
        'description' : product.description,
        'image' : product.image.url,
        'price' : product.price,
        'quanity' : product.quanity
    }
    return JsonResponse(data=data)