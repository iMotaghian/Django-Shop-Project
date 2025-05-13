from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import ProductModel, ProductStatusType, ProductCategoryModel

# Create your views here.

class ShopProductGridView(ListView):
    template_name = "shop/products-grid.html"
    queryset = ProductModel.objects.filter(status=ProductStatusType.publish.value)