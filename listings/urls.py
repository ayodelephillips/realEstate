from django.urls import path
from . import views

#we need the first url to have the '' so it pertains to /listings. the index method in listings returns a list of all the listings
#for the second one, we need it to act like /listings/id e.g. /listings/23. to get the 23rd listing. into the url, we put the parameters. method lising returns an individual listing
urlpatterns=[
    path('',views.index, name='listings'),
    path('<int:listing_id>',views.listing, name='listing'),
    path('search',views.search, name='search')

]