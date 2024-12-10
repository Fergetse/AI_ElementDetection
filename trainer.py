import cv2 as cv
import numpy as np
import os

# Ruta al dataset de imágenes positivas
feliz = "C:/Users/modim/Desktop/emotions/feliz"
triste = "C:/Users/modim/Desktop/emotions/triste"
enojado = "C:/Users/modim/Desktop/emotions/enojado"
neutral = "C:/Users/modim/Desktop/emotions/neutral"
sorprendido = "C:/Users/modim/Desktop/emotions/sorprendido"

def load_images_from_folder(folder, label):
    images = []
    labels = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename).replace('\\', '/')
        grayImage = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        if grayImage is not None:
            images.append(grayImage)
            labels.append(label)
        else:
            print(f"Error al leer la imagen: {img_path}")
    return images, labels




# Cargar imágenes 
feliz_images, feliz_labels = load_images_from_folder(feliz, 0)
triste_images, triste_labels = load_images_from_folder(triste, 1)
enojado_images, enojado_labels = load_images_from_folder(enojado, 2)
neutral_images, neutral_labels = load_images_from_folder(neutral, 3)
sorprendido_images, sorprendido_labels = load_images_from_folder(sorprendido, 4)

# Combinar las imágenes y etiquetas de ambas clases
import cv2 as cv
import numpy as np
import os

# Ruta al dataset de imágenes positivas
feliz = "C:/Users/modim/Desktop/emotions/feliz"
triste = "C:/Users/modim/Desktop/emotions/triste"
enojado = "C:/Users/modim/Desktop/emotions/enojado"
neutral = "C:/Users/modim/Desktop/emotions/neutral"
sorprendido = "C:/Users/modim/Desktop/emotions/sorprendido"

def load_images_from_folder(folder, label):
    images = []
    labels = []
    index = 0
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename).replace('\\', '/')
        grayImage = cv.imread(img_path, cv.IMREAD_GRAYSCALE)
        if grayImage is not None:
            images.append(grayImage)
            labels.append(label)
            index+=1
            if index == 1000:
                break
        else:
            print(f"Error al leer la imagen: {img_path}")
    return images, labels




# Cargar imágenes 
feliz_images, feliz_labels = load_images_from_folder(feliz, 0)
triste_images, triste_labels = load_images_from_folder(triste, 1)
enojado_images, enojado_labels = load_images_from_folder(enojado, 2)
neutral_images, neutral_labels = load_images_from_folder(neutral, 3)
sorprendido_images, sorprendido_labels = load_images_from_folder(sorprendido, 4)

# Combinar las imágenes y etiquetas de ambas clases
facesData = feliz_images + triste_images + enojado_images + neutral_images + sorprendido_images
labels = feliz_labels + triste_labels + enojado_labels + neutral_labels+ sorprendido_labels



#facesData = feliz_images + enojado_images + sorprendido_images
#labels = feliz_labels + enojado_labels + sorprendido_labels


print(f"Total de ejemplos positivos: {len(facesData)}")
print(f"Total de ejemplos negativos: {len(labels)}")

if facesData:
    # Crear aaaaaaaa
    faceRecognizer = cv.face.FisherFaceRecognizer_create()
    faceRecognizer.train(facesData, np.array(labels))

    # Ruta donde guardo al xml
    save_path = 'C:/Users/modim/Desktop/emociones_model_GOD1.xml'
    # Guardado
    faceRecognizer.write(save_path)

    print(f"Modelo guardado como '{save_path}' en el directorio: {os.getcwd()}")
else:
    print("No se encontraron imágenes válidas para entrenar el modelo.")
