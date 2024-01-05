from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from apps.authors.models import Author
from apps.multimedia.models import MediaImage
from .managers import MagazineManager, MagazineArticleManager
from ckeditor.fields import RichTextField


# Create your models here.
class Magazine(models.Model):
    MAGAZINE_CHOICES = {
        ('0', 'Revista principal',),
        ('1', 'Revista secundaria',),
    }
    STATUS_CHOICES = {
        ('0', 'Activo',),
        ('1', 'Inactivo',),
        ('2', 'Eliminado',),
    }
    magazine = models.CharField(
        verbose_name='Revista',
        max_length=1,
        default='0',
        choices=MAGAZINE_CHOICES
    )
    magazine_name = models.CharField(
        verbose_name='Nombre del ejemplar', max_length=255
    )
    intro_author = models.ForeignKey(
        Author,
        verbose_name='Autor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    slug = AutoSlugField(
        populate_from='magazine_name',
        unique=True,
        editable=True,
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name='Estado',
        max_length=1,
        default='0',
        choices=STATUS_CHOICES
    )
    intro_text = RichTextField(verbose_name='Introducción')
    image = models.ForeignKey(
        MediaImage,
        verbose_name='Imagen',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    created = models.DateField(
        verbose_name='Fecha de creación',
        auto_now_add=True,
        null=True
    )
    updated = models.DateField(
        verbose_name='Fecha de edición',
        auto_now=True,
        null=True
    )

    objects = MagazineManager()

    class Meta:
        verbose_name = 'Revista'
        verbose_name_plural = 'Revistas'

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.slug)])

    def __str__(self) -> str:
        magazine_choices = {
            '0': 'Revista principal',
            '1': 'Revista secundaria',
        }
        return f'{magazine_choices[self.magazine].upper()}: {self.magazine_name}'


class MagazineArticle(models.Model):
    STATUS_CHOICES = {
        ('0', 'Activo',),
        ('1', 'Inactivo',),
        ('2', 'Eliminado',),
    }
    author = models.ForeignKey(
        Author,
        verbose_name='Autor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    magazine = models.ForeignKey(
        Magazine,
        verbose_name='revista',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    article_title = models.CharField(verbose_name='Título', max_length=255)
    article_number = models.PositiveSmallIntegerField(
        verbose_name='Número de artículo'
    )
    slug = AutoSlugField(
        populate_from='article_title',
        unique=True,
        editable=True,
        blank=True,
        null=True
    )
    place = models.CharField(
        verbose_name='Lugar',
        max_length=255,
        null=True,
        blank=True
    )
    status = models.CharField(
        verbose_name='Estado',
        max_length=1,
        default='0',
        choices=STATUS_CHOICES
    )
    text = RichTextField(verbose_name='Articulo')
    created = models.DateField(
        verbose_name='Fecha de creación',
        auto_now_add=True,
        null=True
    )
    updated = models.DateField(
        verbose_name='Fecha de edición',
        auto_now=True,
        null=True
    )

    objects = MagazineArticleManager()

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def get_absolute_url(self):
        return reverse('detail', args = [str(self.slug)])

    def __str__(self) -> str:
        status_dict = {
            '0': 'Activo',
            '1': 'Inactivo',
            '2': 'Eliminado',
        }
        return f'{self.magazine} // {self.article_title}, id: {self.article_number} ({status_dict[self.status]})'