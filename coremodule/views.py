from django.shortcuts import render
import requests
from django.contrib import messages
from .openwthr import get_weather
# Create your views here.
def home(request):
    city=request.POST.get('city')
    if city!=None:
        print(city)
        try:
           fetch_res=get_weather(city)
           print(fetch_res)
           weatherdb=dict()
           weatherdb['city']=fetch_res[0]
           weatherdb['weather']=fetch_res[1]
           weatherdb['weatherdes']=fetch_res[2]
           weatherdb['temp']=fetch_res[3]
           weatherdb['hum']=fetch_res[4]
           weatherdb['wind']=fetch_res[5]
           weatherdb['pressure']=fetch_res[6]
           weatherdb['feels_like']=fetch_res[7]
           weatherdb['temp_min']=fetch_res[8]
           weatherdb['temp_max']=fetch_res[9]
           return render(request,'index.html',{'weatherdb':weatherdb})
        except Exception as e :
            messages.error(request,'Enter Valid City')
            return render(request,'home.html')
            print(e)
            
    else:
        return render(request,'home.html')
