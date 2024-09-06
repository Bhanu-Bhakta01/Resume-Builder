from django.contrib import admin
from .models import (
    PersonalInfo,
    Education,
    WorkExperience,
    Skill,
    Certification,
    Project,
    Language,
    Interest,
    Reference
)

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'start_date', 'end_date', 'personal_info')
    search_fields = ('degree', 'institution', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('degree', 'institution', 'start_date')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'start_date', 'end_date', 'personal_info')
    search_fields = ('job_title', 'company_name', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('job_title', 'company_name', 'start_date')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'personal_info')
    search_fields = ('name', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('proficiency',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'date_obtained', 'valid_until', 'personal_info')
    search_fields = ('name', 'organization', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('organization', 'date_obtained')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies_used', 'start_date', 'end_date', 'personal_info')
    search_fields = ('title', 'technologies_used', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('start_date', 'end_date')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'personal_info')
    search_fields = ('name', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('proficiency',)

@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('name', 'personal_info')
    search_fields = ('name', 'personal_info__first_name', 'personal_info__last_name')

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'company', 'email', 'personal_info')
    search_fields = ('name', 'company', 'personal_info__first_name', 'personal_info__last_name')
    list_filter = ('company',)
