from django.db import models
from django.conf import settings

# Create your models here.

class Tiendas(models.Model):
    TIPO_TIENDA = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    store = models.CharField(max_length=50,primary_key=True)
    types = models.CharField(max_length=1, choices=TIPO_TIENDA)
    size = models.IntegerField()

class Caracteristicas(models.Model):
    id_tienda_c = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    date = models.TextField()
    temperature =  models.FloatField()
    fuel_price =  models.FloatField()
    md1 =  models.CharField(max_length=50)
    md2 =  models.CharField(max_length=50)
    md3 =  models.CharField(max_length=50)
    md4 =  models.CharField(max_length=50)
    md5 =  models.CharField(max_length=50)
    cpi =  models.DecimalField(max_digits=20,decimal_places=2)
    unenemplyment = models.DecimalField(max_digits=20,decimal_places=2)
    is_holiday = models.CharField(max_length=50)

class Caracteristicas_store(models.Model):
    Store = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    Date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    Temperature = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    Fuel_Price = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown1 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown2 = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    MarkDown3 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown4 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown5 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    CPI = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    Unemployment = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    IsHoliday = models.TextField(blank=True, null=True)  # Field name made lowercase.

class Caracteristicas_final(models.Model):
    Store = models.FloatField( blank=True, null=True) 
    Date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    Temperature = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    Fuel_Price = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown1 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown2 = models.FloatField(blank=True, null=True)  # Field name made lowercase.
    MarkDown3 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown4 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    MarkDown5 = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    CPI = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    Unemployment = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    IsHoliday = models.TextField(blank=True, null=True)  # Field name made lowercase.

class Ventas_stores(models.Model):
    Store = models.IntegerField( blank=True, null=True) 
    Dept = models.IntegerField( blank=True, null=True) 
    Date = models.DateField( blank=True, null=True)  # Field name made lowercase.
    Weekly_Sales = models.FloatField( blank=True, null=True)  # Field name made lowercase.
    IsHoliday = models.TextField(blank=True, null=True)  # Field name made lowercase.




class Ventas(models.Model):
    id_tienda_v = models.ForeignKey(Tiendas, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100)
    date = models.TextField()
    weekly_sales = models.DecimalField(max_digits=20,decimal_places=2)
    isholiday = models.CharField(max_length=50,default='FALSE')

