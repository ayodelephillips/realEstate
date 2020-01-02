from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import price_choices,bedroom_choices,state_choices
def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)# order by listz_date in descending manner. the earliest is 1st. and also filter to show only published ones
    paginator=Paginator(listings,6)  #allow for pagination
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings':paged_listings
    }

    return render(request,'listings/listings.html',context)

def listing(request, listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing': listing

    }
    return render(request,'listings/listing.html', context)

def search(request):
    print("into search")
    queryset_list=Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords) #select.... where description LIKE keywords

    #city search
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    #state search
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            queryset_list=queryset_list.filter(state__iexact=state)

    # # bedrooms search. search for houses with bedrooms up to the number of bedrooms specified in the search field
    if 'bedrooms' in request.GET:
        bedrooms=request.GET['bedrooms']
        if bedrooms:
            queryset_list=queryset_list.filter(bedrooms__lte=bedrooms) #lte means less than or equal

    # search for price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)  # lte means less than or equal

    context={
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listings':queryset_list,
        'values':request.GET,
    }
    return render(request,'listings/search.html',context)