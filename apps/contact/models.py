from django.db import models
# from .managers import ContactMessageManager


# Create your models here.
class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ('0', 'Sin contestar'),
        ('1', 'Contestado'),
        ('2', 'Eliminado'),
    )
    SUBJECT_CHOICES = (
        ('0', 'Publicaciones'),
        ('1', 'Servicios editoriales'),
        ('2', 'Otro'),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    subject = models.CharField(
        default='0',
        max_length=1,
        choices=SUBJECT_CHOICES
    )
    message = models.TextField(null=True, blank=True)
    status = models.CharField(
        default='0',
        max_length=1,
        choices=STATUS_CHOICES
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación',
        null=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Fecha de edición',
        null=True
    )

    class Meta:
        verbose_name = 'Mensaje de contacto'
        verbose_name_plural = 'Mensajes de contacto'
        ordering = ('created',)

    # objects = ContactMessageManager()

    def get_message(self):
        STATUS_DICT = {
            '0': 'Sin contestar',
            '1': 'Contestado',
            '2': 'Mensaje eliminado',
        }
        return f'{self.id} {self.name} {STATUS_DICT[self.status]}'
