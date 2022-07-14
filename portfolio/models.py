from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
import re


STATUS = (
    ("Doing", "Doing"),
    ("Complated", "Complated"),

)


class Skill(models.Model):

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = "Skill"
    name = models.CharField(max_length=20, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="Skills/")
    score = models.IntegerField( blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class AboutMe(models.Model):

    class Meta:
        verbose_name_plural = 'About Me'
        verbose_name = "About Me"

    title = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    banner = models.ImageField(blank=True, null=True, upload_to="banner/")
    project = models.IntegerField(blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    clients = models.IntegerField(blank=True, null=True)
    winner = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title



class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(blank=True, null=True, upload_to="avatar/")
    job = models.CharField(max_length=80, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv/")
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    about_me = models.OneToOneField(
        AboutMe, on_delete=models.CASCADE, blank=True, null=True)
  
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
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'


class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio'
        verbose_name = 'Portfolio'
        ordering = ["name"]

    name = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    sub_title = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(null=False, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    final_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS )
    tag = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Services(models.Model):

    class Meta:
        verbose_name_plural = 'Services'
        verbose_name = "Service"

    title = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="Services/")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Resume(models.Model):

    class Meta:
        verbose_name_plural = 'Resume'
        verbose_name = "Resume"

    title_education = models.CharField(max_length=200, blank=True, null=True)
    description_education = models.CharField(
        max_length=200, blank=True, null=True)
    date_education = models.CharField(max_length=20,
        blank=True, null=True)

    title_experience = models.CharField(max_length=200, blank=True, null=True)
    description_experience = models.CharField(
        max_length=200, blank=True, null=True)
    date_experience = models.CharField(max_length=20,
        blank=True, null=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title_education}, {self.title_experience}'
