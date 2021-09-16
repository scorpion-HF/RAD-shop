from django.contrib import admin
from .models import Category, Specification, Product


class SpecificationInline(admin.TabularInline):
    model = Specification


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    inlines = [
        SpecificationInline,
    ]
    filter_horizontal = ('categories',)
    list_display = ['title', 'price']


admin.site.register(Category)
admin.site.register(Specification)
