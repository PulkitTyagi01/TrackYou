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
import itertools
from django.views import View
import io,csv
from django.contrib import messages


class DataUploadView(View):
    def get(self, request):
        template_name = 'upload.html'
        return render(request, template_name)
        

    def post(self, request):
        if len(request.FILES)==0:
            messages.warning(request,("Please select a file"))
        else:
            file=str(request.FILES['employeefile'])
            filename,extension=file.split('.')
            print(filename,extension)
            if extension=='csv':
                paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
                portfolio1 = csv.DictReader(paramFile)
                list_of_dict = list(portfolio1)
                message="The user and the profiles are successfully created for"
                for i in range(len(list_of_dict)):
                    username = list_of_dict[i]['username']
                    try:
                        new_user=User(first_name=list_of_dict[i]['first_name'],last_name=list_of_dict[i]['last_name'],email=list_of_dict[i]['email'],
                                    username=list_of_dict[i]['username'],password=list_of_dict[i]['password'])
                        new_user.save()
                        new_user.set_password(new_user.password)
                        new_user.save()
                        try:
                            new_profile = Profile(user = User.objects.get(username=list_of_dict[i]['username']), 
                                        team = TeamAndManager.objects.get(name=list_of_dict[i]['team']), 
                                        role=list_of_dict[i]['role'])
                            new_profile.save()
                            # if list_of_dict[i]['role']=="2":
                            #     new_teamandmanager = TeamAndManager(name=list_of_dict[i]['team'],manager=User.objects.get(
                            #         username=list_of_dict[i]['username']).id)
                            #     new_teamandmanager.save()
                            
                            messages.success(request,(f'User and profile successfully created for {username}'))
                        except:
                            messages.error(request,(f'There was a probelm while creating the profile for {username}'))
                    except:
                        messages.error(request,(f'Username with {username} already exists'))
            else:
                print('Wrong file uploaded. Please upload a CSV file')
                messages.error(request,('Wrong file uploaded. Please upload a CSV file'))
        return render(request,'upload.html',{'message':message})

@login_required
def AddTeamMember(request):
    if request.method == "POST":
        employeename = request.POST['EmployeeName']
        team =TeamAndManager.objects.get(manager_id=request.user.id).name
        try:
            # print(User.objects.get(username=employeename))
            # print(TeamAndManager.objects.get(name=team))
            
            team_members_object = Profile.objects.filter(team__name=team)
            print(team_members_object)
            team_members_list = []
            for i in team_members_object:
                team_members_list.append(i.user.username)
            print(team_members_list)

            users_profile_queryset = Profile.objects.all()
            print(users_profile_queryset)
            users_profile_list = []
            for i in users_profile_queryset:
                users_profile_list.append(i.user.username)
            print(users_profile_list)

            if employeename in team_members_list:
                messages.warning(request,(f"User {employeename} is already in the team"))
            elif employeename in users_profile_list:
                messages.warning(request,(f'User {employeename} is already added in another team'))
            else:
                new_teammember = Profile(user = User.objects.get(username=employeename), team = TeamAndManager.objects.get(name=team))
                new_teammember.save()
                messages.success(request,(f'User {employeename} has been succesfully added to the team'))
            return redirect('/home')
        except:
            messages.warning(request,(f'User {employeename} does not exist'))
    return redirect('/home')


@login_required
def DeleteTeamMember(request):
    if request.method=="POST":
        employeename=request.POST['EmployeeName']
        try:
            team=TeamAndManager.objects.get(manager_id=request.user.id).name
            delete_teammember = Profile.objects.filter(user = User.objects.get(username=employeename), team = TeamAndManager.objects.get(name=team))
            print(delete_teammember)
            print(len(delete_teammember))
            if len(delete_teammember)>0:
                delete_teammember.delete()
                messages.error(request,(f"Team member {employeename} successfully deleted. Thank You!"))
            else:
                messages.error(request,(f"No user with name {employeename}. Please check again!! "))
        except:
            messages.error(request,(f"No user with name {employeename}. Please check again!! "))
    return redirect('/home')

@login_required
def AddProject(request):
    if request.method=="POST":
        ProjectName = request.POST['Projectname']
        Description = request.POST['Description']
        team = TeamAndManager.objects.get(manager_id=request.user.id).name
        team_id = TeamAndManager.objects.get(manager_id=request.user.id).id
        teamprojects_queryset= Project.objects.filter(team_id=team_id)
        print(teamprojects_queryset)
        teamprojects_list = []
        for i in teamprojects_queryset:
            teamprojects_list.append(i.name)
        print(teamprojects_list)
        if ProjectName in teamprojects_list:
            messages.warning(request,(f'Project {ProjectName} already exists'))
        else:
            new_project = Project(name=ProjectName, team = TeamAndManager.objects.get(name=team), description = Description)
            new_project.save()
            messages.success(request,(f"Project {ProjectName} has been added successfully"))
        
    return redirect('/Projects')

