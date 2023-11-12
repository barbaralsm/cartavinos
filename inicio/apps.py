from django.apps import AppConfig


class InicioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inicio'
    
class appmodeloblog(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appmodeloblog'   
    
    
 
# class vinosconfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'vinos' 
    
# class regionesconfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'regiones' 
# class maridajesconfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'maridajes' 
# class tipsconfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'tips' 