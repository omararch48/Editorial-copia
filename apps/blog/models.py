from django.db import models
from autoslug import AutoSlugField
from apps.authors.models import Author
from apps.multimedia.models import MediaImage
from ckeditor.fields import RichTextField
from .managers import PostsManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name='Categoría', max_length=255)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        editable=True,
        blank=True,
        null=True
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de edición'
    )

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created',]

    def __str__(self) -> str:
        return f'{self.name}'


class Post(models.Model):
    STATUS_CHOICE = (
        ('0', 'Activo',),
        ('1', 'Inactivo',),
        ('2', 'Eliminado',),
    )
    title = models.CharField(
        max_length=200, 
        verbose_name='Título'
    )
    slug = AutoSlugField(
        populate_from='title',
        unique=True,
        editable=True,
        blank=True,
        null=True
    )
    intro = models.TextField(
        verbose_name='Introducción', blank=True, null=True, default=None
    )
    content = RichTextField(
        verbose_name='Contenido'
    )
    image = models.ForeignKey(
        MediaImage,
        verbose_name='Imagen',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    author = models.ForeignKey(
        Author, 
        verbose_name='Autor', 
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField(
        Category, 
        verbose_name='Categorias'
    )
    status = models.CharField(
        max_length=1, 
        verbose_name='Estado', 
        choices=STATUS_CHOICE, 
        default='0'
    )
    created = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Fecha de creación'
    )
    updated = models.DateTimeField(
        auto_now=True, 
        verbose_name='Fecha de edición'
    )

    objects = PostsManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['status', '-created']


    def __str__(self) -> str:
        return f'{self.title}'