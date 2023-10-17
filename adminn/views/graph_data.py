import datetime,json
from dateutil.relativedelta import relativedelta

from django.http import JsonResponse
# from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.decorators import login_required

from ..models import *
import itertools

           
def graph_data(request,user):
    
    final_data_dict = {
        'by_weeks' : {},
        'by_days' : {},
        'daily_report_daywise' : {},
        'by_months' : {}
    }  

    # day wise calculation start (vipul)
    day_wise_hours = {}
    day_wise_minutes = {}
    daily_report_daywise = {}
    queryset = UserProjectProgress.objects.order_by('-date').filter(userproject__user__username=user)
    if len(queryset) > 10:
        for i in queryset[0:10]:
            hours,minutes=str(i.daily_hours).split('.')
            day_wise_hours[f'{i.date.date()}'] = day_wise_hours.get(f'{i.date.date()}',0)+int(hours)
            day_wise_minutes[f'{i.date.date()}'] = day_wise_minutes.get(f'{i.date.date()}',0)+int(minutes)
            daily_report_daywise[f'{i.date.date()}'] = daily_report_daywise.get(f'{i.date.date()}','') + i.daily_report + ', '
    else:
        for i in queryset:
            hours,minutes=str(i.daily_hours).split('.')
            day_wise_hours[f'{i.date.date()}'] = day_wise_hours.get(f'{i.date.date()}',0)+int(hours)
            day_wise_minutes[f'{i.date.date()}'] = day_wise_minutes.get(f'{i.date.date()}',0)+int(minutes)
            daily_report_daywise[f'{i.date.date()}'] = daily_report_daywise.get(f'{i.date.date()}','') + i.daily_report + ', '
    
    for key,value in day_wise_minutes.items():
        day_wise_hours[key] += value//60

    final_days_wise = {'days_wise':day_wise_hours}
    final_daily_report_daywise = {'daily_report_daywise' : daily_report_daywise}
    # day wise calculation end (vipul)
    
    # Month wise calculation start (vipul)
    date_after_month = datetime.date.today() + relativedelta(months = -11)
    today_date = datetime.date.today()
    month_wise_hours = {}
    month_wise_minutes = {}
    queryset = UserProjectProgress.objects.order_by('-date').filter(date__lte=today_date, date__gte = date_after_month).filter(userproject__user__username=user).values('date','daily_hours')
    print('months',queryset)
    for i in queryset:
        hours, minutes=str(i['daily_hours']).split('.')

        # print('<<<<<<<<<<<<<<<<99999999999999999999999>>>>>>>>>>>>>>>>>>>')
        # print(i['daily_hours'])
        # print(hours,minutes)
        # print(i["date"].strftime("%B")[:3])
        # print(month_wise_hours.get(i["date"].strftime("%B")[:3],0))
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
        end_week = start_week + datetime.timedelta(6)
        week_key = "{} to {}".format(start_week,end_week)
        data_list_hours = {}
        data_list_minutes = {}
        queryset = UserProjectProgress.objects.filter(date__range=[start_week,end_week])
        final_queryset = queryset.filter(userproject__user__username=user)
        hours, minutes = 0,0
    
        for flag in final_queryset:
            hours,minutes = str(flag.daily_hours).split('.')
            data_list_hours[flag.userproject.user.username] = data_list_hours.get(flag.userproject.user.username, 0) + int(hours)
            data_list_minutes[flag.userproject.user.username] = data_list_minutes.get(flag.userproject.user.username, 0) + int(minutes)
    
        for key, value in data_list_minutes.items():
            data_list_hours[key] += value//60
            print(value)
        if not data_list_hours:
            final_data_dict['by_weeks'][week_key] = 0
        else:
            for key,value in data_list_hours.items():
                final_data_dict['by_weeks'][week_key] = data_list_hours[key]
                print(value)

        # week wise calculation end

    final_data_dict['by_days'] = final_days_wise['days_wise']
    final_data_dict['daily_report_daywise'] = final_daily_report_daywise['daily_report_daywise']
    final_data_dict['by_months'] = final_month_wise['month_wise']
    print('final_data_dict',final_data_dict)
    # print('-------------------------------------------------------')
    # print(final_data_dict)
    # print(value)

    return JsonResponse(final_data_dict)

def team_graph_data(request,team1):
    
    final_data_dict = {
        'by_weeks' : {},
        'by_days' : {},
        'by_months' : {}
    }  

    # day wise calculation start (vipul)
    day_wise_hours={}
    day_wise_minutes={}
    queryset = UserProjectProgress.objects.order_by('-date').filter(userproject__project__team__name=team1)

    for i in queryset:
        hours, minutes=str(i.daily_hours).split('.')
        day_wise_hours[f'{i.date.date()}'] = day_wise_hours.get(f'{i.date.date()}',0)+int(hours)
        day_wise_minutes[f'{i.date.date()}'] = day_wise_minutes.get(f'{i.date.date()}',0)+int(minutes)
        # print(month_wise_hours)
        # print(month_wise_minutes)

    for key, value in day_wise_minutes.items():
        day_wise_hours[key] += value//60

    final_days_wise = {'days_wise':dict(itertools.islice(day_wise_hours.items(),0,10))}

    # days_wise = {}

    # queryset = UserProjectProgress.objects.order_by('-date').filter(userproject__project__team__name=team1)
    # print(queryset)
    # print('????????????????/////////////<<<<<<<>>>>>>>',len(queryset))
    # for i in queryset:
    #     internal_days_wise = {f'{i.date.date()}' : f'{i.daily_hours}'}
    #     if f'{i.date.date()}' in days_wise.keys():
    #         days_wise[f'{i.date.date()}'] = float(days_wise[f'{i.date.date()}']) + float(internal_days_wise[f'{i.date.date()}'])
    #     else:
    #         days_wise.update(internal_days_wise)

    # final_days_wise = {'days_wise':dict(itertools.islice(days_wise.items(),0,10))}
    # day wise calculation end (vipul)
    
    # Month wise calculation start (vipul)
    date_after_month = datetime.date.today() + relativedelta(months = -11)
    today_date = datetime.date.today()
    month_wise_hours = {}
    month_wise_minutes = {}
    queryset = UserProjectProgress.objects.order_by('-date').filter(date__lte=today_date, date__gte = date_after_month).filter(userproject__project__team__name=team1).values('date','daily_hours')
    
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
        end_week = start_week + datetime.timedelta(6)
        week_key = "{} to {}".format(start_week,end_week)
        data_list_hours = {}
        data_list_minutes = {}
        queryset = UserProjectProgress.objects.filter(date__range=[start_week,end_week])
        final_queryset = queryset.filter(userproject__project__team__name=team1)
        hours, minutes = 0,0
    
        for flag in final_queryset:
            hours,minutes = str(flag.daily_hours).split('.')
            data_list_hours[flag.userproject.project.team.name] = data_list_hours.get(flag.userproject.project.team.name, 0) + int(hours)
            data_list_minutes[flag.userproject.project.team.name] = data_list_minutes.get(flag.userproject.project.team.name, 0) + int(minutes)
    
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