from django.contrib import admin
from .models import Application
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# admin.site.register(User)
# admin.site.register(Department)

#admin.site.register(Application)

admin.site.unregister(User)
@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields=[
        'date_joined',
    ]
    def get_form(self, request, obj = None,  **kwargs):
        form= super().get_form(request, obj, **kwargs)
        is_super=request.user.is_superuser
        if not is_super:
            form.base_fields['username'].disabled=True
        return form
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display=("name","applying_to")
    search_fields=("name__startswith", )