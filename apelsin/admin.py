from django.contrib import admin
from django.contrib.auth.models import Group,User

from .models import Phone,Category,Model

admin.site.unregister(Group)
admin.site.unregister(User)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Model,ModelAdmin)

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','ram','rom','color','descriptions','created_at','updated_at')
admin.site.register(Phone,PhoneAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Category,CategoryAdmin)