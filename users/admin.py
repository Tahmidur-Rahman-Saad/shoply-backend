from django.contrib import admin
from .models import Customer,AdminInfo

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')


@admin.register(AdminInfo)
class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone','nid')
    search_fields = ('user__username', 'phone','nid')

    
# admin.site.register(Customer,AdminInfo)
