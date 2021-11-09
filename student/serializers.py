from rest_framework import serializers
from student.models import Student


class StudentSerializer(serializers.ModelSerializer):
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

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "profile_image",
            "email",
            "password",
            "phone",
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
        ]