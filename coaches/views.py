from django.shortcuts import render
from coaches.models import Coach
from courses.models import Course


def detail(request, c_id):
    c_id = int(c_id)
    coach = Coach.objects.get(id=c_id)
    return render(request, 'coaches/detail.html', {'coach': coach})
