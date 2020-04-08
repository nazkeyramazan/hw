from django.shortcuts import render
from api.models import Company , Vacancy
from django.http.response import JsonResponse
from django.http import Http404
# Create your views here.

def company_list(request):
    try:
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
    except Company.DoesNotExist as e:
        return JsonResponse ({'ERROR': str(e)})
    return JsonResponse(companies_json , safe=False)

def company_detail(request ,company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'Error': str(e)})
    return JsonResponse(company.to_json())

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