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
