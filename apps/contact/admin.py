from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage


# Register your models here.
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'state',
    ]
    list_filter = [
        'status',
    ]
    search_fields = ['name', 'email', 'phone']
    readonly_fields = [
        'name',
        'email',
        'phone',
        'subject',
        'message',
    ]

    @admin.display(ordering='active', description='Estado')
    def state(self, obj):
        STATUS_DICT = {
            '0': 'Sin contestar',
            '1': 'Contestado',
            '2': 'Eliminado',
        }
        STATUS_COLORS = {
            '0': 'green',
            '1': 'royalblue',
            '2': 'red',
        }
        return format_html(
            f'''
                <span style="color: {STATUS_COLORS[obj.status]}">
                    {STATUS_DICT[obj.status]}
                </span>
            '''            
        )
        

admin.site.register(ContactMessage, ContactMessageAdmin)