@login_required
def DeleteProject(request):
    if request.method=="POST":
        ProjectName = request.POST['Projectname']
        # print("sadsadsa",ProjectName)
        try:
            team = TeamAndManager.objects.get(manager_id=request.user.id).name
            delete_project = Project.objects.filter(name=ProjectName, team = TeamAndManager.objects.get(name=team))
            if len(delete_project)>0:
                delete_project.delete()
                messages.error(request,(f" Project {ProjectName} successfully deleted. Thank You!"))
            else:
                messages.error(request,(f" No project with the name {ProjectName}.Please check again !"))
        except:
            messages.error(request,(f" No project with the name {ProjectName}.Please check again !"))

    return redirect('/Projects')

@login_required
def ChangeProjectStatus(request):
    if request.method=="POST":
        ProjectName = request.POST['Projectname']
        status = request.POST['Status']
        try:
            team = TeamAndManager.objects.get(manager_id=request.user.id).name
        except:
            team = Profile.objects.get(user_id=request.user.id).team.name
        try:  
            update_project = Project.objects.get(name = ProjectName, team=TeamAndManager.objects.get(name=team))
            update_project.status = status
            if status=='3':
                update_project.end_date = datetime.datetime.now()
            update_project.save()
            messages.success(request,("Project Status has been changed successfully. Thank You!!"))
        except:
            messages.error(request,("Please select the Project name and status"))
        z=Profile.objects.get(user_id=request.user.id).role
    if z==2:
        return redirect('/Projects')
    else:
        return redirect('/home')

