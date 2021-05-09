from django.db import models

class Hero(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField("Hero's name",max_length=50, null=False, blank=False)
    group = models.CharField("Primary attribute",max_length=50, null=False, blank=False)

    class Meta:
        verbose_name = 'Hero'
        verbose_name_plural = 'Heros'
        ordering = ['id']
    
    def __str__(self):
        return self.name
