-- Minimal schema mirroring Excel columns

CREATE TABLE IF NOT EXISTS CrimeData (
  "Unnamed:_0" TEXT
);

CREATE TABLE IF NOT EXISTS StormData (
  "Event_ID" BIGINT NOT NULL,
  "Crime_type" TEXT NOT NULL,
  "Crime_Code" BIGINT NOT NULL,
  "City" TEXT NOT NULL,
  "City_Code" BIGINT NOT NULL,
  "Date_of_crime" TIMESTAMPTZ NOT NULL
);
