import secrets

from django.db import models


class CiudadModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", help_text="(Obligatorio)")
    slug = models.SlugField(max_length=50, unique=True, verbose_name="Slug", help_text="(Obligatorio)")

    class Meta:
        db_table = "ciudades"
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = secrets.token_hex(4)
            while CiudadModel.objects.filter(slug=prov).exists():
                prov = secrets.token_hex(4)
            self.slug = prov
        super().save(*args, **kwargs)
