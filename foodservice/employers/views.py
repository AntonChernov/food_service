# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Employers

# Create your views here.


def all_employers(request):
    if request.metod == 'GET':
        args = {}
        if request.user.has_perm('add_employers'):
            employers = Employers.objects.filter(dismissed=False)
            if employers and len(employers) > 0:
                all_emp = [i.as_dict for i in employers]
                args['employers'] = all_emp
                args['error'] = False
                return JsonResponse(data=args, safe=False, content_type='application/json', status=200)
            else:
                args['error'] = True
                args['message'] = 'Працівникі не знайдені!'
                return JsonResponse(data=args, safe=False, content_type='application/json', status=404)
        else:
            args['error'] = True
            args['message'] = 'Користувач не має прав на перегляд працівників!'
            return JsonResponse(data=args, safe=False, content_type='application/json', status=404)
    else:
        args = {'error': True, 'message': 'Не допустимий тип запиту!'}
        return JsonResponse(data=args, safe=False,  content_type='application/json', status=400)


def employer_data(request, uid=None):
    if request.method == 'GET':
        args = {}
        if request.user.has_perm('change_employers'):
            try:
                emp = Employers.objects.get(id=uid)
                args['error'] = False
                args['employer'] = emp.as_dict()
                return JsonResponse(data=args, safe=False, content_type='application/json', status=200)
            except ObjectDoesNotExist:
                args['error'] = True
                args['message'] = 'Працівника не знайдені!'
                return JsonResponse(data=args, safe=False, content_type='application/json', status=404)
    else:
        args = {'error': True, 'message': 'Не допустимий тип запиту!'}
        return JsonResponse(data=args, safe=False, content_type='application/json', status=400)