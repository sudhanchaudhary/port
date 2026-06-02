from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=200, null=True, blank=True)
    email=models.EmailField(null=True,blank=True)
    message=models.TextField(null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    resume=models.FileField(upload_to='Resume')
    date=models.DateTimeField(auto_now_add=True)
    
class TechCategory(models.Model):
    title=models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
class Skill(models.Model):
            
    Skill_Level=(
    ('Beginner','Beginner'),
    ('Intermediate','Intermediate'),
    ('Expert','Expert')
     )
    tech=models.ForeignKey(TechCategory, on_delete=models.CASCADE)
    skill=models.CharField(max_length=200)
    experience=models.IntegerField(default='1')
    level=models.CharField(choices=Skill_Level)
    def __str__(self):
        return self.skill
    
class Project(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    github=models.CharField(max_length=300,blank=True,null=True)
    live=models.CharField(max_length=300,blank=True,null=True)
    def __str__(self):
        return self.title
    
class Project_Features(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='feature')
    feature=models.CharField(max_length=300)
    def __str__(self):
        return self.feature

class Project_Skill(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='skill')
    skill=models.CharField(max_length=50)
    
                                                                                                       