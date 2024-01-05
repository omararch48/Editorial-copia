from django.contrib import admin
from django.utils.html import format_html
from .models import MediaImage, Image


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ['indentificador_imagen', 'url_imagen', 'created']
    # readonly_fields = ['image']

    @admin.display(ordering='id')
    def indentificador_imagen(self, obj):
        return f'Id imagen: {obj.id}'

    @admin.display
    def url_imagen(self, obj):
        return format_html(
            f'''
                <a href={obj.image.url}>{obj.image.url}</a>
            '''
        )

class MediaImageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'user_owner',
        'imagen',
        'fuente',
        'is_active',
        'created',
        'updated',
    ]
    search_fields = ['name']
    readonly_fields = ['is_active', 'destroy']
    list_filter = ['is_active']

    @admin.display
    def imagen(self, obj):
        return format_html(
            f'''
                <div
                    style="display: flex; align-items: center; justify-content: center;"
                >
                    <img
                        style="width: 120px;"
                        src="{obj.get_url()}"
                        alt="Imagen no disponible"
                    />
                </div>
            '''
        )

    @admin.display
    def fuente(self, obj):
        if obj.image:
            return 'Imagen'
        return 'Url'


admin.site.register(MediaImage, MediaImageAdmin)
admin.site.register(Image, ImageAdmin)