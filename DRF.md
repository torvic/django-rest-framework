# Django REST Framework

Django REST Framework es una poderosa y flexible herramienta para construir Web APIs.
Algunas razones por la que debes usar DRF:
* El **Web browsable API** es de gran ayuda para los desarrolladores.
* La politicas de autenticacion de DRF incluyen paquetes para **OAuth1** y **OAuth2**.
* Serialization soporta **ORM** y **NO-ORM** para las fuentes de dato.
* Puedes usar vistas basadas en funciones, sino necesitas las potenetes vistas basadas en clases.
* Extensiva documentacion, y gran soporte de la comunidad.
* Utilizado por empresas reconocidas internacionalmente, incluidas **Mozilla**, **Red Hat**, **Heroku**.

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

