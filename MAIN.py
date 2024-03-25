import cv2
import numpy as np
from FILTROS import filtros
from LOGICA import acciones
# Inicializar la captura de video (cámara)
cap = cv2.VideoCapture(0)
# Establecer la resolución de video (ancho y alto)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
kernel = np.ones((5, 5), np.uint8)
V_max=50
# Bucle principal de procesamiento de video
c=0
while True:
    # Leer un frame (captura de video)
    ret, frame = cap.read()

    #---------------------------------------------------
    binary_segmentation, transformed_area = filtros(frame, kernel)
    #---------------------------------------------------
    distance,v1,v2 = acciones(binary_segmentation,transformed_area,V_max)
    #---------------------------------------------------
    #funcion 3
    #---------------------------------------------------
    #funcion 4
    #---------------------------------------------------
    #print(distance)
    # Mostrar el frame en una ventana
    cv2.circle(transformed_area, (320, 300), 5, (0, 255, 255), -1)  # Punto amarillo fijo en (320, 300)
    cv2.imshow('frame', transformed_area)

    while cv2.waitKey(1) & 0xFF == ord('s'):
        print("stop_motors")
    
    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("stop_motors")
        print("PROCESO TERMINADO!!!!!!")
        break

# Liberar los recursos de la cámara
cap.release()
cv2.destroyAllWindows()
