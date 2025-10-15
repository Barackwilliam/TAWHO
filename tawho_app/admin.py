from django.contrib import admin
from .models import *

@admin.register(OrganizationInfo)
class OrganizationInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'registration_number', 'operating_area']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'member_type', 'join_date', 'is_active']
    list_filter = ['member_type', 'is_active']
    search_fields = ['name', 'email']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'start_date', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'description']

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donor_name', 'donation_type', 'amount', 'donation_date', 'is_approved']
    list_filter = ['donation_type', 'is_approved']
    search_fields = ['donor_name', 'donor_email']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read']
    search_fields = ['name', 'email', 'subject']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'upload_date', 'is_public']
    list_filter = ['document_type', 'is_public']
    search_fields = ['title']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_date', 'location', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'location']