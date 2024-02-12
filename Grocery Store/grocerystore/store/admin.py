from django.contrib import admin
from .models import Product,Orders,Contact
# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Contact)