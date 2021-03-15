from django.db import models

class UserTab(models.Model):
    UName = models.CharField(max_length=64)
    LoginName = models.CharField(max_length=64)
    LoginPassword = models.CharField(max_length=256)


class TaskTab(models.Model):
    TName = models.CharField(max_length=64)
    TState = models.IntegerField()
    TCreate = models.ForeignKey(UserTab, on_delete=models.CASCADE, related_name='tc')
    TManager = models.ForeignKey(UserTab, on_delete=models.CASCADE, related_name='tm')
    TPlanFinishTimestamp = models.DateField()
    TDescription = models.TextField()
    TGrade = models.IntegerField()



class TaskPartnerTab(models.Model):
    TaskID = models.ForeignKey(TaskTab, on_delete=models.CASCADE, related_name='tid')
    UserID = models.ForeignKey(UserTab, on_delete=models.CASCADE, related_name='uid')