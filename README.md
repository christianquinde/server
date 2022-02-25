# server
Servidor de contactos para la herramienta de videoconferencia.

Esta herramienta se diseñó mediante scripts de Linux para cumplir con las distintas funcionalidades y los experimentos se efectuaron en ordenadores con sistema operativo Ubuntu 20.04. Para efectuar los diferentes cálculos también se implementaron scripts en Python 3.7. 

Esta herramienta se instala en un equipo dentro de la misma red. Es la primera herramienta en entrar en funcionamiento.

Actúa como base de datos. Cada usuario que ingrese a la herramienta de videoconferencia envía su nombre, apellido e IP.

La base de datos agrega los datos de cada usuario. 

Si un usuario que está registrado cambia su nombre. El servidor busca su IP y actualiza el nombre y apellido ingresado.

Al ingresar a la interfaz principal de la herramienta de videoconferencia, la base de datos envía un archivo txt con todos los contactos.

La interfaz de videoconferencia se encuentra disponible en: https://github.com/christianquinde/App-videoconferencia
