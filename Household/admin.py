from django.contrib import admin
from .models import Category,Household,Model


class ModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Model,ModelAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Category,CategoryAdmin)


class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','color','descriptions','created_at','updated_at')
admin.site.register(Household,HouseholdAdmin)