FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias necesarias para la detección de hardware
RUN apt-get update && apt-get install -y \
    lshw \
    procps \
    hwinfo \
    && rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requisitos e instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app/ .

# Exponer el puerto que utilizará nuestra API
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]