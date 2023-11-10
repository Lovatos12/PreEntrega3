from django.db import models

# Create your models here.
class CrearForo(models.Model):
    temas_foros=(("Comida","Comida"), 
                 ("Salud","Salud"),
                 ("Ejercio","Ejercicio"),
                 ("Otro","Otro")
    )
    
    nombre=models.CharField(max_length=64,blank=False,verbose_name="Nombre del Foro")
    tema=models.CharField(max_length=7,choices=temas_foros)
    contenido=models.CharField(max_length=1500,blank=False,verbose_name="Contenido del Foro")

    def __str__(self):
        return f"{self.tema} ,{self.nombre}"


class Forista(models.Model):
    sexos=(("M","Masculino"),
           ("F","Femenino"),
           ("D","Default")
    )
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    sexo=models.CharField(max_length=1,choices=sexos,default="D")
    email = models.EmailField(blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)


class RespuestaForo(models.Model):
    respuesta=models.CharField(max_length=1500,blank=False,verbose_name="Contenido del Foro")