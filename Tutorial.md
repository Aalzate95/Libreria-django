# Introducción a Django
[Tutorial](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Introduction)

### Comandos esenciales

Crear proyecto Django:
`django-admin startproject nombreproyecto`
Crear aplicación Django:
`python manage.py startapp nombreapp`

### Proyecto basico

creamos el proyecto
`django-admin startproject biblioteca`

Tendremos la siguiente estructura:
```
biblioteca/
    manage.py
    biblioteca/
        settings.py
        urls.py
        wsgi.py
```
La subcarpeta biblioteca es la sección principal, ya que contiene toda la configuración del proyecto.
- `settings.py` contiene todos los ajustes del proyecto. Aquí es donde se configuran las base de datos, locacion de ficheros y registro de aplicaciones.
- `urls.py` aquí definimos el mapa de urls, la estructura principal, pero se suele delegar responsabilidad de urls a cada aplicación.
- `wsgi.py` se encarga de la comunicación con el servidor web.
- `manage.py` es usado para crear las aplicaciones y empezar el desarrollo del servidor web

Dentro del archivo `settings.py` encontraremos dos secciones muy importantes.
- `SECRET_KEY`. Es la clave secreta que se usa como estrategia de seguridad. Cuando se ponga en producción debe cambiarse por un codigo diferente.
- `DEBUG` Por defecto está en `true` pero al tenerlo en produccion deberá estar en `false`. Esto debido a que la información de depuración al estar pública es una vulnerabildad importante de la que atacantes pueden sacar ventaja.


### Crear un administrador
Para poder iniciar sesion en el administrador de Django necesitamos crear un usuario tipo Administrador, para ello ejecutamos lo siguiente:
`python manage.py createsuperuser`
Una vez creado es necesario reiniciar el servidor de desarrollo.

#### Personalización del sitio de Administrador
[Administración](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/)




Links:
[Api-rest-framework](https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c)

actualmente voy por esta sección:
[aquí](https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Sessions)
me quedé en la sección de sesiones, revisar el tema de auth.