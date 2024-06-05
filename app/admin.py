from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Product, Image, Attribute, Customers, Specific, Specific_value

# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(Customers)
admin.site.register(Specific)
admin.site.register(Specific_value)
admin.site.unregister(User)
admin.site.unregister(Group)