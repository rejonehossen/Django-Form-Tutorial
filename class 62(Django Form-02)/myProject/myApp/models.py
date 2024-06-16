from django.db import models
from django.contrib.auth.models import AbstractUser

class customuser(AbstractUser):
    usertype=[
        ('admin','Admin'),
        ('user','User'),
    ]
    
    
    
    city=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to='static/picture/user',null=True)
    usertype=models.CharField(max_length=100,choices=usertype,null=True)
    
    class Meta:
        ordering=["last_name","first_name"]
        verbose_name="Users Model"
        db_table="Django Form Table"
        unique_together=["username","email"]
        verbose_name_plural="Custom User"



class categorymodel(models.Model):
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE,null=True)
    categoryname=models.CharField(max_length=100,null=True)
    create_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)
    
    class Meta:
        ordering=["categoryname"]
        verbose_name="Category Model"
        db_table="Category Table"
        unique_together=['categoryname']
        

class TaskModel(models.Model):
    priotiry=[
        ("high","High"),
        ("medium","Medium"),
        ("low","Low"),
    ]
    created_by=models.ForeignKey(customuser,on_delete=models.CASCADE, null=True)
    categorytast=models.ForeignKey(categorymodel,on_delete=models.CASCADE, null=True)
    priotiry=models.CharField(choices=priotiry,max_length=100,null=True)
    taskname=models.CharField(max_length=100,null=True)
    due_date=models.DateField(null=True)
    date=models.DateField(null=True)
    description=models.TextField(max_length=500,null=True)
    status=models.CharField(max_length=100,default="On_Going",null=True)
    create_at=models.DateField(auto_now_add=True,null=True)
    update_at=models.DateField(auto_now=True,null=True)
    completed_date=models.DateField(null=True)
    
    
    # class Meta:
    #     unique_together=[""]