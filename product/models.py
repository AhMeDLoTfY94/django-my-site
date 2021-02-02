from django.db import models

class Product(models.Model):
          x=[
                    ('phone','phone'),
                    ('computer','computer')
          ]
          name   =models.CharField(max_length=50)
          content=models.TextField()
          price  =models.DecimalField(max_digits=5,decimal_places=4)
          image  =models.ImageField(upload_to='photos/%y/%m/%d')
          category=models.CharField(max_length=50,null=True,choices=x)
          active =models.BooleanField(default=True)
          
          def __str__(self):
                    return self.name
          class Meta:
                    ordering=["name"]

