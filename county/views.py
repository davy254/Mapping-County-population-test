from django.shortcuts import render
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import County
from django.views.generic import  TemplateView
from django.core.cache import cache
# Create your views here.
"""def county_view(request):
    county_geojson = serialize('geojson',County.objects.all())
    return JsonResponse(json.loads(county_geojson))
"""


def county_view(request):
    redis_key = 'county'
    county = cache.get(redis_key)  # getting value for given key from redis
    if not county:

        county = serialize('geojson', County.objects.all())
        cache.set(redis_key, county)  # if not GeoJSON is not in cache set it
    return JsonResponse(json.loads(county))


class MainPageView(TemplateView):
    template_name = 'county/main.html'
