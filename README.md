### Pasos para instalación
1. Instalar Python 3.10 
2. Instalar Django
 $ python3 -m pip install Django==4.1.3
3. Crear nuevo proyecto
- ubicarnos donde queremos crear el nuevo proyecto
- desde la terminar ejecutar
 $ django-admin startproject holamundo

### Migración

Migración de los datos se deben hacer cada vez que se modifique la estructura de los datos

1. Ubicarnos en la carpeta del proyecto
- ejecutar 
 $ python3 manage.py migrate

2. Ejecutar el servidor de pruebas de Django
$ python3 manage.py runserver

### Modularización

1. Dentro de la carpeta principal del proyecto, ejecutar
- $ python3 manage.py startapp comentarios
2. En el archivo settings.py se debe agregar la aplicación que se va a utilizar, se añade con el nombre de la aplicación o carpeta

INSTALLED_APPS = [
    'django.contrib.admin',
    'comentarios',
]

3. Verificar si la aplicación queda correctamente instalada ejecutar
$ python3 manage.py check comentarios

### Modelos de datos
$ python3 manage.py makemigrations
- hacer la migración
$ python3 manage.py migrate

### Códigos de operadores en búsquedas
- __lte: menor o igual (lower than equals)
- __gte: mayor o igual (greater than equals)
- __lt: menor que (lower than)
- __gt: mayor que (greater than)
- __contains: contiene
- __exact: exacto