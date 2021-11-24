import os
from django.db import models
from django.dispatch import receiver

# Create your models here.
GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]
LEVEL_CHOICES=[
    ('Undergraduate','Undergraduate'),
    ('Postgraduate','Postgraduate'),
    ('Phd','Phd'),
]
STATUS_CHOICES=[
    ('File Submitted','File Submitted'),
    ('Conditional Offer','Conditional Offer'),
    ('Unconditional Offer','Unconditional Offer'),
    ('Offer rejected','Offer rejected'),
    ('Deposit Paid','Deposit Paid'),
    ('Interview','Interview'),
    ('CAS Requested','CAS Requested'),
    ('CAS Issued','CAS Issued'),
    ('VFS Appointment','VFS Appointment'),
    ('Visa Granted','Visa Granted'),
    ('Visa Rejected','Visa Rejected'),
]

# def filefolder_path(instance, filename):
#     return f"{instance.name}/{filename}"  


class Student(models.Model):
    name = models.CharField(max_length=100, blank=False)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    actual_email = models.EmailField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, blank=True, null=True)
    academic = models.CharField(max_length=200, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)
    english = models.CharField(max_length=30, blank=True, null=True) 
    intake = models.CharField(max_length=50, blank=True, null=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES,blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)
    university = models.CharField(max_length=200, blank=True, null=True)
    course = models.CharField(max_length=200, blank=True, null=True)
    amount_paid = models.CharField(max_length=20, blank=True, null=True)
    passport_number = models.CharField(max_length=20, blank=True, null=True)
    recommendation = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    passport = models.FileField(upload_to='documents', blank=True, null=True)
    academic_transcript = models.FileField(upload_to='documents', blank=True, null=True)
    ielts = models.FileField(upload_to='documents', blank=True, null=True)
    sop = models.FileField(upload_to='documents', blank=True, null=True)
    cv = models.FileField(upload_to='documents', blank=True, null=True)
    reference = models.FileField(upload_to='documents', blank=True, null=True)
    work_experience = models.FileField(upload_to='documents', blank=True, null=True)
    visa = models.FileField(upload_to = 'documents', blank=True, null=True)
    application_screenshot = models.FileField(upload_to='documents', blank=True, null=True)
    other = models.FileField(upload_to='documents', blank=True, null=True)
    payment_receipt = models.FileField(upload_to='documents', blank=True, null=True)
    application_form = models.FileField(upload_to='documents', blank=True, null=True)
    citizenship = models.FileField(upload_to='documents', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']    

@receiver(models.signals.post_delete, sender=Student)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.profile_image:
        if os.path.isfile(instance.profile_image.path):
            os.remove(instance.profile_image.path)

    if instance.visa:
        if os.path.isfile(instance.visa.path):
            os.remove(instance.visa.path)

    if instance.passport:
        if os.path.isfile(instance.passport.path):
            os.remove(instance.passport.path)

    if instance.academic_transcript:
        if os.path.isfile(instance.academic_transcript.path):
            os.remove(instance.academic_transcript.path)

    if instance.ielts:
        if os.path.isfile(instance.ielts.path):
            os.remove(instance.ielts.path)

    if instance.sop:
        if os.path.isfile(instance.sop.path):
            os.remove(instance.sop.path)                                        

    if instance.cv:
        if os.path.isfile(instance.cv.path):
            os.remove(instance.cv.path)

    if instance.reference:
        if os.path.isfile(instance.reference.path):
            os.remove(instance.reference.path)

    if instance.work_experience:
        if os.path.isfile(instance.work_experience.path):
            os.remove(instance.work_experience.path)        

    if instance.application_screenshot:
        if os.path.isfile(instance.application_screenshot.path):
            os.remove(instance.application_screenshot.path)

    if instance.other:
        if os.path.isfile(instance.other.path):
            os.remove(instance.other.path)        



@receiver(models.signals.pre_save, sender=Student)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False    