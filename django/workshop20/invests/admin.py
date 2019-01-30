from django.contrib import admin
from .models import Question, Choice
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('content', 'votes',)

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice, ChoiceAdmin)