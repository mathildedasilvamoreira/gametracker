#!/bin/bash
set -e

# --- Attente de la base de données ---
echo "Attente de la base de données..."
./scripts/wait-for-db.sh

# --- Initialisation de la base avec le script SQL ---
echo "Initialisation de la base de données..."
mysql  --skip-ssl -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" < scripts/init-db.sql

# --- Vérification des tables ---
echo "Tables présentes dans la base :"
mysql  --skip-ssl -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" -e "SHOW TABLES;"

# --- Test de la connexion Python ---
echo "Test de la connexion Python..."
python -c "from src.database import get_connection; conn = get_connection(); print('Connexion réussie' if conn.is_connected() else '❌ Connexion échouée')"

echo "Base de données prête et connexion Python OK !"
