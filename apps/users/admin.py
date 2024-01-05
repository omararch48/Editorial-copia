from django.contrib import admin
from django.utils.html import format_html
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'last_name',
        'first_name',
        'email',
        'grupos',
        'is_superuser',
        'is_staff',
        'is_active',
        'estado',
        'imagen',
    ]
    search_fields = ['last_name', 'first_name', 'email']
    list_display_links = ['last_name', 'email']
    ordering = ['id', 'last_name', 'first_name']
    filter_horizontal = ['groups', 'user_permissions']
    list_filter = ['status', 'is_superuser', 'is_staff', 'is_active']

    # list_filter = (
    #     ('status', {'title': 'Estado'}),
    #     ('is_superuser', {'title': 'Superusuario'}),
    #     ('is_staff', {'title': 'Personal'}),
    #     ('is_active', {'title': 'Activo'}),
    #     ('groups', {'title': 'Grupos'}),
    # )
    # raw_id_fields = ['groups']

    @admin.display
    def grupos(self, obj):
        user_groups = obj.groups.all()
        if len(user_groups) == 0:
            return 'No hay grupos'
        groups_html = ''
        for group in user_groups:
            groups_html += f'<li>{group}</li>'
        return format_html(
            f'''
                <ul>{groups_html}</ul>
            '''
        )

    @admin.display(ordering='status')
    def estado(self, obj):
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
        if obj.is_superuser and obj.id != 1:
            return format_html(
                f'''
                    <span style="color: {STATUS_COLORS[obj.status]}">
                        {STATUS_DICT[obj.status]}
                    </span>
                    <script>
                        alert(
                            'Advertencia: HAY MÁS DE UN SUPERUSUARIO - {obj.id} {obj.last_name} {obj.first_name} -'
                        )
                    </script>
                '''            
            )
        return format_html(
            f'''
                <span style="color: {STATUS_COLORS[obj.status]}">
                    {STATUS_DICT[obj.status]}
                </span>
            '''            
        )

    @admin.display
    def imagen(self, obj):
        if obj.image == None or obj.image == '':
            return format_html(
                f'''
                    <div
                        style="display: flex; align-items: center; justify-content: center;"
                    >
                        <span style="color: royalblue; text-transform: uppercase; font-size: 20px; padding: 5px 0;">
                            Sin imagen
                        </span>
                    </div>
                '''
            )            
        return format_html(
            f'''
                <div
                    style="display: flex; align-items: center; justify-content: center;"
                >
                    <img
                        style="width: 120px;"
                        src="{obj.image}"
                        alt="Imagen no disponible"
                    />
                </div>
            '''
        )


admin.site.register(User, UserAdmin)