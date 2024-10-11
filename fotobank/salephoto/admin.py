from django.contrib import admin
from .models import Photo,Category

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','date_taken')
    list_display_links = ('title',)
    search_fields = ('title','keywords')
    list_filter = ('date_taken','category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_display_links = ('id','title')
    search_fields = ('title',)

# Register your models here.
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category,CategoryAdmin)
