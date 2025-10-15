from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
from .forms import *

def homepage(request):
    programs = Program.objects.filter(is_active=True)[:3]
    events = Event.objects.filter(is_active=True)[:3]
    org_info = OrganizationInfo.objects.first()
    
    context = {
        'programs': programs,
        'events': events,
        'org_info': org_info,
    }
    return render(request, 'homepage.html', context)

def about_us(request):
    org_info = OrganizationInfo.objects.first()
    members = Member.objects.filter(is_active=True)
    
    context = {
        'org_info': org_info,
        'members': members,
    }
    return render(request, 'about.html', context)

def programs(request):
    programs = Program.objects.filter(is_active=True)
    categories = Program.PROGRAM_CATEGORIES
    
    context = {
        'programs': programs,
        'categories': categories,
    }
    return render(request, 'programs.html', context)

def membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership_success')
    else:
        form = MembershipForm()
    
    context = {'form': form}
    return render(request, 'membership.html', context)

def donation(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            # Send confirmation email
            send_mail(
                'Thank you for your donation - TAWHO',
                f'Dear {donation.donor_name}, thank you for your generous donation.',
                'noreply@tawho.org',
                [donation.donor_email],
                fail_silently=True,
            )
            return redirect('donation_success')
    else:
        form = DonationForm()
    
    context = {'form': form}
    return render(request, 'donation.html', context)

def documents(request):
    documents = Document.objects.filter(is_public=True)
    
    context = {
        'documents': documents,
    }
    return render(request, 'documents.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'contact.html', context)

# API Views
def program_list_api(request):
    programs = Program.objects.filter(is_active=True)
    data = []
    for program in programs:
        data.append({
            'id': program.id,
            'title': program.title,
            'description': program.description,
            'category': program.get_category_display(),
        })
    return JsonResponse(data, safe=False)

def member_stats_api(request):
    total_members = Member.objects.filter(is_active=True).count()
    by_type = {}
    for member_type, display_name in Member.MEMBER_TYPES:
        count = Member.objects.filter(member_type=member_type, is_active=True).count()
        by_type[display_name] = count
    
    return JsonResponse({
        'total_members': total_members,
        'members_by_type': by_type
    })

def program_list_api(request):
    programs = [
        {
            'id': 1,
            'title': 'Reproductive Health Education',
            'description': 'A project to provide women with knowledge on reproductive health, family planning, and proper child upbringing.',
            'category': 'health',
            'start_date': '2024-01-15',
            'end_date': '2024-12-15',
            'is_active': True
        },
        {
            'id': 2,
            'title': 'Entrepreneurship Training',
            'description': 'Providing women with skills to start and run small businesses.',
            'category': 'economic',
            'start_date': '2024-02-01',
            'end_date': None,
            'is_active': True
        },
        {
            'id': 3,
            'title': 'HIV/AIDS Awareness',
            'description': 'A project to educate the community about HIV/AIDS, sexually transmitted diseases, and prevention methods.',
            'category': 'health',
            'start_date': '2024-03-01',
            'end_date': '2024-08-01',
            'is_active': True
        }
    ]
    return JsonResponse(programs, safe=False)