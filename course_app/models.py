from django.db import models

# Create your models here.
class Course(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=150,null=False,blank=False)
    no_of_sem=models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.course_name
    
class Subject(models.Model):
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    sub_id=models.IntegerField(primary_key=True)
    sub_name=models.CharField(max_length=200,null=False,blank=False)
    sem=models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.sub_name

class Student(models.Model):
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    entrl_no=models.IntegerField(primary_key=True)
    stud_name=models.CharField(max_length=200,null=False,blank=False)
    sem=models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.stud_name


class Marktable(models.Model):
    course_id=models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    sub1=models.CharField(max_length=200,null=True)
    sub2=models.CharField(max_length=200,null=True)
    sub3=models.CharField(max_length=200,null=True)
    sub4=models.CharField(max_length=200,null=True)
    sem=models.IntegerField(blank=False, null=False)
