from rest_framework import  serializers

from api.models import Company , Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company  = Company.objects.create(**validated_data)
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.description = validated_data.get('description' , instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data('address' , instance.address)
        instance.save()
        return instance

class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description' , 'city' , 'address',)

class VacancyModelSerializer(serializers.ModelSerializer):
    company = CompanyModelSerializer (read_only= True)
    company_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description' , 'salary' , 'company', 'company_id')

class VacancyWithCompanyModelSerializer(serializers.ModelSerializer):
    vacancies = VacancyModelSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'description' , 'city' , 'address', 'vacancies')

