from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from api.models import Company , Vacancy
from api.serializers import CompanyModelSerializer , VacancyWithCompanyModelSerializer , CompanySerializer , VacancyModelSerializer

@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanyModelSerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        company.delete()

        return Response({'deleted': True})

@api_view(['GET'])
def company_vacancies(request , company_id):
    try:
        company = Company.objects.get(id = company_id)
    except Company.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id = company_id)
        serializer = VacancyWithCompanyModelSerializer(vacancies, many= True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancyModelSerializer(vacancies , many= True)
        return Response(serializer.data)
    elif request.method =='POST':
        serializer = VacancyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancyModelSerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancyModelSerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()

        return Response({'deleted': True})

@api_view(['GET'])
def topten_vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        top_ten = vacancies.order_by('-salary')[:10]
        serializer = VacancyModelSerializer(top_ten, many=True)
        return Response(serializer.data)
