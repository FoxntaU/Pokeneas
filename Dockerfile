FROM python:3.8

# Create app directory
WORKDIR /usr/src/app

# Copy the Flask app source to the working directory
COPY . .

# Install Flask
RUN pip install -r requirements.txt

# Cambia la línea EXPOSE para exponer el puerto 8080
EXPOSE 8080

# Cambia el comando CMD para ejecutar Flask en el puerto 8080
CMD ["python", "app.py"]
