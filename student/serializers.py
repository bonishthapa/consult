from rest_framework import serializers
from student.models import Student
from user.serializers import UserSerializer


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            print("key",key)
            print("data",data)
            if val == data:
                print("val",val)
                return key
        self.fail('invalid_choice', input=data)
        
class StudentSerializer(serializers.ModelSerializer):
    gender = ChoiceField(choices=Student.GENDER_CHOICES, required=False)
    level = ChoiceField(choices=Student.LEVEL_CHOICES, required=False)
    status = ChoiceField(choices=Student.STATUS_CHOICES, required=False)
    profile_image = serializers.ImageField(required=False)
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
    payment_receipt = serializers.FileField(max_length=None, required=False)
    application_form = serializers.FileField(max_length=None, required=False)
    citizenship = serializers.FileField(max_length=None, required=False)
    created_by = UserSerializer(required=False)
    updated_by = UserSerializer(required=False)

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "profile_image",
            "actual_email",
            "email",
            "password",
            "phone",
            "dob",
            "address",
            "gender",
            "academic",
            "percentage",
            "english",
            "intake",
            "level",
            "status",
            "university",
            "course",
            "amount_paid",
            "passport_number",
            "recommendation",
            "remarks",
            "passport",
            "academic_transcript",
            "ielts",
            "sop",
            "cv",
            "reference",
            "work_experience",
            "visa",
            "application_screenshot",
            "other",
            "payment_receipt",
            "application_form",
            "citizenship",
            "created_by",
            "updated_by"
        ]
        read_only_fields=['created_at','updated_at''created_by','updated_by']

