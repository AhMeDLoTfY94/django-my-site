from django.db import models

class Female(models.Model):
          name_female=models.CharField(max_length=50)
          
class Male(models.Model):
          name_male=models.CharField(max_length=50)
          girl=models.OneToOneField(Female,on_delete=models.CASCADE)
          
class Login(models.Model):
          username=models.CharField(max_length=50)
          password=models.CharField(max_length=50)
          
          def __str__(self):
                    return self.username