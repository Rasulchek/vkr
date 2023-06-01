import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from api.LRP_functions import Lrp
from api.Berlicamp_Messi3 import Berlicamp_Messi3
from api.Berlicamp_Messi2 import Berlicamp_Messi2
from api.LKP_functions import testprimitivedeg
from api.LKP_functions import test_multip_prim
from api.LKP_functions import lkp_power
from api.LKP_functions import calc_arbitrary_el
from api.LKP_functions import calculate_lkp
from api.BBS_functions import bbs_generator


@csrf_exempt
@require_http_methods(["POST"])
def lrpSolve(request, **kwargs):
    data = json.loads(request.body)
    pol1 = data.get('pol1')
    pol0 = data.get('pol0')

    k, d, L, L2, alpha, c = Lrp(pol1, pol0)

    data = {
        'k': k,
        'd': d,
        'L': L,
        'L2': L2,
        'alpha': alpha,
        'c': c,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def abmSolve(request, **kwargs):
    data = json.loads(request.body)
    G = data.get('G')
    p = data.get('p')

    if int(p) == 3:
        l, k, g_list, h_list, m_list, b_list, L = Berlicamp_Messi3(G)
    else:
        l, k, g_list, h_list, m_list, b_list, L = Berlicamp_Messi2(G)
    data = {
        'l': l,
        'k': k,
        'g_list': g_list,
        'h_list': h_list,
        'm_list': m_list,
        'b_list': b_list,
        'L': L
    }
    print(data)
    print(p)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def lkpTestPrim(request, **kwargs):
    data = json.loads(request.body)
    a = data.get('a')
    p = data.get('p')
    e = data.get('e')

    massage = testprimitivedeg(a, p, e)
    data = {
        'massage': massage,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def lkpTestMulPrim(request, **kwargs):
    data = json.loads(request.body)
    a = data.get('a')
    c = data.get('c')
    m = data.get('m')

    massage1, massage2, massage3 = test_multip_prim(a, c, m)
    data = {
        'massage1': massage1,
        'massage2': massage2,
        'massage3': massage3,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def lkpPower(request, **kwargs):
    data = json.loads(request.body)
    a = data.get('a')
    m = data.get('m')

    test, power = lkp_power(a, m)
    data = {
        'power': power,
        'test': test,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def calcelem(request, **kwargs):
    data = json.loads(request.body)
    a = data.get('a')
    c = data.get('c')
    m = data.get('m')
    unkn_num = data.get('unkn_num')
    kn_num = data.get('kn_num')
    kn_el = data.get('kn_el')

    test, unkn_el = calc_arbitrary_el(a, c, m, kn_el, kn_num, unkn_num)
    data = {
        'test': test,
        'unkn_el': unkn_el,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def lkpSolve(request, **kwargs):
    data = json.loads(request.body)
    x = data.get('x')
    a = data.get('a')
    c = data.get('c')
    m = data.get('m')
    l = data.get('l')

    L = calculate_lkp(x, a, c, m, l)
    data = {
        'L': L,
    }
    print(data)
    return JsonResponse(data, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def bbsSolve(request, **kwargs):
    data = json.loads(request.body)
    p = data.get('p')
    q = data.get('q')
    seed = data.get('seed')
    l = data.get('l')

    L = bbs_generator(p, q, seed, l)
    data = {
        'L': L,
    }
    print(p, q)
    return JsonResponse(data, safe=False)
