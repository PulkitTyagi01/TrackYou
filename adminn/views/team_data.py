import datetime
from unicodedata import name

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from ..models import *

def team_data(request, team):
    # print('helllllllllloooooooooooooooooo theeeeeeeeeeeeeerrrrrrrrrrrrrreeeeeeeeee', team)
    team_id = TeamAndManager.objects.get(name = team)
    team_members = Profile.objects.filter(team=team_id)
    final_dict = {}

    for team_member in team_members:
        #calculation for username and related projects
        particular_projects = UserProject.objects.filter(user=team_member.user)
        final_dict[team_member.user.username] = ["",[],""]
        for project in particular_projects:
            final_dict[team_member.user.username][0] = final_dict[team_member.user.username][0] + project.project.name + ", "
        final_dict[team_member.user.username][0] = final_dict[team_member.user.username][0][:len(final_dict[team_member.user.username][0])-2]
        role = team_member.get_role_display()
        final_dict[team_member.user.username][2] = role
        #calculation for last week hours
        date = datetime.date.today()
        print(date)
        start_week = date - datetime.timedelta(date.weekday()) - datetime.timedelta(7)
        end_week = start_week + datetime.timedelta(7)

        data_list_hours = {}
        data_list_minutes = {}


        queryset1 = UserProjectProgress.objects.filter(userproject__in=particular_projects)
        queryset = queryset1.filter(date__range=[start_week,end_week])

        hours, minutes = 0,0

        for flag in queryset:
            hours,minutes = str(flag.daily_hours).split('.')
            data_list_hours[flag.userproject.user.username] = data_list_hours.get(flag.userproject.user.username, 0) + int(hours)
            data_list_minutes[flag.userproject.user.username] = data_list_minutes.get(flag.userproject.user.username, 0) + int(minutes)

        for key, value in data_list_minutes.items():
            data_list_hours[key] += value//60

        if team_member.user.username in data_list_hours.keys() and team_member.user.username in final_dict.keys():
            final_dict[team_member.user.username][1].append(data_list_hours[team_member.user.username])
    
    for team_member in team_members:
        if team_member.user.username not in final_dict.keys():
            final_dict[team_member.user.username] = ["",[]]

    TeamList = TeamAndManager.objects.all()

    z1=Profile.objects.get(user_id=request.user.id).role
    
    print(final_dict)
    FinalDataDict = {
        'final_dict' : final_dict,
        'TeamList' : TeamList,
        'role1':z1,
    }
    


    return render(request,"home.html", FinalDataDict)

