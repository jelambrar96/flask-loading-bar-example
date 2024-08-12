# flask-loading-bar-example

Para implementar esta funcionalidad en una aplicación Flask, puedes seguir los siguientes pasos:

1. **Configurar el formulario en HTML** para cargar el archivo CSV.
2. **Procesar el archivo en el servidor** una vez subido.
3. **Mostrar un modal con una barra de progreso** mientras el archivo se procesa.
4. **Devolver el archivo procesado** al cliente una vez terminado.

A continuación te doy un ejemplo básico del código necesario para lograr esto:

### Estructura de archivos:
```
/your_project
    /templates
        index.html
    app.py
```

### 1. **HTML para el formulario y modal** (`templates/index.html`):

### 2. **Aplicación Flask** (`app.py`):

### 3. **Explicación del Flujo**:

- **Subida del archivo**: El usuario selecciona un archivo CSV y lo sube a través del formulario.
- **Modal de carga**: Al enviar el formulario, se muestra un modal con una barra de progreso que refleja el estado de la carga.
- **Procesamiento**: El archivo se guarda en el servidor, se procesa utilizando pandas, y el archivo procesado se guarda.
- **Descarga**: Una vez procesado, se redirige al usuario a una página donde puede descargar el archivo procesado.

### Notas:
- Este ejemplo es básico y puede necesitar ajustes según las necesidades específicas de tu proyecto, como mejorar el manejo de errores o personalizar la barra de progreso.
- En un entorno de producción, se recomienda configurar una cola de tareas para manejar el procesamiento de archivos más grandes de forma asíncrona.
