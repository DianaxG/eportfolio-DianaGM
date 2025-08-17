-- ENHANCED VERSION (normalized + indexes) — Best-effort based on Excel columns

CREATE SCHEMA IF NOT EXISTS miami;

CREATE TABLE IF NOT EXISTS miami.dim_offense (
  offense_id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS miami.dim_location (
  location_id SERIAL PRIMARY KEY,
  name TEXT UNIQUE NOT NULL
);

-- Storms (curated from StormData)
CREATE TABLE IF NOT EXISTS miami.storm (
  storm_id BIGINT PRIMARY KEY,
  start_ts TIMESTAMPTZ,
  end_ts   TIMESTAMPTZ,
  severity TEXT,
  notes    TEXT
);

-- Crime incidents (fact)
CREATE TABLE IF NOT EXISTS miami.incident (
  incident_id BIGINT PRIMARY KEY,
  occurred_at TIMESTAMPTZ NOT NULL,
  offense_id  INT NOT NULL REFERENCES miami.dim_offense(offense_id),
  location_id INT NOT NULL REFERENCES miami.dim_location(location_id),
  raw_lat     DOUBLE PRECISION,
  raw_lon     DOUBLE PRECISION,
  storm_id    BIGINT NULL REFERENCES miami.storm(storm_id)
);

CREATE INDEX IF NOT EXISTS idx_incident_time ON miami.incident(occurred_at);
CREATE INDEX IF NOT EXISTS idx_incident_offense ON miami.incident(offense_id);
CREATE INDEX IF NOT EXISTS idx_incident_location ON miami.incident(location_id);
