# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requisitos y el código fuente a la imagen
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación estará escuchando
EXPOSE 8000

# Define el comando que se ejecutará al iniciar el contenedor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
