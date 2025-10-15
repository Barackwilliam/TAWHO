from django.db import models
from django.core.validators import EmailValidator

class OrganizationInfo(models.Model):
    name = models.CharField(max_length=200, default="Tanzania Women Hope Organization (TAWHO)")
    registration_number = models.CharField(max_length=50, default="OONGO/R/7662")
    address = models.TextField(default="P.O. Box 20950, Ilala-Dar es Salaam")
    headquarters = models.TextField(default="Majohe Shule street, Ilala District Dar es salaam region")
    operating_area = models.CharField(max_length=100, default="Tanzania Mainland")
    
    class Meta:
        verbose_name_plural = "Organization Information"

class Member(models.Model):
    MEMBER_TYPES = [
        ('founder', 'Founder Member'),
        ('ordinary', 'Ordinary Member'),
        ('coopted', 'Co-opted Member'),
        ('honorary', 'Honorary Member'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.get_member_type_display()}"

class Program(models.Model):
    PROGRAM_CATEGORIES = [
        ('education', 'Education & Skills Training'),
        ('health', 'Health & Reproductive Care'),
        ('economic', 'Economic Empowerment'),
        ('advocacy', 'Advocacy & Awareness'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=PROGRAM_CATEGORIES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='programs/', null=True, blank=True)
    
    def __str__(self):
        return self.title

class Donation(models.Model):
    DONATION_TYPES = [
        ('money', 'Financial Donation'),
        ('equipment', 'Equipment/Materials'),
        ('time', 'Volunteer Time'),
        ('expertise', 'Professional Expertise'),
    ]
    
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    donation_type = models.CharField(max_length=20, choices=DONATION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    donation_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.donor_name} - {self.get_donation_type_display()}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Document(models.Model):
    DOCUMENT_TYPES = [
        ('constitution', 'Constitution'),
        ('certificate', 'Registration Certificate'),
        ('report', 'Annual Report'),
        ('financial', 'Financial Statement'),
    ]
    
    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title