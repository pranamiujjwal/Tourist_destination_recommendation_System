from django.urls import path

from .views import *

app_name = "CORE"

urlpatterns = [
  path('index/', index_view ,name="indexView"),
  path('index/search/<str:city>/', index_api ,name="indexApi"),
]
