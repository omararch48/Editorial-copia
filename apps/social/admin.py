from django.contrib import admin
from django.utils.html import format_html
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    list_display = [
        'list_str',
        'order',
        'link',
        'status',
    ]
    list_filter = ['active',]

    @admin.display(description='Red Social (Nombre clave)')
    def list_str(self, obj):
        return str(obj)

    @admin.display(description='Enlace')
    def link(self, obj):
        return format_html(
            f'''
                <a href={obj.url} target="_blank">{obj.url}</a>
            '''
        )

    @admin.display(ordering='active', description='Estado')
    def status(self, obj):
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
                <span style="color: {STATUS_COLORS[obj.active]}">
                    {STATUS_DICT[obj.active]}
                </span>
            '''            
        )


admin.site.register(Link, LinkAdmin)