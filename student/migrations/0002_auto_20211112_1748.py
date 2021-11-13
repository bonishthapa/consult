# Generated by Django 3.2.8 on 2021-11-12 17:48

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='student',
            name='application_form',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='student',
            name='citizenship',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='payment_receipt',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='student',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('File Submitted', 'File Submitted'), ('Conditional Offer', 'Conditional Offer'), ('Unconditional Offer', 'Unconditional Offer'), ('Offer rejected', 'Offer rejected'), ('Deposit Paid', 'Deposit Paid'), ('Interview', 'Interview'), ('CAS Requested', 'CAS Requested'), ('CAS Issued', 'CAS Issued'), ('VFS Appointment', 'VFS Appointment'), ('Visa Granted', 'Visa Granted'), ('Visa Rejected', 'Visa Rejected')], max_length=50),
        ),
    ]