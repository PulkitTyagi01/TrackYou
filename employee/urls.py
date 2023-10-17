from . import views
from django.urls import path

# from TrackYou import adminn

app_name = 'employee'

urlpatterns = [
   path('changepasssword',views.changepassword.as_view(),name='changepassword'),
   path('dailyupdate',views.DailyUpdate, name='dailyupdate'),
   path('edit_profile',views.edit_profile, name='edit_profile'),
   path('emp/<str:name1>',views.emp_data,name='employee_data'),
]