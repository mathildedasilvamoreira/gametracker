#!/bin/bash
# Script d’attente pour la base de données MySQL
# Boucle jusqu'à 30 tentatives avec 2s d'intervalle
# Utilise les variables d'environnement : DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

set -e

HOST=${DB_HOST:-"db"}
PORT=${DB_PORT:-"3306"}
USER=${DB_USER:-"root"}
PASSWORD=${DB_PASSWORD:-"root"}

MAX_TRIES=30
WAIT_SECONDS=2

echo "Attente de la base de données $HOST:$PORT ..."

for i in $(seq 1 $MAX_TRIES); do
    if mysql -h"$HOST" -P"$PORT" -u"$USER" -p"$PASSWORD" --skip-ssl\
    -e "SELECT 1;" >/dev/null 2>&1; then
        echo "Base de données prête !"
        exit 0
    fi
    echo "Tentative $i/$MAX_TRIES - Attente ..."
    sleep $WAIT_SECONDS
done

echo "Erreur : La base de données n’est pas disponible après $MAX_TRIES tentatives."
exit 1
