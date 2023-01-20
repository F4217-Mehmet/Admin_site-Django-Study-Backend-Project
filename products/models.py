from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)  #SlugField, temel olarak belirli bir URL'den sonra URL yollarını depolamak için kullanılır.

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
    
    def __str__(self):
        return f"{self.name} - {self.description}"

    def added_days_ago(self): 
        fark = timezone.now() - self.create_date
        return fark.days
#adminde yaptığımın  aynısını burada yaptım. sadece self yeterli. adminde yazdığım sadece admini ilgilendirir. Modelde yazdığım artık objeye ait oldu. projenin her yerinde kullanabilirim, ulaşabilirim.
