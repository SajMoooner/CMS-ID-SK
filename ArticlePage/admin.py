from django.contrib import admin
from .models import Article, Subtitle, TargetAudience, Department, LifeSituation

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'main_message', 'target_audience', 'created_at', 'life_situation')
    # Můžete přidat další konfigurace admin třídy, např. list_filter, search_fields atd.

admin.site.register(Article, ArticleAdmin)
admin.site.register(Subtitle)
admin.site.register(TargetAudience)
admin.site.register(Department)
admin.site.register(LifeSituation)

