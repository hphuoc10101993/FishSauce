from django.contrib import admin

from FishSauceApp.forms import FishSauceForm, CompanyForm
from FishSauceApp.models import FishSauce, Company, Member

admin.site.site_header  = 'Fish Sauce MaiThuy'


class FishSauceAdmin(admin.ModelAdmin):
    form = FishSauceForm
    list_display = ('name_product', 'price', 'description', 'produce_date', 'expire_date', 'quanity', 'image')


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ('name_company', 'phone', 'address')


admin.site.register(FishSauce, FishSauceAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Member)
