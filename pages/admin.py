from django.contrib import admin
from .models import About, Skill, Project, Contact, Resume

# About Admin
class AboutAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'subtitle', 'description', 'name', 'email', 'photo', 'phone')
 list_display_links = ('id', 'title', 'subtitle')
 list_filter = ('name', 'subtitle')
 search_fields = ('title', 'subtitle', 'description', 'name', 'email', 'photo', 'phone')
 list_per_page = 10

admin.site.register(About, AboutAdmin)

# Skill Admin
class SkillAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'skill_1', 'skill_1_1', 'skill_1_2', 'skill_1_3', 'skill_1_4', 'skill_1_5', 'skill_1_5', 'skill_1_6', 'skill_1_7', 'skill_1_8', 'skill_1_9', 'skill_1_10', 'skill_1_11', 'skill_1_12')
 list_display_links = ('id', 'title', 'skill_1')
 list_filter = ('title', 'skill_1_1')
 search_fields = ('id', 'title', 'skill_1', 'skill_1_1', 'skill_1_2', 'skill_1_3', 'skill_1_4', 'skill_1_5', 'skill_1_5', 'skill_1_6', 'skill_1_7', 'skill_1_8', 'skill_1_9', 'skill_1_10', 'skill_1_11', 'skill_1_12')
 list_per_page = 10

admin.site.register(Skill, SkillAdmin)

# Project Admin
class ProjectAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'skills_used', 'description', 'url_live', 'source_code', 'photo')
 list_display_links = ('id', 'title')
 list_filter = ('title', 'skills_used')
 search_fields = ('id', 'title', 'skills_used ', 'description', 'url_live', 'source_code', 'photo')
 list_per_page = 10

admin.site.register(Project, ProjectAdmin)

# Contact Admin
class ContactAdmin(admin.ModelAdmin):
 list_display = ('id', 'name', 'email', 'contact_date', 'phone')
 list_display_links = ('id', 'name')
 list_filter = ('id', 'name')
 search_fields = ('name', 'email', 'phone')
 list_per_page = 10

admin.site.register(Contact, ContactAdmin)

# Resume Admin
class ResumeAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'description', 'resume')
 list_display_links = ('id', 'title')
 list_filter = ('id', 'title')
 search_fields = ('title', 'resume', 'description')
 list_per_page = 10

admin.site.register(Resume, ResumeAdmin)

