from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','listing','email','contact_date')
    #create links that lead back to the main listing entry, so they can be edited
    list_display_links = ('id','name')
    search_fields = ('name ','email','listing')
    list_per_page = 25
admin.site.register(Contact,ContactAdmin)