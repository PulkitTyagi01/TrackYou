from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.core.exceptions import ValidationError



class TeamAndManager(models.Model):
    name = models.CharField(max_length=20,blank=False, null=False)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} : {}'.format(self.name, self.manager)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_name')
    team = models.ForeignKey(TeamAndManager, on_delete=models.CASCADE)
    #declaring role choices
    EMPLOYEE , MANAGER , ADMIN = 1, 2 , 3
    ROLE = (
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin')
    )
    role = models.IntegerField(choices=ROLE, blank=False, null=False, default=EMPLOYEE)
    # forgot_password = models.CharField(max_length=100)
    #Note: This foreign key is diff.
    # parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='parent_name')

    def __str__(self):
        return '{} {} {}'.format(self.user, self.team, self.get_role_display())

    # This function returns every member of particular manager.
    # def team(self):
    #     return Profile.objects.filter(parent = self)


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField(blank=True, null=True)
    ACTIVE, ON_HOLD, COMPLETED = 1, 2, 3
    STATUS = (
        (ACTIVE, 'Active'),
        (ON_HOLD, 'On_hold'),
        (COMPLETED, 'Completed')
    )
    status = models.IntegerField(choices=STATUS, blank=False, null=False, default=ACTIVE)
    team = models.ForeignKey(TeamAndManager, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.name, self.get_status_display(), self.team)


class UserProject(models.Model):
    user = models.ForeignKey(User, db_index=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} {}'.format(self.user, self.project)

class UserProjectProgress(models.Model):
    userproject = models.ForeignKey(UserProject, on_delete=models.CASCADE)
    daily_hours = models.DecimalField(blank=False, max_digits=4, decimal_places=2, null=False)
    daily_report = models.TextField(blank = True, null = True)
    date = models.DateTimeField(blank=False, null=False, default=now)

    def save(self):
        if self.userproject:
            project_status = self.userproject.project.status
            if((project_status != 1) and self.userproject.project.end_date < self.date):
                raise ValidationError("This project is either 'on hold' or 'completed'")
            else:
                super().save()

    def __str__(self) -> str:
        return '{} {} {}'.format(self.userproject, self.date, self.daily_hours)

class POC(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_report = models.TextField(blank = True, null = True)
    date = models.DateTimeField(blank=False, null=False, default=now)

    def __str__(self) -> str:
        return '{} {}'.format(self.user, self.date)
