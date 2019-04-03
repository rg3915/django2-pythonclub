from django.db import models
from django.urls import reverse_lazy


class Band(models.Model):

    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'band'
        verbose_name_plural = 'bands'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # retorna a url no formato /bands/1/
        return reverse_lazy('band_detail', kwargs={'pk': self.pk})

    def get_members_count(self):
        # count members by band
        # conta os membros por banda
        return self.band.count()


class Member(models.Model):

    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
        ('g', "Guitar"),
        ('b', "Bass"),
        ('d', "Drums"),
        ('v', "Vocal"),
        ('p', "Piano"),
    ),
        max_length=1
    )

    band = models.ForeignKey(
        "Band",
        related_name='band',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.name
