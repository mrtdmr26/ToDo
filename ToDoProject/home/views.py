from django.shortcuts import render, redirect

#from django.http import HttpResponse
from django.utils import timezone
from rest_framework.authtoken.models import Token

#import json
import requests
import datetime

#for signup section
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def home_main(request):
    if (request.user.is_authenticated) and (request.method == "GET"):
    # Do something for authenticated users.

        ##for user in User.objects.all():
        token = Token.objects.get_or_create(user=request.user)

        #For debugging purposes
        print("Token " + str(token[0]))

        url = 'http://127.0.0.1:8000/api/v1/'
        headers = {'Authorization': "Token " +str(token[0])}
        response = requests.get(url, headers=headers)

        #response = requests.get('', auth=(request.user.username, 'Ahtapot135'))
        print(request.user.username)
        data = response.json()
        
        data1 = []
        data2 = []
        for todo in data:
            if todo["completed"]:
                data1.append(todo)
            else:
                data2.append(todo)

        return render(request, 'home/home_main.html', {'forTrue': data1, 'forFalse':data2})
        #return render(request, 'home/home_main.html', context)
        #return JsonResponse(data, safe=False)
    elif (request.user.is_authenticated) and (request.method == "POST"):

        token = Token.objects.get_or_create(user=request.user)
        url = 'http://127.0.0.1:8000/api/v1/'
        headers = {'Authorization': "Token " +str(token[0])}
        

        if "complete_button_ForFalse" in request.POST:
            value = request.POST['complete_button_ForFalse']

            patcher = requests.patch(url+str(value)+"/", {"completed": True}, headers=headers)
            if patcher.status_code == 200:
                print('Entry has been patched successfully! FF')
            return redirect("/")
        if "uncomplete_button_ForTrue" in request.POST:
            value = request.POST['uncomplete_button_ForTrue']

            patcher = requests.patch(url+str(value)+"/", {"completed": False}, headers=headers)
            if patcher.status_code == 200:
                print('Entry has been patched successfully! FT')
            return redirect("/")
        if "delete_button" in request.POST:
            value = request.POST['delete_button']

            deleter = requests.delete(url+str(value)+"/", headers=headers)
            if deleter.status_code == 200:
                print('Entry has been deleted successfully!')
            return redirect("/")
        if "create_button" in request.POST:
            uid = request.user.id
            duedate = request.POST['DueDate_forInput']
            title = request.POST['Title_forInput']
            description = request.POST['TextArea_forInput']

            if duedate == "":
                duedate_edited = timezone.now()
            else:
                duedate_edited = datetime.datetime.strptime(str(duedate), '%d-%m-%Y %H:%M')

            creationdatetime = timezone.now()
            
            datapackage = {
                'uid': uid,
                'title': title,
                'description': description,
                'created': creationdatetime,
                'duedate': duedate_edited,
                'completed': False}
            #json_string = json.dumps(datapackage)

            creater = requests.post(url, data=datapackage, headers=headers)
            #https://www.django-rest-framework.org/api-guide/status-codes/
            if creater.status_code == 201:
                print('Entry has been added to DB!')
            return redirect("/")
    else:
    # Do something for anonymous users.
        return redirect('login')

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'  