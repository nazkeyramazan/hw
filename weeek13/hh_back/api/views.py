from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Company , Vacancy
from api.serializers import CompanySerializer ,CompanyModelSerializer
# Create your views here.

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies , many=True)
        return JsonResponse(serializer.data , safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

@csrf_exempt
def company_detail(request ,company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})

    if request.method == 'GET':
        serializer  = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data = request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})



def company_vacancies(request , company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})

    vacancies = company.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json , safe= False)

def vacancy_list(request):
    try:
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error' : 'there are no vacancies'})
    return JsonResponse(vacancies_json , safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())

def topten_vacancies(request):
    try:
        vacancies = Vacancy.objects.all()
        top_ten = vacancies.order_by('-salary')
        top_ten_json = [top.to_json() for top in top_ten]
    except Vacancy.DoesNotExist:
        return JsonResponse ({'Error':'There are no 10 vacancies'})
    return JsonResponse(top_ten_json ,safe=False)