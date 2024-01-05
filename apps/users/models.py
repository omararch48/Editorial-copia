from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('N', 'Sin registrar',),
        ('M', 'Masculino',),
        ('F', 'Femenino',),
        ('B', 'No binario',),
        ('O', 'Otro',),
        ('P', 'Prefiero no decirlo',),
    )
    STATUS_CHOICES = (
        ('0', 'Activo',),
        ('1', 'Inactivo',),
        ('2', 'Eliminado',),
    )
    username = models.CharField(
        verbose_name='Nombre de usuario',
        max_length=100,
        unique=True
    )
    email = models.EmailField(verbose_name='Email', unique=True)
    first_name = models.CharField(
        verbose_name='Nombres',
        max_length=50,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Apellidos',
        max_length=50,
        blank=True
    )
    gender = models.CharField(
        verbose_name='Género',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )
    status = models.CharField(
        verbose_name='Estado',
        max_length=1,
        choices=STATUS_CHOICES,
        blank=True,
        default='1'
    )
    image = models.URLField(
        verbose_name='Imagen',
        max_length=255,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(verbose_name='Activo', default=False)
    is_staff = models.BooleanField(verbose_name='Es staff', default=False)
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

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ('created',)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    def get_short_name(self):
        return f'{self.first_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'