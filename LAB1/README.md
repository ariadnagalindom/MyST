# MyST
 Microestructuras y Sistemas de Traiding 

 ESTRUCTURA DEL PROYECTO: 

1. files: una carpeta donde se encuentran los archivos a utilizar 
2. venv: carpeta donde se encuentra el ambiente virtual del proyecto 
3.  requirements.txt: archivo .txt donde se enlistan los requerimientos de librerias que necesita el ambiente (pip freeze > requirements.
txt)
4. main.py: script donde se mandan llamar funciones y se presentan codigos para el acomodo de datos, aquí se mandan llamar functions.py
 y visualizations.py, haciendo uso de lo almacenado en data.py
5. data.py: script donde se guardan datos de utilidad en diferentes scripts 
6. functions.py: script donde declaramos funciones de medianas a complejas que se usaran en main.py 
7. visualizations.py: script donde se dejan todas las funciones desarrolladas para visualizar datos como tablas, gráficas, textos impresos, etc. 
8. notebook.ipynb: cuaderno de jupyter donde se explica todo el proyecto, va de la mano con main.py con la única diferencia de que en el notebook se explica detalladamente en entradas de texto. A su vez, debe guardarse como .html 
9. README.md: archivo introductorio del proyecto
10. .gitignore: tipo .txt donde se almacenan archivos a ignorar en GitHub

MÁS SOBRE EL PROYECTO: 
Dentro de la materia de Microestructuras y Sistemas de Traiding para Otoño 2021 se crea simula una inversión de un millón de pesos 
con dos estrategias diferentes; activa y pasiva. 

SECUENCIA PARA CORRER SCRIPTS:
functions>data>main
al final correr el notebook 

WARNING:
Prestar especial atención en correr las celdas según el sistema donde se este usando, hay líneas para correr iOs y Windows, sin 
embargo, si se corre la equivocada generará error ya que no podrá descargar correctamente los datos. 


ACTIVAR AMBIENTE VIRTUAL:
colocar la siguiente linea en una terminal Promt segun el sistema utilizado
Windows:
venv\Scripts\activate 
iOS:
venv/Scripts/activate