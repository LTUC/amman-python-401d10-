from django.contrib import admin
# Register your models here.
from .models import Snack

class CustomSnackAdmin(admin.ModelAdmin):
    model = Snack
    list_display = ['name', 'purchaser', 'desc',]
    fieldsets= (
        ('Owner',{
            'fields':('purchaser',
            )}
        ),
        ('snack info',{
            'fields':('name','desc',
            )}
        )
    )

    
admin.site.register(Snack, CustomSnackAdmin)