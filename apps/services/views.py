from django.shortcuts import render, redirect
from .models import Service


def services_page(request):

    if request.method == "POST":

        Service.objects.create(

            service_type=request.POST.get('service_type'),

            idea_name=request.POST.get('idea_name'),

            expected_price=request.POST.get('expected_price'),

            full_name=request.POST.get('full_name'),

            phone=request.POST.get('phone'),

            email=request.POST.get('email'),
        )

        return redirect('/services/')

    services = Service.objects.all()

    return render(request, 'services/services.html', {
        'services': services
    })