# Proyecto de Automatización de Pruebas para MercadoLibre
Este proyecto realiza pruebas automatizadas en el sitio de MercadoLibre usando Selenium y Pytest, con generación de reportes visuales mediante Allure.

## Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de contar con las siguientes herramientas:
* Python 3.12 o superior (el proyecto usa Python 3.12.7)
* Java (necesario para Allure) v. 23.0.1
* Installar Allure https://allurereport.org/docs/install/ v. 2.32.0
* Navegador Edge y el correspondiente controlador de Edge (para Selenium)


## Instalación
1.- Clona este repositorio:

```bash
git clone https://github.com/marioquirogabernal/test_automatizado.git
cd test_automatizado
```

2.- Instala el entorno virtual y las dependencias necesarias:
````bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
````

3.- Asegúrate de que Allure esté correctamente instalado en tu sistema.

## Ejecución de las Pruebas
1.- Ejecuta las pruebas y guarda los resultados en el directorio ./resultados:
```bash
pytest --alluredir=./resultados
```
2.- Genera el reporte Allure a partir de los resultados:
````bash
allure generate ./resultados -o ./reporte --clean
````
3.- Abre el reporte en el navegador para ver los detalles y capturas:
````bash    
allure open ./reporte
````
Created with love by: Mario Eduardo Quiroga Bernal
