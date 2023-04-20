from django.shortcuts import render
from django.http import JsonResponse

from .utils import getCityList

def index_view(request):
  if request.method=="GET":
    context = {
      "status":200,
      "message":"Select any city to visit",
      "popular": ("Srinagar","Rajkot","Pune","Bengaluru","Hyderabad","Bhilai","Lucknow","Asansol","Jamshedpur","Agartala","Nashik","Ludhiana","Meerut","Varanasi","Kanpur","Agra","Gwalior","Kochi","Kannur","Chennai","Madurai","Rajkot","Pune","Bengaluru","Hyderabad","Bhilai","Lucknow","Asansol","Jamshedpur","Chennai")
    }
    return render(request, "CORE/index.html", context)


def index_api(request, city):
  if request.method=="GET":
    context = {
      "status":200,
      "message":"Sucessful",
      "tourist_places": getCityList(city)
    }
    return JsonResponse(context)