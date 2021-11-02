from rest_framework import serializers
from student.models import Student


# class FileListSerializer ( serializers.Serializer ) :
#     documents = serializers.ListField(
#                        child=serializers.FileField( max_length=100000,
#                                          allow_empty_file=False)
#                                 )
#     def create(self, validated_data):
#         # blogs=Student.objects.latest('created_at')
#         image=validated_data.pop('documents')
#         for img in image:
#             photo=StudentFile.objects.create(documents=img,**validated_data)
#         return photo

# class StudentFileSerializer(serializers.ModelSerializer):
#     documents = serializers.FileField(max_length=None, required=False)

#     class Meta:
#         model = StudentFile
#         fields = ['id','student','documents']

class StudentSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(required = False)
    # documents = StudentFileSerializer(many=True)
    passport = serializers.FileField(max_length=None, required=False)
    academic_transcript = serializers.FileField(max_length=None, required=False)
    ielts = serializers.FileField(max_length=None, required=False)
    sop = serializers.FileField(max_length=None, required=False)
    cv = serializers.FileField(max_length=None, required=False)
    reference = serializers.FileField(max_length=None, required=False)
    work_experience = serializers.FileField(max_length=None, required=False)
    visa = serializers.FileField(max_length=None, required=False)
    application_screenshot = serializers.FileField(max_length=None, required=False)
    other = serializers.FileField(max_length=None, required=False)

    class Meta:
        model = Student
        fields=['id','name','profile_image','email','password','phone','address','gender','academic','percentage','english','intake','level','status','university','course','amount_paid','passport_number','recommendation','passport','academic_transcript',
    'ielts',
    'sop',
    'cv',
    'reference',
    'work_experience',
    'visa',
    'application_screenshot',
    'other']