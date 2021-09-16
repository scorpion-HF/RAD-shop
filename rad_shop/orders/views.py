from django.views.generic import UpdateView, DeleteView, CreateView, ListView, DetailView
from .models import Cart, CartItem, Order, OrderItem
from .forms import AddToCartForm, OrderForm
from django.forms import formset_factory
from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from branches.models import Branch


class UserCart(LoginRequiredMixin, UpdateView):
    model = Cart
    template_name = 'orders/cart.html'
    context_object_name = 'cart'

    def get(self, request, *args, **kwargs):
        if self.kwargs['branch'] == 'none':
            return HttpResponseRedirect(reverse('branches:select-branch', args=['cart']))
        else:
            get_object_or_404(Branch, name=self.kwargs['branch'])
        return super().get(request, *args, **kwargs)

    def get_form_class(self):
        return formset_factory(AddToCartForm, extra=len(CartItem.objects.filter(cart=self.get_object())))

    def get_form(self, form_class=None):
        data = {
            'form-TOTAL_FORMS': len(CartItem.objects.filter(cart=self.get_object())),
            'form-INITIAL_FORMS': len(CartItem.objects.filter(cart=self.get_object())),
        }
        i = 0
        for item in CartItem.objects.filter(cart=self.get_object()):
            data['form-{}-quantity'.format(i)] = item.quantity
            i += 1
        initial = []
        for item in CartItem.objects.filter(cart=self.get_object()):
            initial.append({'quantity': item.quantity})
        forms = self.get_form_class()(data=data, initial=initial)
        return forms

    def post(self, request, *args, **kwargs):
        initial = []
        for item in CartItem.objects.filter(cart=self.get_object()):
            initial.append({'quantity': item.quantity})
        forms = self.get_form_class()(request.POST, initial=initial)
        for form, item in zip(forms, CartItem.objects.filter(cart=self.get_object())):
            form.instance = item
        if forms.is_valid():
            return self.form_valid(forms)
        else:
            messages.error(self.request, 'خطا در ورود اطلاعات')
            return HttpResponseRedirect(reverse('orders:user-cart', kwargs={'branch': 'none'}))

    def form_valid(self, form):
        for f in form:
            f.save()
            return HttpResponseRedirect(reverse('orders:user-cart', kwargs={'branch': 'none'}))

    def get_object(self, queryset=None):
        return Cart.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = CartItem.objects.filter(cart=self.get_object(),
                                                        product__branch__name=self.kwargs['branch'])
        context['formset__cart_items'] = zip(self.get_form(),
                                             CartItem.objects.filter(cart=self.get_object(),
                                                                     product__branch__name=self.kwargs['branch']))
        context['cart_total'] = Cart.objects.get(user=self.request.user).get_total(self.kwargs['branch'])
        return context


class RemoveFromCart(LoginRequiredMixin, DeleteView):
    model = CartItem

    def get_success_url(self):
        messages.success(self.request, '"{}" از سبد خرید شما حذف گردید'.format(self.get_object().product.title))
        return reverse('orders:user-cart', kwargs={'branch': 'سیرجان'})

    def get(self, request, *args, **kwargs):
        if self.get_object().cart.user == self.request.user:
            url = self.get_success_url()
            self.get_object().delete()
            return HttpResponseRedirect(url)
        else:
            messages.error('درخواست غیر مجاز')
            return HttpResponseRedirect(reverse('orders:user-cart', kwargs={'branch': 'سیرجان'}))


class CreateOrder(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/create-order.html'
    form_class = OrderForm

    def get(self, request, *args, **kwargs):
        get_object_or_404(Branch, name=self.kwargs['branch'])
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('orders:orders')

    def get_initial(self):
        self.initial['address'] = self.request.user.address
        self.initial['phone_number'] = self.request.user.phone_number
        self.initial['postal_code'] = self.request.user.postal_code
        return self.initial.copy()

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.branch = Branch.objects.get(name=self.kwargs['branch'])
        self.object.save()
        cart, cart_created = Cart.objects.get_or_create(user=self.request.user)
        cart_items = cart.cartitem_set.filter(product__branch__name=self.kwargs['branch'])
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=self.object,
                                                  product_title=cart_item.product.title,
                                                  product_price=cart_item.product.price,
                                                  product_quantity=cart_item.quantity)
            order_item.save()
            cart_item.delete()
        return super().form_valid(form)


class OrdersList(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-date')


class RemoveOrder(LoginRequiredMixin, DeleteView):
    model = Order

    def get_success_url(self):
        messages.success(self.request, 'سفارش حذف گردید')
        return reverse('orders:orders')

    def get(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user and self.get_object().postal_code:
            self.get_object().delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            messages.error('درخواست غیر مجاز')
            return HttpResponseRedirect(reverse('orders:orders'))


class OrderDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'orders/order_detail.html'

    def has_permission(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItem.objects.filter(order=self.get_object())
        return context





