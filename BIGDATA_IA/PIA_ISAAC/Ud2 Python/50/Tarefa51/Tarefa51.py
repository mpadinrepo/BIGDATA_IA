import cv2
import face_recognition

# Cargar la imagen con OpenCV
image = cv2.imread('L:\REPOLOCAL\BIGDATA_IA\MIA_DAVID\EjerciciosModelosAgentes\quien-es-quien-prolog\tableroesquema.png')

# Convertir la imagen de BGR (OpenCV) a RGB (face_recognition)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Buscar las ubicaciones de las caras en la imagen
face_locations = face_recognition.face_locations(rgb_image)

# Inicializar una lista para almacenar los datos de cada cara detectada
face_data = []

# Iterar sobre las ubicaciones de las caras y extraer características faciales
for idx, (top, right, bottom, left) in enumerate(face_locations, 1):
    # Recortar la región de la cara de la imagen
    face_image = image[top:bottom, left:right]

    # Extraer características faciales de la cara
    face_encoding = face_recognition.face_encodings(rgb_image, [(top, right, bottom, left)])[0]

    # Guardar los datos de la cara en la lista
    face_data.append({
        'Número de cara': idx,
        'Ubicación': (top, right, bottom, left),
        'Características faciales': face_encoding
    })

    # Dibujar un rectángulo alrededor de la cara en la imagen original
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# Mostrar la imagen con las caras detectadas
cv2.imshow('Imagen con caras detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Mostrar la información de cada cara detectada
for data in face_data:
    print(f"Cara {data['Número de cara']}:")
    print(f"Ubicación: {data['Ubicación']}")
    print(f"Características faciales: {data['Características faciales']}\n")
