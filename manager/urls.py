from . import views
from django.urls import path

# from TrackYou import adminn

app_name = 'manager'

urlpatterns = [
    path('uploaddata',views.DataUploadView.as_view(),name='uploaddata'),
    path('AddTeamMember', views.AddTeamMember, name='AddTeamMember'),
    path('DeleteTeamMember', views.DeleteTeamMember, name='DeleteTeamMember'),
    path('AddProject',views.AddProject, name='AddProject'),
    path('DeleteProject',views.DeleteProject, name='DeleteProject'),
    path('ModifyProjectStatus',views.ChangeProjectStatus, name='ModifyProjectStatus'),
    path('Projects',views.team_projectdata, name='team_projectdata'),
    path('searchprojects',views.searchproject, name='searchprojects'),
    path('project_graph_data/<str:project1>',views.project_graph_data,name='project_graph_data'),
    
]