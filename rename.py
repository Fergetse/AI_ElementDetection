import os

# Definir la carpeta con los documentos
folder = "C:/Users/modim/Desktop/n"

# Listar los documentos en la carpeta
documents = os.listdir(folder)

# Iterar sobre los documentos y renombrarlos
for index, doc in enumerate(documents):
    # Obtener la extensión del archivo
    file_extension = os.path.splitext(doc)[1]
    
    # Crear el nuevo nombre del archivo
    new_name = f"doc_{index}{file_extension}"
    
    # Obtener la ruta completa del archivo actual y del nuevo archivo
    current_path = os.path.join(folder, doc)
    new_path = os.path.join(folder, new_name)
    
    # Renombrar el archivo
    os.rename(current_path, new_path)

print("Documentos renombrados exitosamente.")
