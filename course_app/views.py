from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def home(request):
    course = Course.objects.all()
    context = {'course': course}
    return render(request, 'course/index.html',context)
def semselect(request):
    crs_id=request.GET['c_id']
    semester=Course.objects.get(course_id=crs_id)
    tot_sem=semester.no_of_sem
    sem_num=[]
    for i in range(1,tot_sem+1):
        sem_num.append(i)
    context={
        'sem_num':sem_num
    }
    return render(request, 'course/data.html',context)
def data(request):
    crs_id = request.GET['c_id']
    sem1= request.GET['smtr']
    stud=Student.objects.filter(course_id=crs_id,sem=sem1)
    sub=Subject.objects.filter(course_id=crs_id,sem=sem1)
    mark=Marktable.objects.filter(course_id=crs_id,sem=sem1)
    cnt=Marktable.objects.filter(course_id=crs_id,sem=sem1).count()
    sub_mark=Marktable.objects.filter(course_id=crs_id,sem=sem1).values('sub1','sub2','sub3','sub4')
    tot_mark=[]
    for i in range(cnt):
        a=0
        lis=list(sub_mark[i].values())
        for i in lis:
            a=a+int(i)
        tot_mark.append(a)
    print(tot_mark)  
    context={
        'subject':sub,
        'mark':mark,
        # 'tot_mark':tot_mark
    }
    return render(request, 'course/datatable.html',context)
