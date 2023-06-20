from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name',]
    fieldsets = UserAdmin.fieldsets + (('Contact Info', {'fields':('phone_number',)}),)

    # fieldsets= (
    #     ('Auth Info',{
    #         'fields':('username','email','password'
    #         )}
    #     ),
    #     ('personal Info',{
    #         'fields':('first_name','last_name','phone_number'
    #         )}
    #     ),
    #     ('Dates',{
    #         'classes':('collapse',),
    #         'fields':('date_joined','last_login'

    #         )}
    #     ),
    #     ('permissions',{
    #         'fields':(
    #             'is_active',
    #             'is_staff',
    #             'is_superuser',
    #             'user_permissions',
    #             'groups')
    #     }

    #     )
    # )

admin.site.register(CustomUser, CustomUserAdmin)