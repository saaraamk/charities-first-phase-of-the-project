from django.db import models
from django.conf import settings

class Benefactor(models.Model):
    EXPERIENCE_CHOICES = [
        (0, 'Beginner'),
        (1, 'Intermediate'),
        (2, 'Expert'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    experience = models.SmallIntegerField(
        choices=EXPERIENCE_CHOICES, 
        default=0
    )
    free_time_per_week = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username


class Charity(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name



class Task(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    ]
    
    id = models.AutoField(primary_key=True)
    assigned_benefactor = models.ForeignKey(
        'Benefactor', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    charity = models.ForeignKey(
        'Charity', 
        on_delete=models.CASCADE
    )
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    gender_limit = models.CharField(
        max_length=1, 
        choices=[('M', 'Male'), ('F', 'Female')],
        null=True, 
        blank=True
    )
    state = models.CharField(
        max_length=1, 
        choices=STATUS_CHOICES, 
        default='P'
    )
    title = models.CharField(max_length=60)
    def __str__(self):
        return self.title