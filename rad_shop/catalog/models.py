from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False, primary_key=True,
                             verbose_name='عنوان دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ('title',)

    def __str__(self):
        return self.title


class Specification(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='عنوان')
    value = models.CharField(max_length=150, blank=False, null=False, verbose_name=' مقدار')
    product = models.ForeignKey('Product', blank=False, null=False, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'مشخصه'
        verbose_name_plural = 'مشخصات'
        ordering = ('product',)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(upload_to='products_images/', null=True, blank=True, verbose_name='تصویر محصول')
    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    price = models.IntegerField(blank=False, verbose_name='قیمت')
    categories = models.ManyToManyField('Category', blank=False, verbose_name='دسته بندی ها')
    branch = models.ForeignKey('branches.Branch', blank=False, null=False, verbose_name='شعبه', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title
