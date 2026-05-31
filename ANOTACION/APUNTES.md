# ANOTACIÓN

Para la anotación de segmentación se seleccionaron aleatoriamente 250 imágenes de 13 sujetos, de diferentes edades, aberraciones y correcciones (gafas o lentillas) usando el script [seleccion_imagenes_aleatorias.py](./SCRIPTS/seleccion_imagenes_aleatorias.py).

Las imágenes fueron anotadas en CVAT, instalado en el servidor photon.inf.um.es con Docker. Se configuró el uso de SAM como apoyo a la segmentación de pupilas que no se podían ajustar a una elipse y se habilitó la infraestructura de autoanotación con Nuclio, con el objetivo de facilitar la generación y revisión de máscaras de la pupila.

Inicialmente se anotó un subconjunto de imágenes para un entrenamiento inicial de una red U-Net.