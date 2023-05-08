from django.shortcuts import render


def LRP(request):
    return render(request, 'LRP.html')


def LKP(request):
    return render(request, 'LKP.html')


def BBS(request):
    return render(request, 'BBS.html')


def SEAL(request):
    return render(request, 'SEAL.html')

def ABM(request):
    return render(request, 'ABM.html')
