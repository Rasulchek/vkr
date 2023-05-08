from django.urls import path, include
from mysite.views import LRP, LKP, BBS, SEAL, ABM

urlpatterns = [
    path('LRP/', LRP, name='LRP'),
    path('LKP/', LKP, name='LKP'),
    path('BBS/', BBS, name='BBS'),
    path('SEAL/', SEAL, name='SEAL'),
    path('ABM/', ABM, name='ABM'),
    path('api/v1/', include('api.urls')),
]
