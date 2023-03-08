from django.db import models
from datetime import datetime

class About(models.Model):
 title = models.CharField(max_length=100)
 subtitle = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 name = models.CharField(max_length=100)
 email = models.CharField(max_length=100)
 phone = models.CharField(max_length=100)
 photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
 def __str__(self):
  return self.title


class Skill(models.Model):
 title = models.CharField(max_length=100)
 skill_1 = models.CharField(max_length=100)
 skill_1_1 = models.CharField(max_length=100)
 skill_1_2 = models.CharField(max_length=100)
 skill_1_3 = models.CharField(max_length=100)
 skill_1_4 = models.CharField(max_length=100)
 skill_1_5 = models.CharField(max_length=100)
 skill_1_6 = models.CharField(max_length=100)
 skill_1_7 = models.CharField(max_length=100)
 skill_1_8 = models.CharField(max_length=100)
 skill_1_9 = models.CharField(max_length=100)
 skill_1_10 = models.CharField(max_length=100)
 skill_1_11 = models.CharField(max_length=100)
 skill_1_12 = models.CharField(max_length=100)
 def __str__(self):
  return self.title

class Project(models.Model):
 title = models.CharField(max_length=200)
 skills_used = models.TextField(blank=True)
 description = models.TextField(blank=True)
 photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
 url_live = models.CharField(max_length=200)
 source_code = models.CharField(max_length=200)
 def __str__(self):
  return self.title


class Contact(models.Model):
 name = models.CharField(max_length=200)
 email = models.CharField(max_length=100)
 phone = models.CharField(max_length=100)
 message = models.TextField(blank=True)
 contact_date = models.DateTimeField(default=datetime.now, blank=True)
 user_id = models.IntegerField(blank=True)
 def __str__(self):
  return self.name

class Resume(models.Model):
 title = models.CharField(max_length=200)
 resume = models.CharField(max_length=200)
 description = models.TextField(blank=True)
 def __str__(self):
  return self.title




 


