from django.shortcuts import render,redirect,get_object_or_404
from item.models import Item
from django.urls import reverse

def cart_summary(request):
    items = Item.objects.filter(is_in_cart=True)
    return render(request, "cart/cart_summary.html",{
        'items':items,
    })

def cart_add(request, item_id):
    item = Item.objects.get(id=item_id)
    item.is_in_cart = True
    item.save()
    return redirect(reverse('item:detail', kwargs={'pk': item_id}))

def cart_delete(request, name):
    item = Item.objects.get(name=name)
    item.is_in_cart = False
    item.save()
    return redirect('/cart/')
