import os
from django.db import models
from django.dispatch import receiver
from user.models import User


# Create your models here.


# def filefolder_path(instance, filename):
#     return f"{instance.name}/{filename}"  


class Student(models.Model):
    
    GENDER_CHOICES=[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    LEVEL_CHOICES=[
        ('undergraduate','Undergraduate'),
        ('postgraduate','Postgraduate'),
        ('phd','Phd'),
    ]
    STATUS_CHOICES=[
        ('file_submitted','File Submitted'),
        ('conditional_offer','Conditional Offer'),
        ('unconditional_offer','Unconditional Offer'),
        ('offer_rejected','Offer rejected'),
        ('deposit_paid','Deposit Paid'),
        ('interview','Interview'),
        ('cas_requested','CAS Requested'),
        ('cas_issued','CAS Issued'),
        ('vfs_appointment','VFS Appointment'),
        ('visa_granted','Visa Granted'),
        ('visa_rejected','Visa Rejected'),
    ]

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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='created_by')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='updated_by',blank=True,null=True)
    

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

    # try:
    #     old_profile_image = Student.objects.get(pk=instance.pk).profile_image
    # except Student.DoesNotExist:
    #     return False

    # try:        
    #     old_passport = Student.objects.get(pk=instance.pk).passport
    # except Student.DoesNotExist:
    #     return False

    # try:        
    #     old_academic_transcript = Student.objects.get(pk=instance.pk).academic_transcript
    # except Student.DoesNotExist:
    #     return False    
        
    # try:    
    #     old_ielts = Student.objects.get(pk=instance.pk).ielts
    # except Student.DoesNotExist:
    #     return False    
        
    # try:    
    #     old_sop = Student.objects.get(pk=instance.pk).sop
    # except Student.DoesNotExist:
    #     return False    
        
    # try:    
    #     old_cv = Student.objects.get(pk=instance.pk).cv
    # except Student.DoesNotExist:
    #     return False    
        
    # try:    
    #     old_reference = Student.objects.get(pk=instance.pk).reference
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_work_experience = Student.objects.get(pk=instance.pk).work_experience
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_visa = Student.objects.get(pk=instance.pk).visa
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_application_screenshot = Student.objects.get(pk=instance.pk).application_screenshot
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_other = Student.objects.get(pk=instance.pk).other
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_payment_receipt = Student.objects.get(pk=instance.pk).payment_receipt
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_application_form = Student.objects.get(pk=instance.pk).application_form
    # except Student.DoesNotExist:
    #     return False    

    # try:    
    #     old_citizenship = Student.objects.get(pk=instance.pk).citizenship
    # except Student.DoesNotExist:
    #     return False

    # new_profile_image = instance.profile_image
    # new_passport = instance.passport
    # new_academic_transcript = instance.academic_transcript
    # new_ielts = instance.ielts
    # new_sop = instance.sop
    # new_cv = instance.cv
    # new_reference = instance.reference
    # new_work_experience = instance.work_experience
    # new_visa = instance.visa
    # new_application_screenshot = instance.application_screenshot
    # new_other = instance.other
    # new_payment_receipt = instance.payment_receipt
    # new_application_form = instance.application_form
    # new_citizenship = instance.citizenship

    # if not old_profile_image == new_profile_image:
    #     if os.path.exists(old_profile_image.path):
    #         os.remove(old_profile_image.path)

    # if not old_passport == new_passport:
    #     if os.path.isfile(old_passport.path):
    #         os.remove(old_passport.path)

    # if not old_academic_transcript == new_academic_transcript:
    #     if os.path.isfile(old_academic_transcript.path):
    #         os.remove(old_academic_transcript.path)

    # if not old_ielts == new_ielts:
    #     if os.path.isfile(old_ielts.path):
    #         os.remove(old_ielts.path)

    # if not old_sop == new_sop:
    #     if os.path.isfile(old_sop.path):
    #         os.remove(old_sop.path)

    # if not old_cv == new_cv:
    #     if os.path.isfile(old_cv.path):
    #         os.remove(old_cv.path)

    # if not old_reference == new_reference:
    #     if os.path.isfile(old_reference.path):
    #         os.remove(old_reference.path)

    # if not old_work_experience == new_work_experience:
    #     if os.path.isfile(old_work_experience.path):
    #         os.remove(old_work_experience.path)                                                        

    # if not old_visa == new_visa:
    #     if os.path.isfile(old_visa.path):
    #         os.remove(old_visa.path)

    # if not old_application_screenshot == new_application_screenshot:
    #     if os.path.isfile(old_application_screenshot.path):
    #         os.remove(old_application_screenshot.path)

    # if not old_other == new_other:
    #     if os.path.isfile(old_other.path):
    #         os.remove(old_other.path)

    # if not old_payment_receipt == new_payment_receipt:
    #     if os.path.isfile(old_payment_receipt.path):
    #         os.remove(old_payment_receipt.path)

    # if not old_application_form == new_application_form:
    #     if os.path.isfile(old_application_form.path):
    #         os.remove(old_application_form.path)

    # if not old_citizenship == new_citizenship:
    #     if os.path.isfile(old_citizenship.path):
    #         os.remove(old_citizenship.path)                                                