from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Цей проєкт було створено в рамках виконання лабораторної роботи с метою набуття та закріплення теоретичних знань та практичних навичок з користування Django. '
                        'Виконав Костерний В.О.') 

def cv(request):
    return render(request, 'cv.html')
