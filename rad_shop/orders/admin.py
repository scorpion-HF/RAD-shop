from django.contrib import admin
from . import models

admin.site.register(models.CartItem)
admin.site.register(models.Cart)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)




