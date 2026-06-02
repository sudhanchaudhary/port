from django.contrib import admin
from .models import Message,Skill,Portfolio,TechCategory,Project,Project_Features,Project_Skill

# Register your models here.
admin.site.register(Message)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(TechCategory)

class ProjectFeatureAdmin(admin.TabularInline):
    model=Project_Features
    extra=2
class ProjectSkillAdmin(admin.TabularInline):
    model=Project_Skill
    extra=2
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','desc']
    inlines=[ProjectFeatureAdmin,ProjectSkillAdmin]