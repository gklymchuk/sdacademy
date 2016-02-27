from django.contrib import admin
from coaches.models import Coach


class CoachAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'gender', 'skype', 'description']
    list_filter = ['id', ('user__is_staff', admin.BooleanFieldListFilter)]

admin.site.register(Coach, CoachAdmin)
