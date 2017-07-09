# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employers

# Create your views here.


def all_employers(request):
    if request.metod == 'GET':
        employers = Employers.objects.all()
    else:
        args = {'error': True, 'message': 'Не допустимий тип запиту!'}
        return JsonResponse(data=args, safe=False,  content_type='application/json', status=400)