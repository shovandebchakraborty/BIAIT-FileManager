from django.db import models

# Create your models here.
class UserFile(models.Model):
    COURSE_TYPE = [
        ("ai & prompt engineering","AI & Prompt Engineering"),
        ("python programming","Python Programming"),
        ("web developer","Web Developer")
    ]
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,default="unknown")
    course = models.CharField(max_length=100, choices=COURSE_TYPE)
    files =  models.FileField(upload_to='userfiles/',null=False,blank=False)
    
    def __str__(self):
        return f"{self.username} | {self.course}"