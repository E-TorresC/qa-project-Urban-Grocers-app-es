
Erick Torres Cohort 12 - Sprint 07
# Proyecto de Pruebas de API - Gestión de Kits

> Este proyecto está diseñado para probar la funcionalidad de una API que gestiona la creación de kits. Se han implementado pruebas utilizando `pytest` para garantizar la integridad y correcto funcionamiento de la API.

## Contenido

- [Requisitos Previos](#requisitos-previos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Ejecución de las Pruebas](#ejecución-de-las-pruebas)
- [Comandos Útiles](#comandos-útiles)
- [Comandos para ejecutar pruebas](#comandos-para-ejecutar-pruebas)

## Requisitos Previos

Antes de empezar, asegúrate de tener instalados los siguientes requisitos:

- [Python 3.x](https://www.python.org/downloads/)
- [PyCharm](https://www.jetbrains.com/pycharm/download/) (o cualquier IDE de tu preferencia)
- `pip` para la instalación de paquetes.

## Configuración del Entorno

### 1. Clona el repositorio

Clona el repositorio en tu máquina local usando el siguiente comando:


git clone <URL_de_tu_repositorio>
cd <nombre_de_tu_repositorio>

### 2. Configura PyCharm

> - Crear un entorno virtual: 
> 
> Abre PyCharm y selecciona File -> New Project.
Selecciona Python como el tipo de proyecto y asegúrate de que la opción New environment using: Virtualenv esté marcada.
Configura el directorio del entorno virtual y elige la versión de Python instalada en tu sistema.
>- Instala las dependencias:
>
>Ve a File -> Settings -> Project: <nombre_del_proyecto> -> Python Interpreter.
Asegúrate de que el intérprete apunte a tu entorno virtual.
Instala los paquetes requeridos usando el siguiente comando en la terminal:
bash
Copiar código
pip install requests pytest

### 3. Configuración de la API
>Modifica las variables en el archivo configuration.py para apuntar a los servicios API que estás utilizando.
>
>python
Copiar código
URL_SERVICE = "https://tu-api-url.com/"
>
>CREATE_USER_PATH = "/api/v1/users/"
>
>KITS_PATH = "/api/v1/kits"

### 4. Estructura del Proyecto
La estructura básica del proyecto es la siguiente:

>- configuration.py: Contiene las configuraciones y rutas de la API.
> 
>- create_kit_name_kit_test.py: Archivo que contiene las pruebas para la API.
> 
>- data.py: Contiene los datos de prueba.
> 
>- sender_stand_request.py: Implementa las solicitudes a la API.

### 5. Comandos Utiles
1. Instalar pytest:(Commando de terminal) pip install pytest
2. Instalar request:(Commando de Pycharm) Python Packages/ Buscar 'requests'/ Install

### 6. Comandos para ejecutar pruebas 
- Ejecutar todas las pruebas en el archivo create_kit_name_kit_test.py:
> pytest create_kit_name_kit_test.py
- Ejecutar una prueba específica dentro de create_kit_name_kit_test.py:
> pytest create_kit_name_kit_test.py::test_create_kit_name_0_chars
- Ejecutar todas las pruebas en el proyecto (si hay múltiples archivos de pruebas):
> pytest
- Ejecutar las pruebas con detalles adicionales (verbose mode):
> pytest -v create_kit_name_kit_test.py
