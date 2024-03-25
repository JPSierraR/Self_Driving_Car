import cv2
import numpy as np
def acciones(binary_segmentation,transformed_area):
    current_row = binary_segmentation[300, :]
    diff = np.where(np.diff(current_row) != 0)[0]
    size_diff = len(diff)

    if size_diff >= 4:
        dot1 = diff[0]
        dot2 = diff[1]
        dot3 = diff[2]
        dot4 = diff[3]
        cv2.circle(transformed_area, (dot1, 300), 5, (0, 0, 255), -1)
        cv2.circle(transformed_area, (dot2, 300), 5, (0, 0, 255), -1)
        cv2.circle(transformed_area, (dot3, 300), 5, (0, 0, 255), -1)
        cv2.circle(transformed_area, (dot4, 300), 5, (0, 0, 255), -1)


        avg_diff = (dot2 + dot3) // 2 if size_diff >= 5 else (dot1 + dot4) // 2
        cv2.line(transformed_area, (dot2, 300), (avg_diff, 300), (0, 255, 0), 5)

        cv2.line(transformed_area, (avg_diff, 300), (dot3, 300), (255, 0, 0), 5)
        cv2.circle(transformed_area, (avg_diff, 300), 7, (0, 0, 255), -1)
        distance = (320 - avg_diff)
    else:
        distance=0
    cv2.putText(transformed_area, f"Distancia: {distance:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2, cv2.LINE_AA)

    return distance