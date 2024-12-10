from django.contrib import admin
from jpapp.models import BangJobs,HydJobs,PuneJobs
# Register your models here.
class Bangadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(BangJobs,Bangadmin)
class Hydadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(HydJobs,Hydadmin)
class Puneadmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']
admin.site.register(PuneJobs,Puneadmin)