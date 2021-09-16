from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .models import Product, Category
from .forms import CategoryFilterForm
from django.shortcuts import render
from orders.forms import AddToCartForm
from orders.models import CartItem, Cart
from django.contrib import messages
from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404
from branches.models import Branch


class ProductsList(ListView, FormMixin):
    model = Product
    context_object_name = 'products'
    template_name = 'catalog/products.html'
    form_class = CategoryFilterForm

    def get(self, request, *args, **kwargs):
        if self.kwargs['branch'] == 'none':
            return HttpResponseRedirect(reverse('branches:select-branch', args=['products']))
        else:
            get_object_or_404(Branch, name=self.kwargs['branch'])
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        filters = []
        for field in form.fields:
            if form[field].value():
                filters.append(Category.objects.get(title=field).pk)
        if len(filters) > 0:
            context = self.get_context_data(object_list=self.get_queryset().filter(categories__in=filters))
            self.queryset = self.get_queryset().filter(categories__in=filters)
        else:
            context = self.get_context_data(object_list=self.get_queryset())
            self.queryset = self.get_queryset()

        return render(request=self.request, template_name='catalog/products.html',
                      context=context)

    def get_queryset(self):
        self.queryset = Product.objects.filter(branch=self.kwargs['branch'])
        term = self.request.GET.get('term')
        if term:
            self.queryset = Product.objects.filter(title__contains=term)
        return super().get_queryset()


class ProductDetail(DetailView, FormMixin):
    model = Product
    context_object_name = 'product'
    template_name = 'catalog/product.html'
    form_class = AddToCartForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('account_login'))
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'ابتدا باید وارد حساب کاربری خود شوید')
            return HttpResponseRedirect(reverse('account_login'))
        cart, cart_created = Cart.objects.get_or_create(
            user=self.request.user,
        )
        cart_item, cart_item_created = CartItem.objects.get_or_create(
            cart_id=cart.id,
            product=self.get_object()
        )
        cart_item.quantity = form.cleaned_data['quantity']
        cart_item.save()
        messages.success(self.request, '{} عدد "{}" به سبد خرید اضافه شد'.format(cart_item.quantity, self.get_object()))
        return HttpResponseRedirect(reverse('catalog:product', args=[self.get_object().pk, self.kwargs['branch']]))









