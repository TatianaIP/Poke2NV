
from django.http import HttpResponse #creando una vista en python
import datetime                      #importar el modulo de Datetime
from django.template import Template,Context
import requests
import json



def saludo (request): # primera vista recibe un request como 
          
    listaPokemones=["spearow","fearow","ekans","arbok","pikachu","raichu",
                    "sandshrew", "sandslash", "nidorina"
                   ]

    doc_Externo= open ("C:/Users/iptat/Desktop/Django/Proyecto Django/1. Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_Externo.read()) #objeto de tipo template
    doc_Externo.close() #cerrar el documento
    ctx=Context({"pokemones":listaPokemones}) #crear el contexto, este contexto permite recibir diccionarios
    documento=plt.render(ctx) #
    return HttpResponse(documento)

def despedida(request): #segunda vista 

    return HttpResponse("Hasta luego queridos alumnos")

def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento = """<html>
    <body>
    <h2>Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,agno,edad):
    
    
    periodo=agno-2021
    edadFutura= edad+periodo
    documento="<html><body><h2> En el año %s tendrás %s años" %(agno,edadFutura)
    return HttpResponse(documento)

def pokemon(request,name):
    
    url='http://pokeapi.co/api/v2/pokemon/%s' %(name)
    
    
    response = requests.get(url)
    response_json = response.json() # esta variable es un diccionario
    abilities=[]
    skills =  response_json['abilities'] #se toman los valores de la clave abilities

    for ability in skills:
        abilities.append(ability['ability']) 

        print(abilities)
        
    doc_Externo= open ("C:/Users/iptat/Desktop/Django/Proyecto Django/1. Proyecto1/Proyecto1/plantillas/miplantilla.html")
    plt=Template(doc_Externo.read()) #objeto de tipo template
    doc_Externo.close() #cerrar el documento
    ctx=Context({"list":abilities}) #crear el contexto, este contexto permite recibir diccionarios
    documento=plt.render(ctx) 

    return HttpResponse(documento)
     
         
    


 