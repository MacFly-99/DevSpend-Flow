# On part d'une image Python officielle (légère)
FROM python:3.14-slim

# On définit le dossier de travail dans le conteneur
WORKDIR /app

# On copie d'abord le requirements.txt pour installer les dépendances
COPY requirements.txt .

# On installe les dépendances (sans le cache pip pour garder l'image légère)
RUN pip install --no-cache-dir -r requirements.txt

# On copie tout le reste du projet dans le conteneur
COPY . .

# On expose le port 8000
EXPOSE 8000

# La commande pour lancer l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]