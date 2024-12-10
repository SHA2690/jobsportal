import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobsportal.settings')
import django
django.setup()

from jpapp.models import HydJobs,BangJobs,PuneJobs
from faker import Faker
from random import *
fake = Faker()
def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Associate Engineer'))
        feligibility = fake.random_element(elements = ('B.Tech','MCA','M.Tech','Mahesh Sir Student','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        hyd_jobs_records = HydJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
        bang_jobs_records = BangJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
        pune_jobs_records = PuneJobs.objects.get_or_create(
            date = fdate,
            company = fcompany,
            title = ftitle,
            eligibility = feligibility,
            address = faddress,
            email = femail,
            phonenumber = fphonenumber,
        )
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully..........')