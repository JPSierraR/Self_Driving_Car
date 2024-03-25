#ESTE MODULO HACE LA TAREA DE CENTRAR UNA AREA DE INTERER, DISMINUIR EL RUIDO DE LAS IMAGENES Y RETORNAR LA IMAGEN SEGMENTADA
import cv2
import numpy as np

def filtros(frame, kernel):
    area_inside_trapezoid = np.zeros_like(frame)
    points = np.array([[130, 200], [560, 200], [620, 460], [70, 460]], np.int32)
    mask = np.zeros_like(frame[:, :, 0])
    
    cv2.fillPoly(mask, [points], color=255)
    area_inside_trapezoid = cv2.bitwise_and(frame, frame, mask=mask)
    dilated_area = cv2.dilate(area_inside_trapezoid, kernel, iterations=1)
    x, y, w, h = cv2.boundingRect(points)
    cropped_dilated_area = dilated_area[y:y+h, x:x+w]

    new_width = 640
    new_height = 480

    resized_dilated_area = cv2.resize(cropped_dilated_area, (new_width, new_height))

    pts1 = np.float32([[0, 0], [new_width, 0], [0, new_height], [new_width, new_height]])
    pts2 = np.float32([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])

    matrix = cv2.getPerspectiveTransform(pts2, pts1)

    transformed_area = cv2.warpPerspective(resized_dilated_area, matrix, (new_width, new_height))
    gray_transformed_area = cv2.cvtColor(transformed_area, cv2.COLOR_BGR2GRAY)
    _, binary_segmentation = cv2.threshold(gray_transformed_area, 127, 255, cv2.THRESH_BINARY)

    return binary_segmentation, transformed_area

