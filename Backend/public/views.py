from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import os
from .models import *
# Create your views here.
def UserPanel(request):
    return render(request, 'userpanel.html')
@csrf_exempt
def FileUpload(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Sorry! Only post method will allow", status=400)
    else:        
        Username  = request.POST.get('username')
        Course = request.POST.get('course')
        File = request.FILES.get('file')
        
        UserFile.objects.create(
            username = Username,
            course = Course,
            files = File
        )
        return JsonResponse({
            "status" : "Done",
            'Message' : "Uploaded"
        },status=201)


def UserData(request):
    if request.method != "GET":
        return JsonResponse({
            "status": "Bad Request",
            "message": "Wrong Method! Please Try Again"
        }, status=400)

    UserData = []

    for fetch in UserFile.objects.all():
        records = model_to_dict(fetch)

        records["student"] = fetch.username # Making a new key for store the user / student name
        records["name"] = os.path.basename(fetch.files.name) #This is for extract the file name.
        records["size"] = fetch.files.size # fetch the file size
        records["course"] = fetch.get_course_display() #display in frontend the course names
        records["files"] = request.build_absolute_uri(fetch.files.url) # Get the file URL

        UserData.append(records)

    return JsonResponse({
        "status": "Data viewing",
        "number_of_data": len(UserData),
        "data": UserData
    }, status=200)