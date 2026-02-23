from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse

@login_required
def portal_view(request: HttpRequest, *args, **kwargs):
    data = {
        "user": str(request.user),
        "is_authenticated": request.user.is_authenticated,
        "method": request.method,
        "account_type":request.user.account_type,
    }
    # return JsonResponse(data)
    # print(request)
    # return HttpResponse("Welcome to portal!")
    if request.user.account_type == "STUDENT":
        print(request.user.account_type)
        return redirect('student_portal')
    elif request.user.account_type == "SCHOOL":
        print(request.user.account_type)
    elif request.user.account_type == "ADMIN":
        print(request.user.account_type)
    return HttpResponse(f"Here: {request}")