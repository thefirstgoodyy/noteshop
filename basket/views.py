from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

# Create your views here.
from django.template import RequestContext
from basket.models import BasketItem, Basket
from product.models import Good


def addItemToBasket(request, product_id):
    item = Good.objects.get(pk=product_id)
    if request.user.is_authenticated:
        current_user = request.user
        this_basket = current_user.basket
        BasketItem.objects.create(basket=this_basket,
                                  product=item)
        return HttpResponseRedirect(reverse("basket:show"))
    else:
        return HttpResponse("Not Lol")


def showBasket(request):
    if request.user.is_authenticated:
        current_user = request.user
        this_basket = Basket.objects.get(owner=current_user)
        basket_item_list = BasketItem.objects.filter(basket=this_basket)
        cost = 0
        for item in basket_item_list:
            one_product = Good.objects.get(name=item.product)
            cost += one_product.price
        context = RequestContext(request, {
            'Items': basket_item_list,
            'price': cost
        })
        return render_to_response('basket.html', context)


def deleteRow(request, item_id):
    item = get_object_or_404(BasketItem, pk=item_id)
    if request.user.is_authenticated:
        item.delete()
        current_user = request.user
        this_basket = Basket.objects.get(owner=current_user)
        basket_item_list = BasketItem.objects.filter(basket=this_basket)
        cost = 0
        for item in basket_item_list:
            one_product = Good.objects.get(name=item.product)
            cost += one_product.price
        context = RequestContext(request, {
            'Items': basket_item_list,
            'price': cost
        })
        return HttpResponseRedirect(reverse('basket:show'), context)
