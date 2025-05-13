from django.db import models

# Create your models here.
class ProductStatusType(models.IntegerChoices):
    publish = 1 ,("نمایش")
    draft = 2 ,("عدم نمایش")
    
    

class ProductCategoryModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    
    
    
class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategoryModel)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(default="/default/product-image.png",upload_to="product/img/")
    description = models.TextField()
    stock = models.PositiveBigIntegerField(default=0)
    status = models.IntegerField(choices=ProductStatusType.choices,default=ProductStatusType.draft.value)
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]


class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="product/extra-img/")
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_data = models.DateTimeField(auto_now=True)