from data.models import *
import csv

'''Migrar Tiendas'''
# tiendas_csv = open('tiendas.csv', 'r', encoding = "utf-8") 
# reader = csv.reader(tiendas_csv)
# headers = next(reader, None)[1:]
# print("Tiendas")
# for row in reader:  
#    tiendas_dict = {}
#    for h, val in zip(headers, row[1:]):
#        tiendas_dict[h] = val
#    tiendas = Tiendas.objects.create(**tiendas_dict)
#  print(caracteristicas_dict)




'''Migrar Ventas'''
# caracteristicas_csv = open('caracteristicasbymo.csv', 'r', encoding = "utf-8") 
# reader = csv.reader(caracteristicas_csv)
# headers = next(reader, None)[1:]
# print("caracteristicas")
# for row in reader:  
#    caracteristicas_dict = {}
#    for h, val in zip(headers, row[1:]):
#        caracteristicas_dict[h] = val
#    caracteristicas = Caracteristicas_final.objects.create(**caracteristicas_dict)
#  print(caracteristicas_dict)

'''Migrar Ventas'''
# ventas_csv = open('ventasdate1.csv', 'r', encoding = "utf-8") 
# reader = csv.reader(ventas_csv)
# headers = next(reader, None)[0:]
# print("ventas")
# for row in reader:  
#    ventas_dict = {}
#    for h, val in zip(headers, row[0:]):
#       ventas_dict[h] = val
#    ventas = Ventas_stores.objects.create(**ventas_dict)
#    print(ventas_dict)



# filters = {}

# for key, value in request.post.items():
#     if key in ['filter1', 'filter2', 'filter3']:
#         filters[key] = value

# Test.objects.filter(**filters)
caracteristicas_csv.close()  