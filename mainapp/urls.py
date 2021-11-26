from django.urls import path
from  . import views

app_name='mainapp'
urlpatterns = [
     path('',views.cityweatherview, name='index'),
     path('remove/<city_name>',views.dltcity,name='remove')

]

