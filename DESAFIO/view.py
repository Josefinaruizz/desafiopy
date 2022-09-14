from django.shortcuts import render 
from django.http import HttpResponse

from AppDesafio.models import Familia

def familia(self):

    familia1 = Familia(nombre = "Josefina", edad = 23 , fecha_nac = 23/12/1998)
    familia2 = Familia(nombre = "Jorgelina", edad=32, fecha_nac = 12/12/1990)
    familia3 = Familia(nombre= "Javier", edad= 27, fecha_nac = 24/11/1994)
    
  
    diccionario = {
        "nombre1" :familia1.nombre, "edad1": familia1.edad, "cumpleanios1": familia1.fecha_nac,
        "nombre2" :familia2.nombre, "edad2":familia2.edad, "cumpleanios2": familia2.fecha_nac,
        "nombre3" :familia3.nombre, "edad3": familia3.edad, "cumpleanios3": familia3.fecha_nac,  }

    mensaje = "Buenos días familia"
    

    return HttpResponse(mensaje)