@login_required
def team_projectdata(request):
    print('<<<<<<<<<<<<<<<<<<<<<YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    team=TeamAndManager.objects.get(manager_id=request.user.id).name
    print(team)
    team_id = TeamAndManager.objects.get(name = team)
    team_projects = Project.objects.filter(team=team_id)
    print(team_projects)
    final_dictt={}

    for project in team_projects:
        if (project.status==1 or project.status==2):
            final_dictt[project.name] = ["",[]]
            final_dictt[project.name][0]=project.get_status_display()
            
            #calculation for last week hours
            date = datetime.date.today()
            start_week = date - datetime.timedelta(date.weekday()) - datetime.timedelta(7)
            end_week = start_week + datetime.timedelta(7)

            data_list_hours = {}
            data_list_minutes = {}
            proj=UserProject.objects.filter(project=project.id)
            # print('>>>>>>>>>aaaaaaaaaaaaaaaaaaaaaa<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            # print(proj)

            queryset1=UserProjectProgress.objects.filter(userproject__in=proj)
            # print('>>>>>>>>>aaaaaaaaaaaaaaaaaaaaaa<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            print(queryset1)
            queryset = queryset1.filter(date__range=[start_week,end_week])
            print('>>>>>>>>>aaaaaaaaaaaaaaaaaaaaaa<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            print(queryset)
            hours, minutes = 0,0
            for flag in queryset:
                print('<<<<<<<<<<<<<<<<<<sssssssssssssssssssssssssss>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print(flag.userproject.project)
                hours,minutes = str(flag.daily_hours).split('.')
                data_list_hours[flag.userproject.project.name] = data_list_hours.get(flag.userproject.project.name, 0) + int(hours)
                data_list_minutes[flag.userproject.project.name] = data_list_minutes.get(flag.userproject.project.name, 0) + int(minutes)
            for key, value in data_list_minutes.items():
                print('key',key)
                data_list_hours[key] += value//60
            print('data',data_list_hours)
            if project.name in data_list_hours.keys():
                final_dictt[project.name][1]=data_list_hours[project.name]
            else:
                final_dictt[project.name][1]=0
            print(final_dictt)
    print('<<<<<<<<>>>>>>>>>>><<<<<<<<<<<<<<<<<<>?>?>?>?>?>?>?>?>?>?>?>?>?>?zzzzzzzzzzzzzzzZZZZZZZZZZZZZZ')
    print(final_dictt)
    for key,value in final_dictt.items():
        print(key,"  ",value)
    z2=Profile.objects.get(user_id=request.user.id).role
    FinalDataDictt = {
        'final_dictt' : final_dictt,
        'team_projects': team_projects,
        'team':team,
        'role2':z2,

    }

    return render(request,"home.html", FinalDataDictt)

@login_required
def project_graph_data(request,project1):
    
    final_data_dict = {
        'by_weeks' : {},
        'by_days' : {},
        'by_months' : {}
    }  
    print('user:',project1)

    day_wise_hours={}
    day_wise_minutes={}
    queryset = UserProjectProgress.objects.order_by('-date').filter(userproject__project__name=project1)

    for i in queryset:
        hours, minutes=str(i.daily_hours).split('.')
        day_wise_hours[f'{i.date.date()}'] = day_wise_hours.get(f'{i.date.date()}',0)+int(hours)
        day_wise_minutes[f'{i.date.date()}'] = day_wise_minutes.get(f'{i.date.date()}',0)+int(minutes)
        # print(month_wise_hours)
        # print(month_wise_minutes)

    for key, value in day_wise_minutes.items():
        day_wise_hours[key] += value//60

    final_days_wise = {'days_wise':dict(itertools.islice(day_wise_hours.items(),0,10))}
    # # day wise calculation start (vipul)
    # days_wise = {}
    # queryset = UserProjectProgress.objects.order_by('-date').filter(userproject__project__name=project1)
    # print('111111111111111112222222222222222222223333333333333344444444444455555555555555666666666666',queryset)
    
    
    # for i in queryset:
    #     internal_days_wise = {f'{i.date.date()}' : f'{i.daily_hours}'}
    #     if f'{i.date.date()}' in days_wise.keys():
    #         days_wise[f'{i.date.date()}'] = float(days_wise[f'{i.date.date()}']) + float(internal_days_wise[f'{i.date.date()}'])
    #     else:
    #         days_wise.update(internal_days_wise)
    
    # final_days_wise = {'days_wise':dict(itertools.islice(days_wise.items(),0,10))}
    # # day wise calculation end (vipul)
    
    # Month wise calculation start (vipul)
    date_after_month = datetime.date.today() + relativedelta(months = -11)
    today_date = datetime.date.today()
    month_wise_hours = {}
    month_wise_minutes = {}
    queryset = UserProjectProgress.objects.order_by('-date').filter(date__lte=today_date, date__gte = date_after_month).filter(userproject__project__name=project1).values('date','daily_hours')
    
    for i in queryset:
        hours, minutes=str(i['daily_hours']).split('.')
        month_wise_hours[i["date"].strftime("%B")[:3]] = month_wise_hours.get(i["date"].strftime("%B")[:3],0)+int(hours)
        month_wise_minutes[i["date"].strftime("%B")[:3]] = month_wise_minutes.get(i["date"].strftime("%B")[:3],0)+int(minutes)
        # print(month_wise_hours)
        # print(month_wise_minutes)

    for key, value in month_wise_minutes.items():
        month_wise_hours[key] += value//60

    final_month_wise = {'month_wise':month_wise_hours}
    # Month wise calculation start (vipul)

    # week wise calculation start (Janin, Anjnish))
    for week in range(1,11):
        date = datetime.date.today()
        start_week = date - datetime.timedelta(date.weekday()) - datetime.timedelta(7*week)
        end_week = start_week + datetime.timedelta(7)
        week_key = "{} to {}".format(start_week,end_week)
        data_list_hours = {}
        data_list_minutes = {}
        queryset = UserProjectProgress.objects.filter(date__range=[start_week,end_week])
        final_queryset = queryset.filter(userproject__project__name=project1)
        hours, minutes = 0,0
    
        for flag in final_queryset:
            hours,minutes = str(flag.daily_hours).split('.')
            data_list_hours[flag.userproject.user.username] = data_list_hours.get(flag.userproject.user.username, 0) + int(hours)
            data_list_minutes[flag.userproject.user.username] = data_list_minutes.get(flag.userproject.user.username, 0) + int(minutes)
    
        for key, value in data_list_minutes.items():
            data_list_hours[key] += value//60
        
        if not data_list_hours:
            final_data_dict['by_weeks'][week_key] = 0
        else:
            for key,value in data_list_hours.items():
                final_data_dict['by_weeks'][week_key] = data_list_hours[key]
        # week wise calculation end

    final_data_dict['by_days'] = final_days_wise['days_wise']
    final_data_dict['by_months'] = final_month_wise['month_wise']

    print('-------------------------------------------------------')
    print(final_data_dict)

    return JsonResponse(final_data_dict)

@login_required
def searchproject(request):
    if request.method == 'GET':
        filterData1 = request.GET.get("query")
        try:
            u = Project.objects.filter(name__istartswith = filterData1).filter(team__name = TeamAndManager.objects.get(manager_id=request.user.id).name)       
        except:
            pass
        if len(u) > 0:
            d = {}
            count = 0
            for i in u:
                project_addon = {f'{count}' : f'{i.name}'}
                count = count +1
                d.update(project_addon)
        else:
            d = {
                '0' : 'No Project Found'
            }
        return JsonResponse(d)