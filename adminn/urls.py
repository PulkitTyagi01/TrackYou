from . import views
from django.urls import path
#from employee.views import *
# from TrackYou import adminn

app_name = 'adminn'

urlpatterns = [
    path('', views.login_view, name=""),
    path('home', views.home, name='home'),
    path('AddTeam', views.AddTeam, name='AddTeam'),
    path('newapi', views.newapi, name='newapi'),
    path('logout', views.logout_view,  name="logout"),
   
    path('searchteam', views.searchteam, name='searchteam'),
    path('searchteam_name', views.searchteam_name, name='searchteam_name'),
    path('Changemanager', views.ChangeManager, name='ChangeManager'),
    path('DeleteTeam', views.DeleteTeam, name='DeleteTeam'),
    path('forgot_password',views.forgot_password,name = 'forgot_password'),
    path('change_password/<str:token>', views.change_password,name="change_password"),
    path('team_graph_data/<str:team1>', views.team_graph_data,  name="team_graph_data"),
    path('graph_data/<str:user>', views.graph_data,  name="graph_data"),
    path('projects_lists',views.projects_list, name='projects_lists'),
    path('<str:team>', views.team_data, name='team_data'),
    # path('emp',views.emp, name="emp"),

]