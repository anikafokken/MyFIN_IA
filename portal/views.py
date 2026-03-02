from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from programs.services.matching import get_ranked_programs


# Create your views here.

@login_required
def student_portal(request):
    programs = get_ranked_programs(request.user.student)
    return render(request, "templates/portal/results.html", {"programs": programs})

def school_portal(request):
    return HttpResponse("Welcome to the Institution Portal!")

def admin_portal(request):
    return HttpResponse("Welcome to the Admin Portal!")