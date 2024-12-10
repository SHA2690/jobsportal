from django.shortcuts import render
from jpapp.models import BangJobs,HydJobs,PuneJobs
# Create your views here.
def home(request):
    
    return render(request,'home.html')

def bang_jobs(request):
    jobs_list=BangJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'bang.html',mydict)

def hyd_jobs(request):
    jobs_list=HydJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'hyd.html',mydict)

def pune_jobs(request):
    jobs_list=PuneJobs.objects.all()
    mydict={'jobs_list':jobs_list}
    return render(request,'pune.html',mydict)