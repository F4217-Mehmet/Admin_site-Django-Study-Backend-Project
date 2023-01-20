from django.contrib import admin
from .models import Product

admin.site.register(Product)

admin.site.site_title = "Coredinat Title"
admin.site.site_header = "Coredinat Admin Portal"  
admin.site.index_title = "Welcome to Coredinat Admin Portal"