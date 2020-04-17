
from django.urls import path
from api.views_fbv import company_list , company_detail, vacancy_list, vacancy_detail , topten_vacancies, company_vacancies
#from api.views import company_list , company_detail ,company_vacancies ,vacancy_list , vacancy_detail , topten_vacancies

from api.views_cbv import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
     # path('login/', obtain_jwt_token),
     # path('companies/', CompanyListAPIView.as_view(), name = 'company list'),
     # path('companies/<int:company_id>/', CompanyDetailAPIView.as_view(),name = 'company details'),
     # path('companies/<int:company_id>/vacancies/' , CompanyVacanciesAPIView.as_view() ),
     # path('vacancies/' ,VacancyListAPIView() ),
     # path('vacancies/<int:vacancy_id>/' ,VacancyDetailAPIView() ),
     # path('vacancies/top_ten/' ,TopTenVacanciesAPIView() ),

      path('login/', obtain_jwt_token),

     path('companies/' ,company_list ),
     path('companies/<int:company_id>/' ,company_detail ),
     path('companies/<int:company_id>/vacancies/' ,company_vacancies ),
     path('vacancies/' ,vacancy_list ),
     path('vacancies/<int:vacancy_id>/' ,vacancy_detail ),
     path('vacancies/top_ten/' ,topten_vacancies ),
]
