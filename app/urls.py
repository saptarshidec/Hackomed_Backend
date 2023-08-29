from django.urls import path, include
from .views import *

urlpatterns = [
    path('predict/',PredictionView.as_view()),
]