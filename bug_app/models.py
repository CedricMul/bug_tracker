from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    def __str__(self):
        return self.username

class Ticket(models.Model):
    status_choices = [
        "New",
        "In Progress",
        "Completed",
        "Invalid"
    ]
    title = models.CharField(max_length=120)
    time_and_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    user_filed = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=status_choices, default="New")
    assigned_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    completed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
