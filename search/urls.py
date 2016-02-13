from django.conf.urls import patterns, url
from search import views

urlpatterns = patterns('',
    url(r'^$', 'search.views.search_view'),
    url(r'^restaurant/(?P<restaurant_id>\d+)', 'search.views.search_restaurant_view', name='restaurant'),
    url(r'^item/(?P<item_id>\d+)', 'search.views.item_view', name='item'),
    url(r'^item/addreview/(?P<item_id>\d+)', 'search.views.item_review', name='item_review'),
)
