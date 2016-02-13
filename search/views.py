from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from restaurant.models import *
from django.db import IntegrityError
from restaurant.models import *
from itertools import chain
from django.views import generic
from django.db.models import Q


def search_view(request):
    has_restaurant=False;
    if request.user.is_authenticated():
        if Restaurant.objects.filter(login=request.user):
            has_restaurant = True

    ''' checking if the user has any restaurant under his login or it's just an admin or restauantless account '''

    cities = Restaurant.objects.values('district').distinct()
    cities = [city['district'] for city in cities]

    fooditem = Item.objects.values('item_name').distinct()
    fooditem = [item['item_name'] for item in fooditem]

    foodelement = Element.objects.values('element_name').distinct()
    foodelement = [item['element_name'] for item in foodelement]

    foods = sorted(chain(fooditem, foodelement), key=lambda s: s.lower())

    district_is_marked = request.GET.get('district_check', None)
    fooditem_is_marked = request.GET.get('food_check', None)
    price_is_marked = request.GET.get('price_check', None)

    district_checked = ''
    food_checked = ''
    price_checked = ''
    if district_is_marked:
        district_checked = 'checked'
    if fooditem_is_marked:
        food_checked = 'checked'
    if price_is_marked:
        price_checked = 'checked'

    district = request.GET.get('district', None)
    food = request.GET.get('food', None)
    starting_price = request.GET.get('price_start', None)
    ending_price = request.GET.get('price_end', None)

    final_query_set = Item.objects.none()
    d_flag = f_flag = False

    if district_is_marked:
        district_query = Item.objects.filter(restaurant__in=Restaurant.objects.filter(district__icontains=district))
        d_flag = True
        final_query_set = district_query

    if fooditem_is_marked:
        food_query = Item.objects.filter(Q(element__in=Element.objects.filter(element_name__icontains=food))|Q(item_name__icontains=food))
        f_flag = True
        if final_query_set or d_flag:
            final_query_set = final_query_set & food_query
        else:
            final_query_set = food_query


    if price_is_marked:
        price_query = Item.objects.filter(price__range=(starting_price,  ending_price))
        if final_query_set or d_flag or f_flag:
            final_query_set = final_query_set & price_query
        else:
            final_query_set = price_query

    final_query_set = final_query_set.distinct()

    if district_is_marked or fooditem_is_marked or price_is_marked:
        return render(request, "search/search.html", {
            'cities': cities,
            'foods': foods,
            'searchresult': True,
            'items': final_query_set,
            'has_restaurant': has_restaurant,
            'district': district,
            'food_value': food,
            'starting_price': starting_price,
            'ending_price': ending_price,
            'district_checked': district_checked,
            'food_checked': food_checked,
            'price_checked': price_checked,
        })
    else:
        return render(request, "search/search.html", {
            'cities': cities,
            'foods': foods,
            'searchresult': False,
            'has_restaurant': has_restaurant,
            })


def search_restaurant_view(request, restaurant_id):
    selected_restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    if request.user.is_authenticated:
        user = auth.get_user(request)
        if user.is_anonymous():
            return render(request, 'search/restaurant.html', {'restaurant': selected_restaurant, })
        queryset = Restaurant.objects.filter(login=user)
        if not queryset:
            return render(request, 'search/restaurant.html', {'restaurant': selected_restaurant, })
        else:
            if queryset[0]==selected_restaurant:
                return redirect('/restaurant')
            else:
                return render(request, 'search/restaurant.html', {'restaurant': selected_restaurant, })
    else:
        return render(request, 'search/restaurant.html', {'restaurant': selected_restaurant, })
        




    return render(request, 'search/restaurant.html', {
        'restaurant': selected_restaurant,
        })

def item_view(request, item_id):
    selected_item = get_object_or_404(Item, pk=item_id)
    reviews = ItemReview.objects.filter(item=selected_item)

    return render(request, 'search/item.html', {
        'item': selected_item,
        'reviews': reviews,
        })


def item_review(request, item_id):
    url = '/search/item/'+str(item_id)
    selected_item = get_object_or_404(Item, pk=item_id)
    reviews = ItemReview.objects.filter(item=selected_item)
    if request.method == 'GET':
        return redirect(url)
    else:
        title = request.POST.get('title', None)
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        rating = request.POST.get('rating', None)
        review = request.POST.get('review', None)

        if title and username and email and rating and review:
            try:
                obj, created = ItemReview.objects.get_or_create(item=selected_item, email=email, defaults={'title': title, 'username': username, 'rating': rating, 'review': review, })
                if not created:
                    messages.error(request, "\nReview not added. Already exists.")
                    return render(request, 'search/item.html', {
                            'item': selected_item,
                            'reviews': reviews,
                            'title': title,
                            'username': username,
                            'email': email,
                            'review': review,
                            })
                else:
                    messages.success(request, "\nReview added.")
                    return redirect(url)
            except Exception as e:
                messages.error(request,  e.message)
                return render(request, 'search/item.html', {
                            'item': selected_item,
                            'reviews': reviews,
                            'title': title,
                            'username': username,
                            'email': email,
                            'review': review,
                            })
        else:
            messages.error(request, "\nFailed to add review. Check all field are filled correctly")
            return render(request, 'search/item.html', {
                            'item': selected_item,
                            'reviews': reviews,
                            'title': title,
                            'username': username,
                            'email': email,
                            'review': review,
                            })
