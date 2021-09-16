from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True,
                             blank=False, verbose_name='کاربر')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def get_total(self, branch):
        cart_items = self.cartitem_set.filter(product__branch__name=branch)
        total = 0
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
        return total

    def __str__(self):
        return 'سبد خرید {}'.format(self.user.get_full_name())


class CartItem(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, verbose_name='عنوان قلم سبد خرید')
    quantity = models.IntegerField(default=1, verbose_name='تعداد')
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=False, blank=False, verbose_name='سبد خرید')

    class Meta:
        verbose_name = 'قلم سبد خرید'
        verbose_name_plural = 'اقلام سبد خرید'

    def get_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return 'اقلام {}'.format(self.cart.__str__())


class Order(models.Model):
    branch = models.ForeignKey('branches.Branch', on_delete=models.CASCADE, null=False, blank=False, verbose_name='شعبه')
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=False, verbose_name='کاربر')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='کد رهگیری پستی')
    address = models.TextField(blank=False, null=False, verbose_name='آدرس ارسال')
    postal_code = models.CharField(max_length=10, blank=False, null=False, default=0, verbose_name='کد پستی')
    is_paid = models.BooleanField(default=False, blank=False, verbose_name='پرداخت شده')
    phone_number = models.CharField(max_length=11, blank=True, null=True, verbose_name='شماره تلفن')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def get_total(self):
        order_items = self.orderitem_set.all()
        total = 0
        for order_item in order_items:
            total += order_item.product_price * order_item.product_quantity
        return total

    def is_posted(self):
        if self.post_code is None:
            return False
        return True

    def __str__(self):
        return 'سفارش {}'.format(self.user.get_full_name())


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False, verbose_name='سفارش')
    product_title = models.CharField(max_length=100, null=False, blank=False, verbose_name='عنوان قلم سفارش')
    product_price = models.IntegerField(blank=False, null=False, verbose_name='قیمت')
    product_quantity = models.IntegerField(blank=False, null=False, verbose_name='تعداد')

    class Meta:
        verbose_name = 'قلم سفارش'
        verbose_name_plural = 'اقلام سفارش'

    def get_total(self):
        return self.product_price * self.product_quantity

    def __str__(self):
        return 'اقلام {}'.format(self.order.__str__())
