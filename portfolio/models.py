from ast import arg
from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import re


class Skill(models.Model):

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = "Skill"
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(blank =True, null=True, upload_to="Skills/")
    is_key_skill = models.BooleanField(default=False)
   

    def __str__(self):
        return self.name


class Tool(models.Model):

    class Meta:
        verbose_name_plural = 'Tools'
        verbose_name = "Tool"
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(blank =True, null=True, upload_to="Tools/")
    is_key_tool = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class AboutMe(models.Model):

    class Meta:
        verbose_name_plural = 'About Me'
        verbose_name = "About Me"

    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    banner = models.ImageField(blank=True, null=True, upload_to="banner/")
    

    def __str__(self):
        return self.title

class History(models.Model):

    class Meta:
        verbose_name_plural = 'Histotys'
        verbose_name = "Histoty"

    experience = models.IntegerField(default=10, blank=True, null=True)
    completed_project = models.IntegerField(default=10, blank=True, null=True)
    happy_client = models.IntegerField(default=10, blank=True, null=True)
    


class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar/")
    bio = models.CharField(max_length=200, blank=True, null=True)
    job = models.CharField(max_length=80, blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv/")
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    tools = models.ManyToManyField(Tool, blank=True)
    about_me = models.OneToOneField(AboutMe, on_delete=models.CASCADE, blank=True, null=True)
    histoty = models.OneToOneField(History, on_delete=models.CASCADE, blank=True, null=True)
    
    # Social Network
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):
    
    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'

        
class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio projects'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True )
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


