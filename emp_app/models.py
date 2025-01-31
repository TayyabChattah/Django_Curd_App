from django.db import models


class dept(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name
    

class Role(models.Model):
    name=models.CharField(max_length=100,null=False)         

    def __str__(self):
        return self.name                 
# Create your models here.
class Employe(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100,null=False)
    dept=models.ForeignKey(dept,on_delete=models.CASCADE)
    salary=models.IntegerField(default=0)
    bonous=models.IntegerField(default=0)
    Role=models.ForeignKey(Role,on_delete=models.CASCADE)
    Phone=models.IntegerField(default=0)
    hire_date=models.DateField()

    def __str__(self):
        return "%s %s %s %s"%(self.first_name,self.last_name,self.dept,self.Phone)