from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from restaurant.models import *

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(Restaurant)
admin.site.register(Element)
admin.site.register(Item)
admin.site.register(ItemReview)


class ModifiedUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Email info'), {'fields': ('email')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        )
admin.site.site_title = 'Food Valley BD'
admin.site.site_header = 'Food Valley BD Administration'
admin.site.register(User, UserAdmin)
# admin.site.index_title = ''  #if commented then default is 'Site Administration'
