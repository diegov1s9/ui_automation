# Proyecto de Automatización UI con Selenium

Proyecto para automatizar una serie de pruebas en la web [OpenCart](http://opencart.abstracta.us/) utilizando Selenium. El flujo de trabajo automatizado incluye la búsqueda de un producto, la adición al carrito de compras, y la validación de su presencia y eliminación en el carrito.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `pages/`: Contiene las clases que representan las diferentes páginas del sitio web.
  - `HomePage.py`
  - `ProductPage.py`
  - `ShoppingCartPage.py`
- `screenshots/`: Carpeta donde se almacenan las capturas de pantalla tomadas durante las pruebas.
- `conftest.py`: Configuración de pytest y funciones auxiliares.
- `data.py`: Contiene datos utilizados en las pruebas.
- `selector.py`: Contiene los selectores utilizados para interactuar con los elementos de la página.
- `TestYourStore.py`: Contiene la clase principal de pruebas que ejecuta el flujo de trabajo automatizado.

## Requisitos

- Python 3.12
- Selenium
- pytest
- Chromium y Chromedriver

## Configuración del Entorno de Desarrollo

El proyecto utiliza un contenedor de desarrollo configurado con DevContainers bajo ARM64. Para configurar el entorno, asegúrate de tener Docker instalado y sigue estos pasos:

1. Clona el repositorio.
2. Abre el proyecto en Visual Studio Code.
3. Abre la carpeta `.devcontainer` y asegúrate de que el archivo `devcontainer.json` esté configurado correctamente.
4. Abre el contenedor de desarrollo.

## Instalación de Dependencias

Las dependencias necesarias se instalan automáticamente al crear el contenedor de desarrollo. Si necesitas instalarlas manualmente, ejecuta:

```sh
pip install selenium pytest
sudo apt-get update
sudo apt-get install -y chromium chromium-driver
```

## Ejecución de Pruebas
Para ejecutar las pruebas, utiliza el siguiente comando:

```sh
python -m pytest TestYourStore.py 
```
