from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Portfolio,
    Skill,
    AboutMe,
    Services,
    Resume,
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)



@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'is_active',)
    readonly_fields = ('slug',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title_education', 'title_experience', )
    

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('title','id',)


@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'name',)
