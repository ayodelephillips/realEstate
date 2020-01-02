from django.contrib import admin

# Register your models here.
from .models import  Listing

#this is used to define what can appear on the admoin page for listings
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    #create links that lead back to the main listing entry, so they can be edited
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title','description','address','city','state','zipcode','price')
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)