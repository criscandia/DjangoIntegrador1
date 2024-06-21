# Proyecto Integrador de Django: Tienda de Remeras

Este proyecto es una aplicación web desarrollada con Django, diseñada para gestionar una tienda de remeras. Permite a los usuarios agregar nuevas remeras, listar todas las remeras disponibles, y navegar por la tienda.

## Características

- **Agregar Nuevas Remeras:** Los usuarios pueden añadir nuevas remeras a la tienda especificando detalles como el nombre, tamaño, color, y precio.
- **Listar Remeras:** La aplicación proporciona una vista donde los usuarios pueden ver todas las remeras disponibles en la tienda.
- **Interfaz de Usuario Amigable:** Utiliza Materialize CSS para una interfaz de usuario moderna y responsiva.

## Tecnologías Utilizadas

- **Backend:** Django
- **Frontend:** HTML, CSS (Materialize)
- **Base de Datos:** SQLite (por defecto en Django)

## Requisitos

Para ejecutar este proyecto, necesitarás Python 3.6 o superior y pip instalados en tu sistema.

## Instalación

1. Clona este repositorio en tu máquina local usando:
git clone https://github.com/criscandia/DjangoIntegrador1.git

2. Navega al directorio del proyecto:
cd DjangoIntegrador1
4. 3. Crea un entorno virtual:
python3 -m venv venv

4. Activa el entorno virtual:
- En Windows:
  ```
  .\venv\Scripts\activate
  ```
- En macOS y Linux:
  ```
  source venv/bin/activate
  ```

5. Instala las dependencias del proyecto:
pip install -r requirements.txt


6. Realiza las migraciones de la base de datos:
python manage.py migrate

7. Inicia el servidor de desarrollo:
python manage.py runserver


8. Abre un navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.

## Contribuir

Las contribuciones son bienvenidas. Por favor, envía un pull request o abre un issue para sugerir cambios o mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
