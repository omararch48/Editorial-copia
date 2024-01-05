from django.db import models
from apps.users.models import User
from .managers import AuthorManager


# Create your models here.
class Author(models.Model):
    STATUS_CHOICES = (
        ('0', 'Activo',),
        ('1', 'Inactivo',),
        ('2', 'Eliminado',),
    )
    user = models.ForeignKey(
        User,
        verbose_name='Usuario',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    bio = models.TextField(verbose_name='Semblanza', null=True, blank=True)
    status = models.CharField(
        verbose_name='Estado',
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='1'
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

    objects = AuthorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ('created',)

    def __str__(self) -> str:
        return f'{self.user}'