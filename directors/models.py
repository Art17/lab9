from django.db import models


class Director(models.Model):
    class Meta:
        permissions = (('can_delete', 'my_perm for deleting  director'),)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars', default='avatars/no_avatar.jpg')
    birthdate = models.DateField()
    year = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(blank=True)


# Create your models here.
