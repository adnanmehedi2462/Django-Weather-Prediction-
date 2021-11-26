
import requests
import json
from django.shortcuts import render,redirect,get_object_or_404
from .models import city
from .forms import cityform
from django.contrib import messages

# Create your views here.

def cityweatherview(request):
	url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b5814487140b02b7f56cae5a914841a3"
	if request.method=='POST':
		form = cityform(request.POST)
		if form.is_valid():
			newcity=form.cleaned_data['name']
			citycount=city.objects.filter(name=newcity).count()
			if citycount==0:
				r=r=requests.get(url.format(newcity)).json()
				if r['cod']==200:

					form.save()
					messages.success(request, 'Successfully added this city', extra_tags='alert')
					

				else:

					messages.error(request, 'The city we not Found in the world !!', extra_tags='alert')


				
			else:
				messages.error(request, 'Already added this city!!', extra_tags='alert')


		
	form=cityform()
	weather=[]
	City=city.objects.all().order_by('-id')
	for p in City:

		r=requests.get(url.format(p)).json()
		print(r)

		city_weather = {

			'city':p,
			'temparature':r['main']['temp'],
			'vis':r['visibility'],
			'con':r['sys']['country'],
			'wind':r['wind']['speed'],
			'feels_like':r['main']['feels_like'],
			'discription':r['weather'][0]['description'],
			'icon':r['weather'][0]['icon'],


		}
		weather.append(city_weather)
		print(weather)



	context={
	'weather':weather,
	'form':form


	}
	return render (request,'index.html',context)

def dltcity(request,city_name):
	citys=get_object_or_404(city,name=city_name)
	citys.delete()
	messages.success(request, 'deleted Successfully', extra_tags='alert')
	return redirect('mainapp:index')