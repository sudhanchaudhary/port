from django.contrib import admin
from .models import Message,Skill,Portfolio,TechCategory

# Register your models here.
admin.site.register(Message)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(TechCategory)