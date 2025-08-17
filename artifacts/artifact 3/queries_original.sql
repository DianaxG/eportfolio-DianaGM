
-- Count of incidents by a likely offense/type column (best-effort; adjust column name if different)
SELECT /* guess */ COALESCE("Offense", "offense", "Crime_Type", "crime_type") AS offense_label,
       COUNT(*) AS incidents
FROM "CrimeData"
GROUP BY offense_label
ORDER BY incidents DESC;

-- Join by likely storm_id/date if present (best-effort)
-- simple to reflect the original baseline.
SELECT c.*, s.*
FROM "CrimeData" c
LEFT JOIN "StormData" s
  ON (COALESCE(c."storm_id", c."Storm_ID") = COALESCE(s."storm_id", s."Storm_ID"))
   OR (DATE(c."date") = DATE(s."date"))
LIMIT 50;
