import os
from django.db import models
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
from apps.users.models import User


# Create your models here.
class Image(models.Model):
    image = models.ImageField(verbose_name='Imagen', upload_to='images')
    created = models.DateField(
        verbose_name='Fecha de creación',
        auto_now_add=True,
        null=True
    )

    class Meta:
        verbose_name = 'Imagen archivo'
        verbose_name_plural = 'Imagenes archivo'

    def __str__(self) -> str:
        return f'Imagen creada en: {self.created}'


class MediaImage(models.Model):
    user_owner = models.ForeignKey(
        User,
        verbose_name='Propietario',
        on_delete=models.SET_NULL,
        null=True,
        related_name='mediaobjects'
    )
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        related_name='mediaobjects'
    )
    name = models.CharField(verbose_name='Nombre', null=True, blank=True)
    url = models.URLField(
        verbose_name='URL',
        max_length=255,
        null=True,
        blank=True,
        default=None
    )
    is_active = models.BooleanField(verbose_name='Activo', default=True)
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
    destroy = models.DateField(
        verbose_name='Fecha de destrucción',
        null=True,
        blank=True,
        default=None
    )

    def get_url(self):
        url = ''
        if self.image:
            url = f'{self.image.image.url}'
            if self.image.image.url[0] == '/':
                url = f'{settings.BASE_URL}{self.image.image.url}'
        else:     
            url = f'{self.url}'
        return url

    def save(self, *args, **kwargs):
        if self.image == None and self.url == None:
            raise('Error, the model needs an image or url')
        elif self.image != None and self.url != None:
            raise('Error, the model needs only an image or only a url')
        super().save(*args, **kwargs)

    constraints = [
        models.CheckConstraint(
            check=(
                (models.Q(image__isnull=False) & models.Q(url__isnull=True)) |
                (models.Q(image__isnull=True) & models.Q(url__isnull=False))
            ),
            name='exclusive_image_or_url_null_check'
        )
    ]

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self) -> str:
        return f'{self.name}'
    # check=~(models.Q(url__isnull=True) & models.Q(image__isnull=True)),


@receiver(post_delete, sender=Image)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(pre_delete, sender=MediaImage)
def delete_image(sender, instance, **kwargs):
    if instance.image:
        image = Image.objects.get(id=instance.image.id)
        instance.image = None
        instance.url = 'delete'
        instance.save()
        image.delete()