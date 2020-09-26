from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard , name='dashboard'),
    path('dashboard', views.dashboard , name='dashboard'),
    path('table', views.table , name='table'),
    path('getSizeStore', views.getSizeStore ),
    path('getByCategory', views.tableByCategory, name='getCategoryStore' ),
    path('table-features', views.table_features, name='table_features' ),

    path('bar', views.barview,name='bar' ),
    path('line-chart', views.lineview,name='line-chart' ),
    path('population-line/', views.population_linechart, name='population-line'),
    path('dataTable', views.dataTable,name='dataTable' ),


]