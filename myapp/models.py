from django.db import models


# Create your models here.
class ClassRoom(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    department=models.CharField(max_length=50)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="classroom_students" ,null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class StudentProfile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)#we dont need related_name to define Modelname is default value of it
    email = models.EmailField()
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    image = models.FileField(upload_to='images',null=True,blank=True)

    def __str__(self):
        return f"profile of {self.student.name}"
    
class Publication(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    headline= models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

