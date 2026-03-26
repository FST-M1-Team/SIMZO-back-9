from django.contrib import admin
from .models import User, InfluenceurProfile, AnnonceurProfile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'is_staff', 'is_active')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(InfluenceurProfile)
admin.site.register(AnnonceurProfile)
