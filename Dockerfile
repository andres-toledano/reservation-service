# Usar la imagen oficial de Python como base
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY . /app

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt


# Exponer el puerto en el que Flask estará escuchando
EXPOSE 5000

# Definir la variable de entorno para la configuración de Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV DB_URL=mysql+mysqlconnector://cumn:grupox2%4025@cumn-database.mysql.database.azure.com:3306/classroom_management

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
