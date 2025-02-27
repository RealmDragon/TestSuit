DO $$
BEGIN
  IF NOT EXISTS (SELECT datname FROM pg_database WHERE datname = 'medical_site_db') THEN
    CREATE DATABASE medical_site_db;
  END IF;
END $$;

CREATE USER medical_user WITH PASSWORD '1997';
GRANT CONNECT ON DATABASE medical_site_db TO medical_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO medical_user;