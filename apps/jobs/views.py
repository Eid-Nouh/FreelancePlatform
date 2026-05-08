from django.shortcuts import render, redirect
from .models import Job


# ==============================
# Find Jobs Page
# ==============================

def find_jobs(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/find_jobs.html', {
        'jobs': jobs
    })


# ==============================
# Post Job Page
# ==============================

def post_job(request):

    if request.method == "POST":

        title = request.POST.get('title')
        description = request.POST.get('description')
        budget = request.POST.get('budget')
        company = request.POST.get('company')
        Job.objects.create(
            title=title,
            description=description,
            budget=budget,
            company=company
        )
        return redirect('/jobs/')
    return render(request, 'jobs/post_job.html')


# ==============================
# Job Details Page
# ==============================

def job_details(request, id):

    job = Job.objects.get(id=id)

    return render(request, 'jobs/job_details.html', {
        'job': job
    })