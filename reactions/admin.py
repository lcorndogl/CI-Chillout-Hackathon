from django.contrib import admin
from .models import Score


# Register your models here.
@admin.register(Score)
class ScoresAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'created_on', 'updated_on')
    list_filter = ('created_on', 'updated_on')
    search_fields = ('user',)
    ordering = ('created_on',)
