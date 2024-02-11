from datetime import date, timedelta
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, FormView

from shopapp.forms import ProductForm
from shopapp.models import Client, Product, Order


class ClientOrders(TemplateView):
    template_name = "shopapp/client_orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_object_or_404(Client, pk=context['client_id'])
        orders = Order.objects.filter(owner=client).order_by('id')
        context['client'] = client
        context['orders'] = orders
        return context


class OrderedProducts(TemplateView):
    template_name = "shopapp/ordered_products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = get_object_or_404(Client, pk=context['client_id'])
        context['client'] = client
        orders = Order.objects.filter(owner=client).order_by('id')
        cur_date = date.today()
        products_for_week = {}
        products_for_month = {}
        products_for_year = {}
        for order in orders:
            for item in order.items.all():
                if order.created > (cur_date - timedelta(days=7)):
                    products_for_week[f'{item.product}'] = item.product
                if order.created > (cur_date - timedelta(days=30)):
                    products_for_month[f'{item.product}'] = item.product
                if order.created > (cur_date - timedelta(days=365)):
                    products_for_year[f'{item.product}'] = item.product
        context['products_for_week'] = products_for_week
        context['products_for_month'] = products_for_month
        context['products_for_year'] = products_for_year
        return context


class ProductView(TemplateView):
    template_name = "shopapp/product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=context['product_id'])
        context['product'] = product
        return context


class ProductAdd(FormView):
    template_name = "shopapp/add_product.html"
    form_class = ProductForm
    # success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        return redirect(form.save().get_absolute_url())

