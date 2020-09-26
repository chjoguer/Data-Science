from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pandas as pd
import numpy as np
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Sum
# Create your views here.

def index(request):
    stores = Tiendas.objects.all()
    stores_df = pd.DataFrame(Tiendas.objects.all().values())

    return render(request,"index.html",{'stores':stores})

def dashboard(request):
    lista = determinateKPI()
    cpi_no_holiday = determinateKPI_CPI()
    earnings = lista[0]
    loss = lista[1]

    return render(request,"dashboard.html",{"earnings":earnings,"loss":loss,"cpi":cpi_no_holiday})

def barview(request):
    return render(request,"barchart.html")

def lineview(request):
    return render(request,"line.html")


def dataTable(request):
    sales_list = Ventas_stores.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator( sales_list, 10)
    try:
        sale = paginator.page(page)
    except PageNotAnInteger:
        sale = paginator.page(1)
    except EmptyPage:
        sale = paginator.page(paginator.num_pages)
    return render(request,"dataTable.html", { 'sales': sale })


def population_linechart(request):
    queryset = Ventas_stores.objects.filter(Store=1,Date__range=["2010-01-01","2010-12-31"],IsHoliday='Verdadero')
    stores_df = pd.DataFrame(queryset.values())
    stores_mean =stores_df.groupby(by="Dept").mean()[0:35]
    label =stores_mean.iloc[:,0]
    list_label=list(label)
    size =stores_mean.iloc[:,2]
    list_size=list(size)
    stores_label = stores_mean.groupby('Dept').size().reset_index(name='count').iloc[:,0]
    list_store = list(stores_label) 

    determinateKPI()
    return JsonResponse(data={
        'labels': list_store,
        'data': list_size,
    })

def table(request):
    tiendas_list = Tiendas.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator( tiendas_list, 10)
    try:
        tienda = paginator.page(page)
    except PageNotAnInteger:
        tienda = paginator.page(1)
    except EmptyPage:
        tienda = paginator.page(paginator.num_pages)
    return render(request,"data-table.html", { 'tiendas': tienda })

def table_features(request):
    caracteristicas_list = Caracteristicas_final.objects.all()
    filter_date =  Caracteristicas_final.objects.all()
    page = request.GET.get('page', 1)
    inicio = request.GET.get('inicio', 'None')
    print(inicio)

    if request.POST.get('fecha_inicio', False) and request.POST.get('fecha_fin', False) !=False:
        filter_date =  filter_date.filter(Date__range=[request.POST['fecha_inicio'],request.POST['fecha_fin']])
        print(request.POST.get('isHoliday', False))
        print(filter_date)

    if request.POST.get('isHoliday', False) !=False :
        print(request.POST.get('isHoliday', False))
        #inicio = request.GET.get('inicio',request.POST['isHoliday'])
        filter_date= filter_date.filter(IsHoliday=request.POST['isHoliday'])      
    paginator = Paginator( filter_date, 10)

    try:
        carcateristicas = paginator.page(page)
    except PageNotAnInteger:
        carcateristicas = paginator.page(1)
    except EmptyPage:
        carcateristicas = paginator.page(paginator.num_pages)
    return render(request,"features-data.html", { 'tiendas': carcateristicas,"inicio":inicio })


def tableByCategory(request):
        tiendas_list = Tiendas.objects.all()
        A_list=None
        print(request.POST.get('category', False))
        if request.POST.get('category', False)!=False:
            A_list=tiendas_list.filter(types=request.POST['category'])
        else :
            A_list=tiendas_list.filter(types="B")

        page = request.GET.get('page', 1)
        print(page);
        paginator = Paginator( A_list, 50)
        try:
            tienda = paginator.page(page)
        except PageNotAnInteger:
            tienda = paginator.page(1)
        except EmptyPage:
            tienda = paginator.page(paginator.num_pages)

        return render(request,"data-table.html", { 'tiendas': tienda })

def listing_store(request):
    contact_list = Tiendas.objects.all()
    paginator = Paginator(contact_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})

def getSizeStore(request):
    stores = Tiendas.objects.all()
    stores_df = pd.DataFrame(Tiendas.objects.all().values())
    label =stores_df.iloc[:,0]
    list_label=list(label)
    size =stores_df.iloc[:,2]
    list_size=list(size)
    pair=list()
    pair.append(list_label)
    pair.append(list_size)
    print(pair)
    return JsonResponse(pair,safe=False)

def determinateKPI():
    lista = []
    #Promedio de ventas sin feriados
    queryset = Ventas_stores.objects.filter(Store=1,Date__range=["2010-01-01","2010-12-31"],IsHoliday='Verdadero')
    stores_df = pd.DataFrame(queryset.values())
    stores_mean =stores_df.groupby(by="Dept").mean()[0:35]
    value_mean_holidays = sum(stores_mean.iloc[:,2])
    formatted_float_holidays = "{:.2f}".format(value_mean_holidays)
    # print(formatted_float_holidays)
    lista.append(formatted_float_holidays)

    #Promedio de ventas sin feriados
    queryset2 = Ventas_stores.objects.filter(Store=1,Date__range=["2010-01-01","2010-12-31"],IsHoliday='Falso')
    stores_df2 = pd.DataFrame(queryset2.values())
    stores_mean2 =stores_df2.groupby(by="Dept").mean()[0:35]
    value_mean = sum(stores_mean2.iloc[:,2])
    asx= stores_mean2.iloc[:,2]
    formatted_float = "{:.2f}".format(value_mean)
    # print(formatted_float)
    lista.append(formatted_float)
    return lista;

def determinateKPI_CPI():
    #Promedio de indice de consumido sin feriados
    queryset = Caracteristicas_final.objects.filter(Date__range=["2010-01-01","2010-12-31"],IsHoliday='Falso')
    stores_df = pd.DataFrame(queryset.values())
    stores_mean =stores_df.groupby(by="IsHoliday").mean()
    value_mean_ipc = sum(stores_mean.iloc[:,8])
    formatted_float_ipc = "{:2.2f}".format(value_mean_ipc)
    return formatted_float_ipc;
    