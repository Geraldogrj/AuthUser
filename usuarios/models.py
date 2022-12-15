from django.db import models
from django.contrib.auth.models import AbstractUser

class Users (AbstractUser):
    choices_perfil = (
        ('tecnico' , 'tecnico'),
        ('controlador' , 'controlador'),
        ('chefe' , 'chefe'),
        ('comandante' , 'comandante'),
    )
    
    perfil = models.CharField(max_length=15, choices=choices_perfil)