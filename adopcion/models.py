from django.db import models

# Create your models here.
class Mascota(models.Model):
    id_mascota      =models.AutoField(db_column='idMascota', primary_key=True)
    mascota         =models.CharField(max_length=50,blank=False,null=False)
    edad            =models.CharField(max_length=10)
    foto            =models.ImageField(upload_to="mascotas",null=False)


    def __str__(self):
        return str(self.mascota)
    
class Usuario(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20, blank=True)
    id_mascota       = models.ForeignKey('Mascota',on_delete=models.PROTECT, db_column='idMascota')  
    telefono         = models.CharField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100, blank=False, null=False)
    direccion        = models.CharField(max_length=50, blank=False, null=False)  
    activo           = models.IntegerField()

    def __str__(self):
        return str(self.rut)  
    
class Animal(models.Model):
    nombre          = models.CharField(max_length=30)
    imagen          = models.ImageField(upload_to="mascotas",null=False)
    edad            = models.CharField(max_length=10)

    def __str__(self):
        return str(self.nombre)
    