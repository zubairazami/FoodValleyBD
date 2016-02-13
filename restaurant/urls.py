from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurant import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'restaurant.views.home_view'),
    url(r'^login/', 'restaurant.views.login_view'),
    url(r'^logout/', 'restaurant.views.logout_view'),
    url(r'^register/', 'restaurant.views.register_view'),
    url(r'^restaurant/$', 'restaurant.views.restaurant_view', name='restaurantinfo'),
    url(r'^restaurant/editdetails/$', 'restaurant.views.restaurant_edit_details_view', name='restauranteditdetails'),
    url(r'^restaurant/updateitems/$', 'restaurant.views.restaurant_update_items_view', name='restaurantupdateitems'),
    url(r'^search/', include('search.urls',namespace='search')),
    # url(r'^blog/', include('blog.urls')),
)
