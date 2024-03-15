import cv2
import pytest
from Tarefa62 import detect_faces

# Ruta de la imagen
image_path = 'imaxe.jpg'  # Reemplaza 'imagen.jpg' con la ruta de tu imagen

def test_detect_faces():
    # Llamada a la función para detectar los rostros
    result_image = detect_faces(image_path)
    # Comprueba si la imagen resultante no es None
    assert result_image is not None
