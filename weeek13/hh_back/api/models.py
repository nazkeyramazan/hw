from django.db import models

# Create your models here.
class Company (models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(default="Top Company")
    city = models.CharField(max_length=150 , default='Pavlodar')
    address = models.TextField(default='no information about address')

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'city' : self.city,
            'address' : self.address,
        }
class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField( default='There are no information about Company description please Update data with PUT method')
    salary = models.IntegerField(default=150000)
    company =  models.ForeignKey(Company ,on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'salary' : self.salary,
            'company' : self.company_id,
        }