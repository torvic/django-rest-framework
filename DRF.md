# Django REST Framework

Django REST Framework es una poderosa y flexible herramienta para construir Web APIs.
Algunas razones por la que debes usar DRF:
* El *[Web browsable API][1]* es de gran ayuda para los desarrolladores.
* La politicas de autenticacion de DRF incluyen paquetes para **OAuth1** y **OAuth2**.
* Serialization soporta **ORM** y **NO-ORM** para las fuentes de dato.
* Puedes usar vistas basadas en funciones, sino necesitas las potenetes vistas basadas en clases.
* Extensiva documentacion, y gran soporte de la comunidad.
* Utilizado por empresas reconocidas internacionalmente, incluidas **Mozilla**, **Red Hat**, **Heroku**.

[1]: https://restframework.herokuapp.com/
## Requerimientos

DRF requires the following:
* Python (3.5 - 3.9).
* Django (2.2, 3.0, 3.1).

## Instalacion

Instalar usando `pip`.
```
pip install djangorestframework
```
Añadir `'rest_framework'` a `INSTALLED_APPS` en `setting.py`.
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
## Apuntes

### Django MVT (modelo, vista, template)
```
|models.py| <--> |forms.py| <--> |views.py| <--> |urls.py| <-->
                               | 
                               |<--> render(template) <-->
```
### Django REST Framework
```
|models.py| <--> |serializer.py| <--> |views.py| <--> |urls.py|
                                    |
                                    |<--> Response(json) <-->
```
## Inicio rapido
```
$ django-admin 
    |--> startproject <name-project> 
    |--> startapp <name-app> --> settings.py

$ py manage.py
    |--> makemigrations
    |--> migrate
    |--> runserver
    |--> createsuperuser

serializer.py
-------------
    *import*
    |--> rest_framework
        |--> serializers.py
    |--> django.contrib.auth
        |--> models.py
            |--> User
    
    *class*
    serializers.py
        |-->.Serializer
        |-->.HyperLinkedModelSerializer
        |-->.ModelSerializer
            |<-- UserSerializer <--> User

views.py
--------
    *import*
    |--> rest_framework
        |-->response.py 
            |--> Response
        |-->decorators.py
            |--> api_view
    |--> django.contrib.auth
        |--> models.py
            |--> User
    |--> <app>
        |--> serializers.py
            |--> UserSerializer
    
    *function*
    user_api_view(request) 
        |--> queryset <--> User.objects.<...>    
        |--> queryset_serializer <--> UserSerializer() 
        |==> Response()

    

in_our_apps
    |--> serializer.py

urls.py
-------
    |--> urls.py|app <--> urls.py|project
        |--> django
            |--> urls
                |--> path
                |--> include

```




































