from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import FreelancerProfile, ClientProfile, Skill, Experience, Education, Portfolio
from apps.accounts.models import CustomUser


def profile_view(request, username=None):
    if username:
        user = get_object_or_404(CustomUser, username=username)
    else:
        if request.user.is_authenticated:
            user = request.user
        else:
            return redirect('login')
    
    context = {'profile_user': user}
    
    if user.user_type == 'freelancer':
        profile, created = FreelancerProfile.objects.get_or_create(user=user)
        skills = profile.skills.all()
        experiences = profile.experiences.all().order_by('-start_date')
        educations = profile.educations.all().order_by('-year')
        portfolios = profile.portfolio_items.all()
        
        context.update({
            'profile': profile,
            'skills': skills,
            'experiences': experiences,
            'educations': educations,
            'portfolios': portfolios,
        })
        return render(request, 'Profile/freelancer_profile.html', context)
    
    else:
        profile, created = ClientProfile.objects.get_or_create(user=user)
        context['profile'] = profile
        return render(request, 'Profile/client_profile.html', context)


@login_required
def edit_profile_view(request):
    user = request.user
    
    if user.user_type == 'freelancer':
        profile, created = FreelancerProfile.objects.get_or_create(user=user)
        experiences = profile.experiences.all()
        educations = profile.educations.all()
        portfolios = profile.portfolio_items.all()
        
        if request.method == 'POST':
            # ========== BASIC INFO ==========
            profile.headline = request.POST.get('headline')
            profile.bio = request.POST.get('bio')
            profile.title = request.POST.get('title')
            
            # Handle hourly_rate
            hourly_rate = request.POST.get('hourly_rate')
            if hourly_rate == '' or hourly_rate is None:
                profile.hourly_rate = None
            else:
                try:
                    profile.hourly_rate = float(hourly_rate)
                except ValueError:
                    profile.hourly_rate = None
            
            profile.location = request.POST.get('location')
            
            # Social Links
            profile.github = request.POST.get('github') or None
            profile.linkedin = request.POST.get('linkedin') or None
            profile.twitter = request.POST.get('twitter') or None
            profile.personal_website = request.POST.get('personal_website') or None
            
            # Profile Image
            if request.FILES.get('profile_image'):
                profile.profile_image = request.FILES['profile_image']
            
            # Cover Image
            if request.FILES.get('cover_image'):
                profile.cover_image = request.FILES['cover_image']
            
            profile.save()
            
            # ========== SKILLS ==========
            skills_string = request.POST.get('skills', '')
            skills_list = [s.strip() for s in skills_string.split(',') if s.strip()]
            profile.skills.all().delete()
            for skill_name in skills_list:
                Skill.objects.create(freelancer=profile, name=skill_name)
            
            # ========== WORK EXPERIENCE ==========
            # Process existing experiences (with ID)
            for exp in experiences:
                if request.POST.get(f'exp_title_{exp.id}'):
                    exp.title = request.POST.get(f'exp_title_{exp.id}')
                    exp.company = request.POST.get(f'exp_company_{exp.id}')
                    
                    # Handle start_date (convert empty string to None)
                    start_date = request.POST.get(f'exp_start_{exp.id}')
                    exp.start_date = start_date if start_date else None
                    
                    # Handle end_date (convert empty string to None)
                    end_date = request.POST.get(f'exp_end_{exp.id}')
                    exp.end_date = end_date if end_date else None
                    
                    exp.current = request.POST.get(f'exp_current_{exp.id}') == 'on'
                    exp.description = request.POST.get(f'exp_desc_{exp.id}')
                    exp.save()
                else:
                    exp.delete()
            
            # Process new experiences
            new_exp_keys = [k for k in request.POST.keys() if k.startswith('new_exp_title_')]
            for key in new_exp_keys:
                index = key.split('_')[-1]
                title = request.POST.get(f'new_exp_title_{index}')
                if title:
                    start_date = request.POST.get(f'new_exp_start_{index}')
                    end_date = request.POST.get(f'new_exp_end_{index}')
                    
                    Experience.objects.create(
                        freelancer=profile,
                        title=title,
                        company=request.POST.get(f'new_exp_company_{index}', ''),
                        start_date=start_date if start_date else None,
                        end_date=end_date if end_date else None,
                        current=request.POST.get(f'new_exp_current_{index}') == 'on',
                        description=request.POST.get(f'new_exp_desc_{index}', '')
                    )
            
            # ========== EDUCATION ==========
            # Process existing education
            for edu in educations:
                if request.POST.get(f'edu_degree_{edu.id}'):
                    edu.degree = request.POST.get(f'edu_degree_{edu.id}')
                    edu.institution = request.POST.get(f'edu_institution_{edu.id}')
                    
                    # Handle year (convert empty string to None)
                    year = request.POST.get(f'edu_year_{edu.id}')
                    edu.year = int(year) if year and year.isdigit() else None
                    
                    edu.description = request.POST.get(f'edu_desc_{edu.id}')
                    edu.save()
                else:
                    edu.delete()
            
            # Process new education
            new_edu_keys = [k for k in request.POST.keys() if k.startswith('new_edu_degree_')]
            for key in new_edu_keys:
                index = key.split('_')[-1]
                degree = request.POST.get(f'new_edu_degree_{index}')
                if degree:
                    year = request.POST.get(f'new_edu_year_{index}')
                    
                    Education.objects.create(
                        freelancer=profile,
                        degree=degree,
                        institution=request.POST.get(f'new_edu_institution_{index}', ''),
                        year=int(year) if year and year.isdigit() else None,
                        description=request.POST.get(f'new_edu_desc_{index}', '')
                    )
            
            # ========== PORTFOLIO ==========
            # Process existing portfolio
            for item in portfolios:
                if request.POST.get(f'portfolio_title_{item.id}'):
                    item.title = request.POST.get(f'portfolio_title_{item.id}')
                    item.description = request.POST.get(f'portfolio_desc_{item.id}')
                    item.project_url = request.POST.get(f'portfolio_url_{item.id}') or None
                    
                    # Check if remove image is checked
                    if request.POST.get(f'portfolio_remove_image_{item.id}') == 'on':
                        if item.image:
                            item.image.delete()
                        item.image = None
                    
                    # Handle new image upload for existing item
                    if request.FILES.get(f'portfolio_image_{item.id}'):
                        if item.image:
                            item.image.delete()
                        item.image = request.FILES[f'portfolio_image_{item.id}']
                    
                    item.save()
                else:
                    if item.image:
                        item.image.delete()
                    item.delete()
            
            # Process new portfolio items
            new_portfolio_keys = [k for k in request.POST.keys() if k.startswith('new_portfolio_title_')]
            for key in new_portfolio_keys:
                index = key.split('_')[-1]
                title = request.POST.get(f'new_portfolio_title_{index}')
                if title:
                    portfolio = Portfolio.objects.create(
                        freelancer=profile,
                        title=title,
                        description=request.POST.get(f'new_portfolio_desc_{index}', ''),
                        project_url=request.POST.get(f'new_portfolio_url_{index}') or None
                    )
                    # Handle image upload
                    if request.FILES.get(f'new_portfolio_image_{index}'):
                        portfolio.image = request.FILES[f'new_portfolio_image_{index}']
                        portfolio.save()
            
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        
        # GET request - prepare form data
        current_skills = ', '.join([skill.name for skill in profile.skills.all()])
        
        context = {
            'profile': profile,
            'skills_list': current_skills,
            'experiences': experiences,
            'educations': educations,
            'portfolios': portfolios,
        }
        return render(request, 'Profile/edit_freelancer.html', context)
    
    else:
        # ========== CLIENT PROFILE (Individual Person) ==========
        profile, created = ClientProfile.objects.get_or_create(user=user)
        
        if request.method == 'POST':
            # Basic Info
            profile.headline = request.POST.get('headline')
            profile.bio = request.POST.get('bio')
            profile.location = request.POST.get('location')
            profile.phone = request.POST.get('phone')
            
            # Social Links
            profile.github = request.POST.get('github') or None
            profile.linkedin = request.POST.get('linkedin') or None
            profile.twitter = request.POST.get('twitter') or None
            
            # Profile Image
            if request.FILES.get('profile_image'):
                profile.profile_image = request.FILES['profile_image']
            
            # Cover Image
            if request.FILES.get('cover_image'):
                profile.cover_image = request.FILES['cover_image']
            
            profile.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
        
        context = {
            'profile': profile,
        }
        return render(request, 'Profile/edit_client.html', context)