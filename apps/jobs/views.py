from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, Application


# =========================
# Find Jobs
# =========================
def find_jobs(request):

    jobs = Job.objects.all()

    return render(request, 'jobs/find_jobs.html', {
        'jobs': jobs
    })


# =========================
# Post Job
# =========================
def post_job(request):

    if request.method == "POST":

        Job.objects.create(

            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            budget=request.POST.get('budget'),
            company=request.POST.get('company'),
        )

        return redirect('/jobs/')

    return render(request, 'jobs/post_job.html')


# =========================
# Job Details
# =========================
def job_details(request, id):

    job = get_object_or_404(Job, id=id)

    applications = Application.objects.filter(job=job)

    return render(request, 'jobs/job_details.html', {
        'job': job,
        'applications': applications
    })


# =========================
# Apply Job
# =========================
def apply_job(request, id):

    job = get_object_or_404(Job, id=id)

    if request.method == "POST":

        Application.objects.create(

            job=job,
            user=request.user,

            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )

    return redirect('/jobs/' + str(id))