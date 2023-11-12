from rest_framework.viewsets import ModelViewSet
from api.serializers import StudentModelSerializer, ClassRoomModelSerializer, StudentProfileModelSerializer
from myapp.models import Student, ClassRoom, StudentProfile
from rest_framework.decorators import action #action is only for viewset
from rest_framework.response import Response

class StudentModelViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset =Student.objects.all()
    
    @action(detail=True)
    def profile(self,*args,**kwargs):
        student = self.get_object() # or Student.objects.get(id=id)
        try:
            profile = student.studentprofile
        except:
            return Response({"detail":"No profile"}, status=400)
        serializer = StudentProfileModelSerializer(profile)
        return Response(serializer.data)
    
    # @action(detail=True)
    # def classroom(self,*args,**kwargs):
    #     student = self.get_object()
    #     classroom = student.classroom_students
    #     serializer = ClassRoomModelSerializer(classroom, many=True)
    #     return Response(serializer.data)
    
class ClassRoomModelViewSet(ModelViewSet):
    serializer_class = ClassRoomModelSerializer
    queryset =ClassRoom.objects.all()

    @action(detail=True)
    def student(self,*args,**kwargs):
        classroom = self.get_object()
        stu = classroom.classroom_students.all()
        serializer = ClassRoomModelSerializer(stu, many=True)
        return Response(serializer.data)
    
class StudentProfileModelViewSet(ModelViewSet):
    serializer_class=StudentProfileModelSerializer
    queryset=StudentProfile.objects.all()
