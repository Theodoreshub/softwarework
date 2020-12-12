from django.contrib import admin

# Register your models here.

from .models import GoodInfo, GoodType

@admin.register(GoodInfo)
class GoodInfoAdmin(admin.ModelAdmin):
    list_display = ['id','gname','gtype','gintro','gprice','gcount','gstate']
    list_editable = ['gcount',]
    list_per_page = 10
    list_display_links = ('gname',)
    search_fields = ['gname','gtype',]
    ordering = ('id',)

@admin.register(GoodType)
class GoodTypeAdmin(admin.ModelAdmin):
    list_display = ['id','gtname',]
    list_display_links = ('gtname',)
    list_per_page = 10
    search_fields = ('gtname',)
