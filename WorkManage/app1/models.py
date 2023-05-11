from django.db import models

# Create your models here.
class Ishchi(models.Model):
    ismi = models.CharField(max_length=100)
    yoshi = models.PositiveIntegerField(null=True,blank=True)
    vazifasi = models.CharField(max_length=50)
    maoshi = models.IntegerField()
    bonusi  = models.IntegerField()
    karyera = models.IntegerField()
    ish_vaqti = models.IntegerField()

    def __str__(self):
        return self.ismi
