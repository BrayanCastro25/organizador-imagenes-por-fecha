# ORGANIZADOR DE IMÁGENES Y VIDEOS POR AÑO Y MES

Este programa consiste en tomar todas una carpeta y cada imagen va siendo agregada a la carpeta según corresponda según el año y el mes. Primero se encontrarán las carpetas por año y segundo por mes donde se organizan en forma ascendente es decir el primer mes corresponde a la carpeta  `1. Enero` y así sucesivamente.



## Consideraciones

* Resulta que las imágenes compartidas por Whatsapp al ser comprimidas eliminan la información de metadata como la primordial para este programa el `DateTimeOriginal`. Que es la fecha cuando se tomo la foto. Lo recomendado para estos casos es que se cree una carpeta especificamente llamada WhatsApp (No es necesario) y que la fecha utilizada para estos archivos sea la que se genera en el nombre por ejemplo `IMG-20200617-WA0010 (2).jpg` donde la fecha es `20200617`.
* Otro caso en particular son las capturas de pantalla `Screenshot_20210926-141402-031.png` donde la fecha es  `20210926`.



## Posibles mejoras

* Se puede simplificar el proceso de búsqueda de algunas imágenes, ya que en ocasiones estas no contienen letras que permitan identificar su clasificación como el siguiente ejemplo: `IMG_20220713_125532_708.jpg`, a pesar que no tiene información metadata ni `Screenshot` que identifica que es una captura de pantalla, como tampoco `WA` que describe que se trata de una imagen de WhatsApp.