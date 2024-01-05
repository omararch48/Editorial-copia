from django.contrib import admin
from django.utils.html import format_html
from .models import Author


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'created',
        'state',
    ]
    list_filter = ['status',]
    search_fields = ['user',]

    @admin.display(ordering='status', description='Estado')
    def state(self, obj):
        STATUS_DICT = {
            '0': 'Activo',
            '1': 'Inactivo',
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

admin.site.register(Author, AuthorAdmin)