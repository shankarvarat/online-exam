from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class profile(models.Model):
    name=models.CharField(max_length=200,default="No Name")
    username=models.OneToOneField(User,on_delete='CASCADE')
    gender=models.CharField(max_length=100)
    mob=models.IntegerField()
    def __str__(self):
        return self.name
class subject(models.Model):
    subid=models.IntegerField(primary_key=True,auto_created=True,default=3000)
    subname=models.CharField(max_length=100)
    def __str__(self):
        return self.subname
class test(models.Model):
    subid=models.ForeignKey(subject,on_delete='CASCADE')
    tname=models.CharField(max_length=200)
    def __str__(self):
        return self.tname
class questions(models.Model):
    question=models.TextField(max_length=300)

    tname=models.ForeignKey(test,on_delete='CASCADE')
    a1=models.CharField(max_length=100)
    a2=models.CharField(max_length=100)
    a3=models.CharField(max_length=100)
    a4=models.CharField(max_length=100)
    ta=models.CharField(max_length=100)
    def __str__(self):
        return self.question
class ua(models.Model):
    tname=models.ForeignKey(test,on_delete='CASCADE')
    name=models.ForeignKey(profile,on_delete='CASCADE')
    question = models.TextField(max_length=300)

    a1 = models.CharField(max_length=100)
    a2 = models.CharField(max_length=100)
    a3 = models.CharField(max_length=100)
    a4 = models.CharField(max_length=100)
    ta = models.CharField(max_length=100)
    ua = models.CharField(max_length=100)
    def __str__(self):
        return self.name


