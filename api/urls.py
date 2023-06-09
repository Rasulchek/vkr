from django.urls import path
from api.views import lrpSolve
from api.views import abmSolve
from api.views import lkpTestPrim
from api.views import lkpTestMulPrim
from api.views import lkpPower
from api.views import calcelem
from api.views import lkpSolve
from api.views import bbsSolve
from api.views import bbsMillerRabin
from api.views import sealSolve
from api.views import sealEncr
from api.views import sealDecr

urlpatterns = [
    path('lrp', lrpSolve),
    path('abm', abmSolve),
    path('lkpTPr', lkpTestPrim),
    path('lkpTMPr', lkpTestMulPrim),
    path('lkpPow', lkpPower),
    path('calcel', calcelem),
    path('lkp', lkpSolve),
    path('bbs', bbsSolve),
    path('bbsmr', bbsMillerRabin),
    path('seal', sealSolve),
    path('sealencr', sealEncr),
    path('sealdecr', sealDecr),

]
