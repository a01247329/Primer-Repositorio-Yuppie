# Parte 5: Detección de bordes con Canny

import cv2
import numpy as np

cam_port = 0
cam = cv2.VideoCapture(cam_port)

while True:
    result, frame = cam.read()
    if result:
        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar Canny
        edges = cv2.Canny(gray, 100, 200)
        # Mostrar el resultado de Canny
        cv2.imshow("Canny Edges - Press q to quit", edges)
        # Salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("No image detected")
        break

cam.release()
cv2.destroyAllWindows()