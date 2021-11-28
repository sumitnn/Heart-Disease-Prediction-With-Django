from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name="index"),
    path('prediction/', WinePredict, name="winepredict"),
    path('output/', Output, name="output")
]
