import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

print("here!")
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri())
    render(
        request,
        'hello/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
    
    now = datetime.now()
    formatted_now = now.strftime("%a, %d %b, %y at %X")

    # Filter name argument to letters only using regular expressions. URL arguments can contain arbitrary text, so we restrict to safe characters only.

    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)

def register(request):
    return render(request, 'registration/register.html')