# Použitie oficiálneho Python obrazu ako základ
FROM python:3.10

# Nastavenie pracovného adresára v kontajneri
WORKDIR /app

# Kopírovanie súborov requirements.txt do kontajnera a inštalácia závislostí
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Kopírovanie zvyšku aplikácie do kontajnera
COPY . /app/

# Nastavenie premenných prostredia
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Spustenie Django servera
CMD ["python", "manage.py", "runserver", "loclahost:8000"]
