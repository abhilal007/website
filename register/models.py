from django.db import models
from django.urls import reverse

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
ROLE_CHOICES = (('S', 'Student'), ('M', 'Mentor'), ('B', 'Both'))
GOAL_CHOICES = (('startup', 'startup'), ('higher_studies', 'Higher Studies'), ('job', 'Job'), ('other', 'Others'))


class User_info(models.Model):

    firstname = models.CharField(max_length=20, blank=False, unique=False)
    lastname = models.CharField(max_length=20, blank=False, unique=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact = models.CharField(max_length=11)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)
    blog_url = models.URLField(max_length=200)
    twitter_id = models.CharField(max_length=30)
    topcoder_handle = models.CharField(max_length=30)
    github_id = models.CharField(max_length=30)
    bitbucket_id = models.CharField(max_length=30)
    typing_speed = models.BigIntegerField()
    interest = models.CharField(max_length=200)
    expertise = models.CharField(max_length=200)
    goal = models.CharField(max_length=15, choices=GOAL_CHOICES)
    username = models.CharField(max_length=20, unique=True, blank=False, primary_key=True)
    email = models.EmailField(blank=False, unique=True) 
    password = models.CharField(max_length=255, blank=False)

    class Meta:
        db_table = 'User_info'

    def get_absolute_url(self):
        return reverse('proposal-detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.firstname + ' ' + self.lastname

    def __str__(self):
        return self.username + ' ' + self.lastname
