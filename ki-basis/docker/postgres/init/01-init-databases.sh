#!/usr/bin/env bash
set -e

# Create roles and databases for applications
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Firefly DB & Role
    CREATE USER ${FIREFLY_DB_USER:-firefly_app} WITH PASSWORD '${FIREFLY_DB_PASSWORD:-firefly_secure_placeholder_password}';
    CREATE DATABASE ${FIREFLY_DB_NAME:-firefly} OWNER ${FIREFLY_DB_USER:-firefly_app};
    REVOKE CONNECT ON DATABASE ${FIREFLY_DB_NAME:-firefly} FROM PUBLIC;
    GRANT ALL PRIVILEGES ON DATABASE ${FIREFLY_DB_NAME:-firefly} TO ${FIREFLY_DB_USER:-firefly_app};

    -- Paperless DB & Role
    CREATE USER ${PAPERLESS_DB_USER:-paperless_app} WITH PASSWORD '${PAPERLESS_DB_PASSWORD:-paperless_secure_placeholder_password}';
    CREATE DATABASE ${PAPERLESS_DB_NAME:-paperless} OWNER ${PAPERLESS_DB_USER:-paperless_app};
    REVOKE CONNECT ON DATABASE ${PAPERLESS_DB_NAME:-paperless} FROM PUBLIC;
    GRANT ALL PRIVILEGES ON DATABASE ${PAPERLESS_DB_NAME:-paperless} TO ${PAPERLESS_DB_USER:-paperless_app};

    -- OpenProject DB & Role
    CREATE USER ${OPENPROJECT_DB_USER:-openproject_app} WITH PASSWORD '${OPENPROJECT_DB_PASSWORD:-openproject_secure_placeholder_password}';
    CREATE DATABASE ${OPENPROJECT_DB_NAME:-openproject} OWNER ${OPENPROJECT_DB_USER:-openproject_app};
    REVOKE CONNECT ON DATABASE ${OPENPROJECT_DB_NAME:-openproject} FROM PUBLIC;
    GRANT ALL PRIVILEGES ON DATABASE ${OPENPROJECT_DB_NAME:-openproject} TO ${OPENPROJECT_DB_USER:-openproject_app};
EOSQL

# Enable pgvector extension on relevant databases
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "${PAPERLESS_DB_NAME:-paperless}" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS vector;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS vector;
EOSQL