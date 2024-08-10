# Proyecto Urban Grocers 

--- 
## Erick Torres Cohort 12 - Sprint 07

Este proyecto automatiza las pruebas de la API de Urban Grocers, específicamente para la creación de kits de productos. Utiliza `pytest` para realizar pruebas de diferentes escenarios de entrada.

### <u> Estructura del Proyecto</u>

El proyecto consta de los siguientes archivos:

### `configuration.py`

Define las URLs base y las rutas para los endpoints de la API.

### `sender_stand_request.py`
Contiene funciones para interactuar con la API, incluyendo la obtención de un token de usuario y la creación de un kit de productos.


### `data.py`
Define los datos de prueba, incluyendo encabezados, el cuerpo de solicitud para la creación de usuarios y diferentes cuerpos de solicitud para la creación de kits.

### `create_kit_name_kit_test.py`

Contiene las pruebas automatizadas utilizando pytest. Incluye pruebas positivas y negativas para validar la creación de kits con diferentes valores para el campo name.


