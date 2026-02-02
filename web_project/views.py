from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, MyFIN client! Welcome to My Future in Nursing!")

