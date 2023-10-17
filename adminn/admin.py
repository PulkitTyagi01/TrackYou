from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(TeamAndManager)
admin.site.register(UserProject)
admin.site.register(UserProjectProgress)
admin.site.register(POC)
