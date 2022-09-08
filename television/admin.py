from re import T
from django.contrib import admin
from .models import Category,Television,Model

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Model,ModelAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')
admin.site.register(Category,CategoryAdmin)


class TelevisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category','color','descriptions','created_at','updated_at')
admin.site.register(Television,TelevisionAdmin)