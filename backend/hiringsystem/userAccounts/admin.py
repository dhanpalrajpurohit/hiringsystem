from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.admin import UserAdmin

from .models import Users
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Users
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_Company', 'is_Candidate')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',  'is_Company', 'is_Candidate')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Users, CustomUserAdmin)
