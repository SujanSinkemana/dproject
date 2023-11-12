from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Student
from rest_framework import status
from api.serializers import StudentSerializers,StudentModelSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
def hello_api(request):
    return JsonResponse({
        "message":"first api"
    })

class info_api(APIView):
    def get(self,*args,**kwargs):
        return Response(
            {
                "id":1,
                "name":"age",
                "age":20,
                "dept":"IT"
            }
        ) # it returns list dict and list along the dict 
    
class InfoListView(APIView):
    def get(self,*args,**kwargs):
        return Response(
            [{"id":1,"name":"ram","dept":"IT"},
             {"id":1,"name":"sita","dept":"IT"}
            ])
    
class StudentView(APIView):
    def get(self,*args,**kwargs):
        try:
            s = Student.objects.get(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "mes":"Student Not"
            })
        return Response({
            "id":s.id,
            "name":s.name,
            "age":s.age,
            "department":s.department,
            "classroom":s.classroom.name if s.classroom else None
        })
    
class StudentListView(APIView):
    def get(self,*args,**kwargs):
        stu = Student.objects.all()
        response=[]
        for s in stu:
           response.append(dict(id=s.id,name=s.name,age=s.age,department=s.department))
        return Response(response)


            

        # response=[dict(name=s.name,age=s.age,department=s.department) for s in stu]
        # return Response(response)
       
         
                
class StudentAPiView(APIView):
    def get(self,*args,**kwargs):
        id =kwargs['id']
        try:
            student = Student.objects.all(id=kwargs['id'])
        except Student.DoesNotExist:
            return Response({
                "mes":"Student Not"
            },status=status.HTTP_404_NOT_FOUND)
        serializer= StudentModelSerializer(student)
        return Response(serializer.data)


def post(self,*args,**kwargs):
    serializer = StudentModelSerializer(data=self.request.data) #This is the object of serializer self in serializers.py method
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        age = serializer.validated_data.get('age')
        department = serializer.validated_data.get('department')
        classroom = serializer.validated_data.get('classroom')
        Student.objects.create(name=name,age=age,department=department)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# def post(self,*args,**kwargs):
#     serializer = StudentModelSerializer(data=self.request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class StudentListCreateView(APIView):
    def get(self,*arg,**kwargs): #get is serialization 
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True,context={"request":self.request})
        return Response(serializer.data)
    
    def post(self,*args,**kwargs):#post is deserialization
        serializer = StudentModelSerializer(data=self.request.data,context={"request":self.request})
        print("self.request POST....",self.request)
        print(self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class StudentListGenericView(ListAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()




class StudentCreateGenericView(CreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentListCreateGenericView(ListCreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['title']= 'Create and lIst Students'
        return context

class StudentRetriveGenericView(RetrieveAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

class StudentUpdateGenericView(UpdateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def partial_update(self, request, *args, **kwargs):
        super().partial_update(request, *args, **kwargs)
        return Response({
            "msg":"Update Sucessfull"
        })

class StudentDeleteGenericView(DestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return Response({
            "msg":"Delete"
        })
    
class StudentREUPDeGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = StudentModelSerializer
    # queryset = Student.objects.all()

    #get_query method is used to all extra logic if we use it we dont have to write queryset = Student.objects.all() above
    def get_queryset(self):
        return Student.objects.filter(department="IT")
    
