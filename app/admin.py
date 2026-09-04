from django.contrib import admin

from app.models import *
# Register your models here.

@admin.register(Book)
class book_admin(admin.ModelAdmin):
    list_display=['title','author','category','available_copies']
    search_fields=['title','author_name']
    list_filter=['category']
    raw_id_fields=['author','category']

@admin.register(Author)
class author_admin(admin.ModelAdmin):
    pass

@admin.register(Category)
class category_admin(admin.ModelAdmin):
    pass

@admin.register(Member)
class member_admin(admin.ModelAdmin):
    pass