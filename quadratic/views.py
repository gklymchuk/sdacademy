# coding=utf-8

from django.shortcuts import render
from quadratic.models import Quadratic
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            a = data['a']
            b = data['b']
            c = data['c']
            q = Quadratic(a, b, c)
            context = {'q': q, 'form': form}
            return render(request, 'quadratic/results.html', context)
        return render(request, 'quadratic/results.html', {'form': form})
    else:
        form = QuadraticForm()
        return render(request, 'quadratic/results.html', {'form': form})
