from django.urls import path
from api.views import lrpSolve


urlpatterns = [
    path('lrp', lrpSolve),
]