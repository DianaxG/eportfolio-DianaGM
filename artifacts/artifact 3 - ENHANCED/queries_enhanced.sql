-- ENHANCED analytics queries

-- 1) Incident counts by offense and location
SELECT o.name AS offense, l.name AS location, COUNT(*) AS incidents
FROM miami.incident i
JOIN miami.dim_offense o ON o.offense_id = i.offense_id
JOIN miami.dim_location l ON l.location_id = i.location_id
GROUP BY o.name, l.name
ORDER BY incidents DESC;

-- 2) Incidents during storms (by timestamp windows)
SELECT i.incident_id, i.occurred_at, o.name AS offense, l.name AS location, s.severity
FROM miami.incident i
JOIN miami.dim_offense o ON o.offense_id = i.offense_id
JOIN miami.dim_location l ON l.location_id = i.location_id
JOIN miami.storm s ON s.storm_id = i.storm_id
WHERE i.occurred_at BETWEEN s.start_ts AND s.end_ts
ORDER BY i.occurred_at;

-- 3) Hourly bucketed incident counts
SELECT date_trunc('hour', occurred_at) AS hour_bucket, COUNT(*) AS incidents
FROM miami.incident
GROUP BY hour_bucket
ORDER BY hour_bucket;
