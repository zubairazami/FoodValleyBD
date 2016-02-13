from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from restaurant.models import Restaurant, Item, Element
from django.db import IntegrityError


def home_view(request):
    return render(request, "home.html", {
        'menuhome': 'active'
    })


def register_view(request):
    if request.method == "GET":
        return render(request, "register.html", {
            'menuregister': 'active'
        })
    else:
        restaurant_name = request.POST.get("restaurant_name", None)
        username = request.POST.get("login", None)
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        proprietor_name = request.POST.get("proprietor", None)
        address = request.POST.get("address", None)
        district = request.POST.get("district", None)
        website = request.POST.get("website", None)
        latitude = request.POST.get("latitude", None)
        longitude = request.POST.get("longitude", None)
        if restaurant_name and username and email and password and proprietor_name and address and district and latitude and longitude:
            received_data = {
                            'restaurant': restaurant_name,
                            'login': username,
                            'email': email,
                            'password': password,
                            'proprietor': proprietor_name,
                            'address': address,
                            'district': district,
                            'website': website,
                            'latitude': latitude,
                            'longitude': longitude,
                            'errorclass': ' has-error', }
            try:
                new_user = User.objects.create_user(username, email, password)
                new_user.is_active = False
                new_user.save()
                obj, created = Restaurant.objects.get_or_create(login=new_user,
                            defaults={
                                'restaurant_name': restaurant_name,
                                'proprietor_name': proprietor_name,
                                'address': address,
                                'district': district,
                                'website': website,
                                'latitude': latitude,
                                'longitude': longitude,
                            })
                if not created:
                    new_user.delete()
                    messages.error(request, "\nFailed to register restaurant")
                    return render(request, "register.html", received_data)
                else:
                    messages.success(request, "\nRestaurant registration successful. Wait for admin's approval.")
                    return redirect("/")

            except IntegrityError:
                messages.error(request, "\nLogin already exists!! Try a different Login.")
                return render(request, "register.html", received_data)

        else:
            messages.error(request, "Please fill out the form properly.")
            return render(request, "register.html", {
                            'restaurant': restaurant_name,
                            'login': username,
                            'email': email,
                            'password': password,
                            'proprietor': proprietor_name,
                            'address': address,
                            'district': district,
                            'website': website,
                            'latitude': latitude,
                            'longitude': longitude, })


def login_view(request):
    if request.user.is_authenticated():
        return redirect("/")

    if request.method == "GET":
        return render(request, "login.html", {
            'menulogin': 'active'
        })
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/restaurant')
            else:
                messages.error(request, "Your account is not active yet, wait for the admin's approval.")
                return redirect("/")
        else:
            messages.error(request, "Wrong username or password. Retry")
            return redirect("/login")


def logout_view(request):
    logout(request)
    messages.success(request, "You're now logged out successfully!")
    return redirect("/login")


def restaurant_view(request):
    if request.user.is_authenticated:
        user = auth.get_user(request)
        if user.is_anonymous():
            messages.error(request, "You have to login first to access any Resturant Management Panel.")
            return redirect("/login")
        queryset = Restaurant.objects.filter(login=user)
        if not queryset:
            messages.error(request, "There is no restaurant under your login. Contact the admins !! ")
            return redirect("/")
        else:
            return render(request, "restaurant.html", {
                'restaurant': queryset[0]
            })
    else:
        messages.error(request, "You have to login first to access any Resturant Management Panel.")
        return redirect("/login")


def restaurant_edit_details_view(request):
    if request.user.is_authenticated:
        user = auth.get_user(request)
        if user.is_anonymous():
            messages.error(request, "You have to login first to access any Resturant Management Panel.")
            return redirect("/login")
        queryset = Restaurant.objects.filter(login=user)
        if not queryset:
            messages.error(request, "There is no restaurant under your login. Contact the admins !! ")
            return redirect("/")
        else:
            if request.method == 'GET':
                return render(request, "editrestaurant.html", {
                    'restaurant': queryset[0]
                })
            else:
                restaurant_name = request.POST.get("restaurant_name", None)
                proprietor_name = request.POST.get("proprietor", None)
                address = request.POST.get("address", None)
                district = request.POST.get("district", None)
                website = request.POST.get("website", None)
                latitude = request.POST.get("latitude", None)
                longitude = request.POST.get("longitude", None)

                if restaurant_name and proprietor_name and address and district and latitude and longitude:
                    received_data = {
                                    'restaurant': restaurant_name,
                                    'proprietor': proprietor_name,
                                    'address': address,
                                    'district': district,
                                    'website': website,
                                    'latitude': latitude,
                                    'longitude': longitude,
                                    }
                    try:
                        restaurant_object = Restaurant.objects.get(login=user)
                        restaurant_object.restaurant_name = restaurant_name
                        restaurant_object.proprietor_name = proprietor_name
                        restaurant_object.address = address
                        restaurant_object.district = district
                        restaurant_object.website = website
                        restaurant_object.latitude = latitude
                        restaurant_object.longitude = longitude
                        restaurant_object.save()
                        messages.success(request, "\nRestaurant informations updated successfully.")
                        return redirect("/restaurant")

                    except Exception:
                        messages.error(request, "\nError while updating. ")
                        return render(request, "editrestaurant.html", received_data)
    else:
        messages.error(request, "You have to login first to access any Resturant Management Panel.")
        return redirect("/login")


def restaurant_update_items_view(request):
    if request.user.is_authenticated:
        user = auth.get_user(request)
        if user.is_anonymous():
            messages.error(request, "You have to login first to access any Resturant Management Panel.")
            return redirect("/login")

        logged_in_restaurant=Restaurant.objects.filter(login=user)[0]

        restaurant_items = Item.objects.filter(restaurant=logged_in_restaurant)
        all_elements = Element.objects.all()

        if request.method == 'GET':
            return render(request, 'updateitems.html', {'items': restaurant_items, 'elements': all_elements, })
        else:
            if 'addbutton' in request.POST:
                item_name = request.POST.get('item_name')
                price = request.POST.get('price')
                element_list = request.POST.get('element_list')
                element_list = element_list.split(',')

                try:
                    new_item = Item.objects.create(item_name=item_name, price=price, restaurant=logged_in_restaurant)
                    new_item.save()
                    for element in element_list:
                        el = Element.objects.get_or_create(element_name=element)[0]
                        el.item.add(new_item)
                    messages.success(request, "Item added successfully.")
                    return redirect('/restaurant/updateitems')
                except Exception as e:
                    messages.error(request, "\nError while updating.\n"+e.message)
                    return render(request, "editrestaurant.html", {'items': restaurant_items, 'elements': all_elements, })

            if 'deletebutton' in request.POST:
                try:
                    selected_item = request.POST.get("delete_select", None)
                    if selected_item:
                        to_be_deleted = Item.objects.filter(item_id=int(selected_item))
                        to_be_deleted.delete()
                        messages.success(request,"Selected items deleted successfully.")
                    else:
                        messages.error(request,"No Item selected to delete.")
                    return redirect('/restaurant/updateitems')
                except Exception as e:
                    messages.error(request,e.message)
                    return redirect('/restaurant/updateitems')

            else:
                return redirect("/")
                
    else:
        messages.error(request, "You have to login first to access any Resturant Management Panel.")
        return redirect("/login")
