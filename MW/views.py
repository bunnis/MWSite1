from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse
from .models import Site, Value

def index(request):
    listSites = Site.objects.all()
    context = {'listaSites' : listSites}
    return render(request, 'index.html', context)

def summary(request):
    sites = Site.objects.all()
    sum_a_aux = 0
    sum_b_aux = 0
    sum_a = {}
    sum_b = {}


    for site in sites:
        values_list = Value.objects.filter(site=site)
        for value in values_list:
                sum_a_aux = sum_a_aux + value.value_A
                sum_b_aux = sum_b_aux + value.value_B

        if(len(values_list) != 0):
            sum_a[site] = sum_a_aux
            sum_b[site] = sum_b_aux
            sum_a_aux = 0
            sum_b_aux = 0

    context = {'sites': sites, 'sum_a': sum_a, 'sum_b': sum_b}
    return render(request, 'summary.html', context)

def summary_average(request):
    sites = Site.objects.all()

    sum_a_aux = 0
    sum_b_aux = 0
    average_a = {}
    average_b = {}
    count = 0

    for site in sites:
        values_list = Value.objects.filter(site=site)
        for value in values_list:
            if value.site == site:
                sum_a_aux = sum_a_aux + value.value_A
                sum_b_aux = sum_b_aux + value.value_B
                count = count + 1

        if(len(values_list) != 0):
            average_a[site] = sum_a_aux/count
            average_b[site] = sum_b_aux/count
            count = 0
            sum_a_aux = 0
            sum_b_aux = 0


    context = {'sites': sites, 'average_a': average_a, 'average_b': average_b}
    return render(request, 'summary_average.html', context)

def site_details(request, site_id):
    site = get_object_or_404(Site, pk=site_id)
    values_list = Value.objects.filter(site=site).order_by('pub_date')
    values_list_site = []

    for value in values_list:
            values_list_site.append(value)

    context = {'site': site, 'values_list_site': values_list_site}
    return render(request, 'site_details.html', context)

