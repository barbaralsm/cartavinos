from django.shortcuts import render

from inicio.models import vinos, regiones, maridajes, tips

def inicio (request):
  
 return render (request, 'inicio/inicio.html', {})


def vinos (request, marca, bodega, cepa, cosecha, precio):
  vinos= vinos(marca='nicasia', bodega='catena zapata', cepa='malbec', cosecha=2022, precio=4200)
  vinos.save()
  return render (request,'vinos.html', {'vinos':vinos})

def regiones(request, nombre, provincias, clima, suelo):
    regiones= regiones(nombre='Lujan de Cuyo', provincias='Mendoza', clima='Calido y templado',suelo= 'salino, eólico arenoso, aluvial y misceláneo', cepas= 'Cabernet Sauvignon, Syrah, Chardonnay, Sauvignon Blanc, Pinot Gris y Torrontés', bodegas='Catena zapata, norton, luigi bosca, septima, Achával-Ferrer')
    regiones.save()
    return render (request,'vinos.html', {'regiones':regiones})

def maridajes(request, cepa, maridaje, marcasrecomendadas):
   maridajes= maridajes(cepa='malbec', maridaje='grillados, pastas con tuco, cordero o chivo a la parrilla, guisados ', marcasrecomendadas= 'Huentala Calizo Carmin Block 3 2020, distinguido como Mejor Malbec del Mundo 2023')
   maridajes.save()
   return render (request,'vinos.html', {'maridajes':maridajes})

def tips (request, etiqueta, maridaje):
  tips= tips(etiqueta='o ficha tecnica, leer todas las caracteristicas', maridaje='tener en cuenta que vamos a acompañar', reseñas='busca en nuestro blog reseñas sobre relacion precio/calidad')
  tips.save()
  return render (request,'vinos.html', {'tips':tips})

def crear_paleta (request):
  return render(request, 'inicio/crear_paleta.html', {})



  # template= loader.get_template('creacion_de_vinos.html')
  # template_renderizado= template.render({'vinos':vinos})
  # return HttpResponse(template_renderizado)

  # template= loader.get_template('creacion_de_regiones.html')
  # template_renderizado= template.render({'regiones':regiones})
  # return HttpResponse(template_renderizado)

  # template= loader.get_template('creacion_de_maridajes.html')
  # template_renderizado= template.render({'maridajes':maridajes})
  # return HttpResponse(template_renderizado)
 
 
  # template= loader.get_template('creacion_de_tips.html')
  # template_renderizado= template.render({'tips':tips})
  # return HttpResponse(template_renderizado)
