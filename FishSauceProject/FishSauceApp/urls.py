from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from FishSauceProject import settings
from .views import *

urlpatterns = [
    path('index', index, name='index'),
    path('', index, name='index'),
    url('get_detail_product/(?P<id>\w{0,50})/$', get_detail_product, name='get_detail_product'),
    path('member/', UserView.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)