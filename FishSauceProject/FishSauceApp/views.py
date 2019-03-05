from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from FishSauceApp.models import FishSauce, Company, Member
from FishSauceApp.serializers import MemberSerializer


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


class UserView(APIView):

    def get(self, request):
        id = int(request.query_params['id']) if 'id' in request.query_params else None
        users = Member.objects.all()
        if id:
            users = users.filter(id=id)
        serializer = MemberSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        member = request.data.get('member')
        serializer = MemberSerializer(data=member)
        if serializer.is_valid(raise_exception=True):
            member_saved = serializer.save()
        return Response({"status": True})

    def put(self, request):
        id = int(request.query_params['id']) if 'id' in request.query_params else None
        saved_member = get_object_or_404(Member.objects.all(), pk=id)
        member_data = request.data.get('member')
        serializer = MemberSerializer(instance=saved_member, data=member_data, partial=True)
        if serializer.is_valid():
            member_saved = serializer.save()
        return Response({"status": True})

    def delete(self, request):
        id = int(request.query_params['id']) if 'id' in request.query_params else None
        member_item = get_object_or_404(Member.objects.all(), pk=id)
        member_item.delete()
        return Response({"status": True})