# SandwichMania-HandTracker

Programa que utiliza una webcam para seguir los movimientos de la 
mano, para después mandar los datos al juego SandwichMania
desarrollado en [LANR](https://lanr.ifc.unam.mx/index.html).
---
## Dependencias

- python 3.11
- opencv-python=4.8.0.76
- mediapipe=0.10.3
- cvzone=1.5.6

Se utilizó pyinstaller=5.13.2 para distribuir el programa.

## Ejecutar

```commandline
python3 main.py
```

## Distribución con Pyinstaller

```commandline
 pyinstaller .\Sandwichmania-HandTracker.spec
```
Si tiene necesidad de generar de nuevo el archivo 
`Sandwichmania-HandTracker.spec`, es probable que haya
problemas con las dependencias de `mediapipe`. 

Este link resultó util para resolver el problema: 
[Issues compiling mediapipe with pyinstaller on macos](https://stackoverflow.com/questions/67887088/issues-compiling-mediapipe-with-pyinstaller-on-macos).

## Datos mandados

Los datos capturados se mandan por el puerto indicado en el
programa como en el siguiente ejemplo:

```
['Right', 720, 496, 632, 0, 550, 558, 28, 618, 516, 30, 675, 518, 22, 721, 534, 14, 650, 463, 21, 749, 482, 7, 768, 521, -1, 760, 549, -4, 662, 488, -2, 764, 528, -7, 766, 574, -8, 745, 599, -6, 671, 525, -26, 760, 569, -24, 753, 609, -17, 731, 628, -12, 675, 569, -48, 739, 604, -37, 731, 631, -23, 712, 644, -13]
```

Tiene la siguiente estructura
 - Un corchete que abre.
 - `'Right' | 'Left' | 'NoHand'` Dependiendo de la mano que esté capturando la webcam.
 - La altura de la captura de la webcam indicada en el programa. Default: 720.
 - 63 enteros con las coordenadas de los 21 puntos capturados por la webcam en orden y de 3 en 3.

Puede consultar los 21 puntos en [Hand landmarks detection guide](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker)