from rest_framework import serializers
from myapp.models import Student, ClassRoom, StudentProfile

class ClassRoomSerializers(serializers.Serializer):
    id =serializers.IntegerField
    name= serializers.CharField()

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.ImageField()
    department = serializers.CharField()
    classroom = ClassRoomSerializers()

class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'

class StudentProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = '__all__'

class StudentModelSerializer(serializers.ModelSerializer):
    about_me = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        
    def get_about_me(self,obj): #obj is object of Student 
        return f"hello {obj.name}age{obj.age}"
    
    def get_address(self,obj):
        try:
            profile = obj.studentprofile.email
            print("address...",profile)
        except:
            profile = None
        return profile
    

    def get_fields(self):
        fields = super().get_fields()
        print("fields...,",fields)
        request = self.context.get("request")
        print(self.context)
        print("request...",request)
        if request and request.method =="GET":
            fields['classroom'] = ClassRoomModelSerializer()
        return fields
    
