# Folosim imaginea oficială de Python
FROM python:3.11-slim

# Setăm folderul de lucru în container
WORKDIR /app

# Copiem fișierul de dependențe
COPY requirements.txt .

# Instalăm dependențele
RUN pip install --no-cache-dir -r requirements.txt

# Copiem restul codului
COPY . .

# Pornim serverul
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]