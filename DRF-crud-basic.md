# CRUD Basico en DRF
Comandos basicos:
```
$ django-admin 
    |--> startproject <name-project> 
    |--> startapp <name-app> --> settings.py

$ py manage.py
    |--> makemigrations
    |--> migrate
    |--> createsuperuser
    |--> runserver
```
models.py --> serializers.py --> views.py --> urls.py

Crear `serializers.py` y `urls.py` en nuestra aplicacion.

En `models.py`:

En `serializers.py`:
```
import
======
    |--> rest_framework 
        |--> serializers.py
    |--> django.contrib.auth
        |--> models.py
            |--> User

clases
======
    serializers.py
        |--> Serializer
        |--> ModelSerializer

    ModelSerializer
        |<-- UserSerializer <--> User
```
En `views.py`:
```
import
======
    |--> rest_framework
        |--> response.py
            |--> Response
        |--> decorators.py
            |--> api_view
    |--> django.contrib.auth
        |--> models.py
            |--> User
    |--> <app>
        |--> serializers.py
            |--> UserSerializer

funciones
=========
    |--> user_api_view --> GET, POST
    |--> user_detail_api_view --> GET, PUT, DELETE    

```
En `urls.py`:
```
import
======
    |--> django.urls
        |--> path
        |--> include
```








