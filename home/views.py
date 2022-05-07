from django.shortcuts import render
from .models import *
from django.db.models import Avg, Max, Min, Sum, Count
# Create your views here.


def home(request):
    student_data = Student.objects.all()
    average = student_data.aggregate(Avg('marks'))
    total = student_data.aggregate(Sum('marks'))
    minimum = student_data.aggregate(Min('marks'))
    maximum = student_data.aggregate(Max('marks'))
    totalcount = student_data.aggregate(Count('marks'))
    print("return:", student_data)
    print()
    print("SQL Query:", student_data.query)
    con = {
        'average': average,
        'total': total,
        'minimum': minimum,
        'maximum': maximum,
        'totalcount': totalcount,
        'students': student_data,
        
    }
    return render(request, 'home.html', con)