import datetime,json
from multiprocessing import managers
from tracemalloc import start
from unicodedata import name
from django.db.models import Q
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import resolve
from adminn.models import *
from dateutil.relativedelta import relativedelta
from django.views import View
import itertools
from django.contrib import messages
from datetime import timezone

@login_required
def emp_data(request, name1):
    employee_data_dict={}
    name1 = User.objects.get(id=request.user.id).first_name
    name2 = User.objects.get(id=request.user.id).last_name
    print(name1,name2)
    name= name1 + ' ' + name2
    if len(name)>1:
        name=name
    else:
        name= User.objects.get(id=request.user.id).username
    print(name)
    projects = UserProject.objects.filter(user_id = request.user.id).filter(project__status=1)
    print(projects)
    employee_data_dict[name]=['','','',[]]
    if len(projects)>0:
        for i in projects:
            employee_data_dict[name][0]=employee_data_dict[name][0]+i.project.name+','
            print(i.project.name)
        employee_data_dict[name][0]=employee_data_dict[name][0][:len(employee_data_dict[name][0])-1]
    else:
        employee_data_dict[name][0]='Currently on POC'
    print(employee_data_dict)

    team_name=Profile.objects.get(user=request.user.id).team.name
    employee_data_dict[name][1]=team_name
    manager_name=TeamAndManager.objects.get(name=team_name).manager
    employee_data_dict[name][2]=manager_name

    #Calculation of last week hours
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday()) - datetime.timedelta(7)
    print(start_week)
    end_week = start_week + datetime.timedelta(7)
    print(end_week)

    data_list_hours = {}
    data_list_minutes = {}


    queryset1 = UserProjectProgress.objects.filter(userproject__in=projects)
    print(queryset1)
    queryset = queryset1.filter(date__range=[start_week,end_week])
    print(queryset)
    hours, minutes = 0,0

    for flag in queryset:
        hours,minutes = str(flag.daily_hours).split('.')
        data_list_hours[flag.userproject.user.username] = data_list_hours.get(flag.userproject.user.username, 0) + int(hours)
        data_list_minutes[flag.userproject.user.username] = data_list_minutes.get(flag.userproject.user.username, 0) + int(minutes)
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    print(data_list_hours)
    print(data_list_minutes)
    for key, value in data_list_minutes.items():
        data_list_hours[key] += value//60

    if request.user.username in data_list_hours.keys():
        employee_data_dict[name][3]=data_list_hours[request.user.username]
    else:
        employee_data_dict[name][3]=0
    print(employee_data_dict)

    z1=Profile.objects.get(user_id=request.user.id).role
    
    max_date = str(datetime.date.today())+'T23:59'
    print(max_date)
    min_date = str(date - datetime.timedelta(date.weekday()) - datetime.timedelta(1))+'T00:00'
    print(min_date)
    default_date = str(date)+'T10:00'
    print(default_date)

    team=Profile.objects.get(user_id=request.user.id).team
    projects=Project.objects.filter(team=team)
    projects_list=[]
    for i in projects:
        if i.status == 1:
            projects_list.append(i.name)
    #print(projects_list)
    #a = 5 

    FinalDataDicttt = {
        'final_dicttt' : employee_data_dict,
        'ProjectList' : projects_list,
        'min_date':min_date,
        'max_date':max_date,
        'default_date':default_date,
        'role3':z1,
        #'var':a,
    }

    return render(request,"home.html",FinalDataDicttt)

@login_required
def DailyUpdate(request):
    if request.method == "POST":
        print('xxxxxxxxxxx,,,,,,,,,,>>>>>>>>>>>>>>>>yyyyyyyyyy')
        name1 = request.user
        print(request.user)
        project1= request.POST['project1']
        hours =request.POST['Hours']
        description=request.POST['Daily Update']
        date1=  request.POST['date']
        date,time=date1.split('T')
        
        # date_project = date+' '+project1
        # print(date_project)

        user_dailyupdates_queryset= UserProjectProgress.objects.order_by('-date').filter(userproject=UserProject.objects.get(user = User.objects.get(username=name1), project = Project.objects.get(name=project1)))
        count=0
        for i in user_dailyupdates_queryset:
            if date == f'{i.date.date()}':
                if project1 == i.userproject.project.name:
                    count+=1
                break

        if count>0:
            messages.error(request,(f'You have already given the update for {date}'))
        else:
            try:
                new_update = UserProjectProgress(userproject=UserProject.objects.get(user = User.objects.get(username=name1), project = Project.objects.get(name=project1)), daily_hours=hours, daily_report = description, date=date1)
                print(new_update)
                new_update.save()
                messages.success(request,("Your update has been successfully Recorded. Thank You"))
            except:
                new_userproject = UserProject(user = User.objects.get(username=name1), project = Project.objects.get(name=project1))
                new_userproject.save()
                
                new_update = UserProjectProgress(userproject=UserProject.objects.get(user = User.objects.get(username=name1), project = Project.objects.get(name=project1)), daily_hours=hours, daily_report = description, date=date1)
                new_update.save()
                messages.success(request,("Your update has been successfully Recorded. Thank You"))

    return redirect('/home')
        # latestfive_dateproject_string_list=[]
        # if len(latestfive_updates_queryset)>5:
        #     for i in latestfive_updates_queryset[0:5]:
        #         latestfive_dateproject_string_list.append(str(i.date.date())+' '+ i.userproject.project.name)
        # else:
        #     for i in latestfive_updates_queryset:
        #         latestfive_dateproject_string_list.append(str(i.date.date())+' '+ i.userproject.project.name)
        # print(latestfive_dateproject_string_list)
        # for i in latestfive_dateproject_string_list:
        #     if date_project == i:
        #         messages.error(request,(f'You have already given the update for {date}'))
        #         break
        #         #new_update = UserProjectProgress.objects.get(userproject=UserProject.objects.get(user = User.objects.get(username=name1), project = Project.objects.get(name=project1)), date=date)



def edit_profile(request):
    name1 = User.objects.get(id=request.user.id)
    username = name1.username
    if request.method =="POST":
        update_firstname = request.POST['firstname']
        update_lastname = request.POST['lastname']
        update_email = request.POST['email']
        name1.first_name = update_firstname
        name1.last_name = update_lastname
        name1.email = update_email
        name1.save()
        messages.success(request,("Your Profile Successfully Updated. Thank You"))
        context={
        'name1':name1
        }
        return redirect(f'emp/{username}')
    else:
        context={
        'name1':name1
        }
        return render(request,'home.html',context)
        
            
            
class changepassword(View):
    def get(self, request):
        template_name = 'changepassword.html'
        return render(request, template_name)

    def post(self, request):
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        try:   
            user=User.objects.get(username=username)
            user.set_password(newpassword)
            user.save()
            message="Password successfully changed"
            #return render(request,'changepassword.html',{'message':message})
        except:
            message='No user with that username'
        return render(request,'changepassword.html',{'message':message})    



