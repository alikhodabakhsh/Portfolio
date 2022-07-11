from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Portfolio,
    Skill,
    Tool,
    AboutMe,
    History,
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user',)

@admin.register(ContactProfile)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('timestamp', 'name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active',)
    readonly_fields = ('slug',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id','title',)

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id','experience')

