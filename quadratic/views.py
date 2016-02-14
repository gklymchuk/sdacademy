# coding=utf-8

from django.shortcuts import render
from quadratic.models import Quadratic


def quadratic_results(request):
    a = request.GET.get('a', '')
    b = request.GET.get('b', '') 
    c = request.GET.get('c', '')
    q = Quadratic(a, b, c)
    return render(request, 'results.html', {'q': q})


